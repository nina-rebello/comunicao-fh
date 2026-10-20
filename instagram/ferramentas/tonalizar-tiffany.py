# Deixa uma foto no tom Tiffany: gradiente de 4 paradas (verde nas sombras, Tiffany nos meios-tons, Tiffany bem
# claro nas luzes), misturado com 15% da cor original da foto. Feito para o teste do slide 4 do post de 21/10 (20/10).
# Uso: python3 tonalizar-tiffany.py foto.jpg saida.jpg [mistura da cor original, 0 a 1] [gama]
import sys
import numpy as np
from PIL import Image

def hexc(h): return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], float)

PARADAS = [(0, '#1F3A36'), (.5, '#6FA79E'), (.78, '#96C5BD'), (1, '#E4F2EF')]

def tonalizar(src, dst, orig=.15, gama=1.0):
    im = np.asarray(Image.open(src).convert('RGB'), float) / 255
    L = im @ [.299, .587, .114]
    lo, hi = np.percentile(L, 1), np.percentile(L, 99)
    L = np.clip((L - lo) / (hi - lo), 0, 1) ** gama
    xs = [p for p, _ in PARADAS]
    duo = np.stack([np.interp(L, xs, [hexc(c)[k] for _, c in PARADAS]) for k in range(3)], -1)
    out = duo * (1 - orig) + im * 255 * orig
    Image.fromarray(np.clip(out, 0, 255).astype('uint8')).save(dst, quality=90)

if __name__ == '__main__':
    tonalizar(sys.argv[1], sys.argv[2], *(float(a) for a in sys.argv[3:]))
