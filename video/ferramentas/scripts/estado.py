"""Lê e muda o estado de um vídeo sem abrir o arquivo inteiro.

estado.py <video> status | <bloco> [--json] | --item <id>
estado.py <video> --set <caminho.com.pontos> <valor json ou texto>
estado.py <video> --etapa <etapa>=<status>
estado.py <video> --pendencia <etapa> "<texto>" | --resolver <id>
"""
import json, sys
from comum import carregar, salvar

ETAPAS = ["preparar", "plano", "motion", "camera", "som", "entrega"]


def status(e):
    print(f"{e['projeto']} · perfil {e.get('perfil')}")
    for et in ETAPAS:
        print(f"  {et:9} {e['etapas'].get(et, 'pendente')}")
    pend = [p for p in e.get("pendencias", []) if not p.get("resolvida")]
    for p in pend:
        print(f"  pendência {p['id']} ({p['etapa']}): {p['texto']}")
    mk = e.get("marcadores", [])
    if mk:
        print(f"  marcadores: {len(mk)}")
    for a in e.get("alertas", []):
        print(f"  ALERTA: {a}")


def resumo(v, nivel=0):
    pad = "  " * nivel
    if isinstance(v, dict):
        for k, x in v.items():
            if isinstance(x, (dict, list)):
                print(f"{pad}{k}:"); resumo(x, nivel + 1)
            else:
                print(f"{pad}{k}: {x}")
    elif isinstance(v, list):
        for x in v[:30]:
            print(f"{pad}- {json.dumps(x, ensure_ascii=False)[:160]}")
        if len(v) > 30:
            print(f"{pad}... (+{len(v) - 30})")
    else:
        print(f"{pad}{v}")


def achar_item(v, id_):
    if isinstance(v, dict):
        if v.get("id") == id_:
            return v
        v = list(v.values())
    if isinstance(v, list):
        for x in v:
            r = achar_item(x, id_)
            if r is not None:
                return r


def main(a):
    video, e = a[0], carregar(a[0])
    if a[1] == "status":
        status(e)
    elif a[1] == "--item":
        print(json.dumps(achar_item(e, a[2]), ensure_ascii=False, indent=1))
    elif a[1] == "--set":
        alvo, chaves = e, a[2].split(".")
        for k in chaves[:-1]:
            alvo = alvo.setdefault(k, {})
        try:
            alvo[chaves[-1]] = json.loads(a[3])
        except json.JSONDecodeError:
            alvo[chaves[-1]] = a[3]
        salvar(video, e)
    elif a[1] == "--etapa":
        et, st = a[2].split("=")
        e["etapas"][et] = st
        salvar(video, e)
    elif a[1] == "--pendencia":
        ps = e.setdefault("pendencias", [])
        ps.append({"id": f"p{len(ps) + 1:02}", "etapa": a[2], "texto": a[3]})
        salvar(video, e)
    elif a[1] == "--resolver":
        for p in e.get("pendencias", []):
            if p["id"] == a[2]:
                p["resolvida"] = True
        salvar(video, e)
    else:
        bloco = e.get(a[1])
        if "--json" in a:
            print(json.dumps(bloco, ensure_ascii=False, indent=1))
        else:
            resumo(bloco)


if __name__ == "__main__":
    main(sys.argv[1:])
