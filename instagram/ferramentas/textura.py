"""Texturas de marca-texto e de tinta impressa no papel (PNG com transparência, em 2x)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def _suave(n, escala, rng):
    k = max(2, n // escala + 2)
    v = rng.normal(0, 1, k)
    x = np.linspace(0, k - 1, n)
    return np.interp(x, np.arange(k), v)

def marca(w, h, cor, seed=0, alfa=0.86, sentido='h', borda=5, mascara=None):
    """w,h em px do slide; devolve imagem 2x. sentido 'h' = traço horizontal (marca-texto), 'v' = barra."""
    rng = np.random.default_rng(seed)
    W, H = int(w * 2), int(h * 2)
    a = np.full((H, W), alfa, float)
    if sentido == 'h':
        a += _suave(H, 6, rng)[:, None] * 0.05          # listras ao longo do traço
        a += _suave(W, 40, rng)[None, :] * 0.04          # tinta mais carregada em trechos
    else:
        a += _suave(W, 8, rng)[None, :] * 0.04
        a += _suave(H, 60, rng)[:, None] * 0.03
    a += rng.normal(0, 0.05, (H, W))                     # granulado
    pontos = (rng.random((H, W)) < 0.006).astype(float)  # falhas da tinta
    pontos = np.array(Image.fromarray((pontos * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.6)), float) / 255
    a -= pontos * 1.6
    # bordas irregulares
    m = np.ones((H, W))
    if sentido == 'h':
        top = (np.abs(_suave(W, 120, rng)) * borda * 1.1 + borda * .4).astype(int)
        bot = (np.abs(_suave(W, 120, rng)) * borda * 1.1 + borda * .4).astype(int)
        yy = np.arange(H)[:, None]
        m[(yy < top[None, :]) | (yy > H - 1 - bot[None, :])] = 0
        esq = (np.abs(_suave(H, 40, rng)) * borda * 1.6).astype(int)
        dir_ = (np.abs(_suave(H, 40, rng)) * borda * 1.6).astype(int)
        xx = np.arange(W)[None, :]
        m[(xx < esq[:, None]) | (xx > W - 1 - dir_[:, None])] = 0
        # tinta acumula nas pontas
        ponta = np.clip(1 - np.minimum(xx, W - 1 - xx) / 40, 0, 1) * 0.10
        a += ponta
    else:
        lado = (np.abs(_suave(H, 30, rng)) * 2).astype(int)
        xx = np.arange(W)[None, :]
        m[(xx < lado[:, None]) | (xx > W - 1 - lado[:, None])] = 0
        topo = (np.abs(_suave(W, 30, rng)) * 2).astype(int)
        yy = np.arange(H)[:, None]
        m[yy < topo[None, :]] = 0
    if mascara is not None:
        m = m * (np.array(mascara.convert('L').resize((W, H)), float) / 255)
    a = np.clip(a, 0, 1) * m
    rgb = np.ones((H, W, 3)) * np.array(cor, float)
    rgb *= (1 - rng.normal(0, 0.025, (H, W, 1)))         # leve variação de cor
    out = np.dstack([np.clip(rgb, 0, 255), a * 255]).astype('uint8')
    return Image.fromarray(out, 'RGBA')

def pessoa(w, h):
    """Máscara de pessoa (cabeça e corpo), em 2x, nas proporções 120x220."""
    W, H = int(w * 2), int(h * 2)
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    sx, sy = W / 120, H / 220
    d.ellipse((32 * sx, 2 * sy, 88 * sx, 58 * sy), fill=255)
    d.rounded_rectangle((12 * sx, 68 * sy, 108 * sx, 160 * sy), radius=int(18 * sx), fill=255)
    d.rectangle((32 * sx, 140 * sy, 88 * sx, 220 * sy), fill=255)
    return m
