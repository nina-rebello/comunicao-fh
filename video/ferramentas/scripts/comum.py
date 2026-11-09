"""Caminhos e funções usadas por todos os scripts do fluxo de edição."""
import glob, json, os, subprocess, unicodedata

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FERR = os.path.join(RAIZ, "video", "ferramentas")
CE = os.path.join(FERR, "Calude Editing")


def _sub(nome):
    """Acha uma subpasta de CE sem depender da forma Unicode do acento."""
    alvo = unicodedata.normalize("NFC", nome)
    for p in os.listdir(CE):
        if unicodedata.normalize("NFC", p) == alvo:
            return os.path.join(CE, p)
    raise FileNotFoundError(nome)


def pasta_brutos(): return _sub("Vídeos Brutos")
def pasta_prontos(): return _sub("Vídeos Prontos")
def pasta_trabalho(video): return os.path.join(CE, "_CLAUDE", video)


def bruto(video):
    achados = glob.glob(os.path.join(pasta_brutos(), video + ".*"))
    if not achados:
        raise FileNotFoundError(f"bruto {video} não encontrado")
    return achados[0]


def carregar(video):
    with open(os.path.join(pasta_trabalho(video), "projeto.json")) as f:
        return json.load(f)


def salvar(video, estado):
    p = os.path.join(pasta_trabalho(video), "projeto.json")
    with open(p + ".tmp", "w") as f:
        json.dump(estado, f, ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)


def frame(segundos, fps):
    """Única conversão de segundos para frame do fluxo inteiro."""
    return int(round(segundos * fps))


def ffprobe(arquivo):
    out = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", arquivo],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def silencios(arquivo, db=-35, dur=0.25):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", arquivo, "-af", f"silencedetect=n={db}dB:d={dur}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    ini, res = None, []
    for linha in err.splitlines():
        if "silence_start:" in linha:
            ini = float(linha.split("silence_start:")[1].split()[0])
        elif "silence_end:" in linha and ini is not None:
            res.append([round(ini, 3), round(float(linha.split("silence_end:")[1].split()[0]), 3)])
            ini = None
    return res
