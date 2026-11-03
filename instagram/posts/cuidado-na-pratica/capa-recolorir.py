# Recolore o fundo da foto da capa para o Tiffany #9FC5BD (sem mexer na mão e no celular),
# apaga a barra de digitar e funde o pé no creme #F0F0E9.
# Uso: python3 instagram/posts/cuidado-na-pratica/capa-recolorir.py instagram/posts/cuidado-na-pratica/fotos/
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
P=sys.argv[1]
im=Image.open(P+'capa-celular.jpg').convert('RGB')
d=ImageDraw.Draw(im); d.rectangle((288,1164,742,1250),fill=im.getpixel((520,1120)))  # apaga a barra de digitar
a=np.asarray(im).astype(np.float32)/255
hsv=np.asarray(im.convert('HSV')).astype(np.float32)/255
h=hsv[...,0]*360; s=hsv[...,1]; v=hsv[...,2]
# peso: tons de fundo (ciano/azul) fora do celular
w=np.clip(1-np.abs(h-195)/45,0,1)*np.clip((s-0.03)/0.06,0,1)
ph=Image.new('L',im.size,255); ImageDraw.Draw(ph).rounded_rectangle((250,260,778,1330),radius=90,fill=0)
w*=np.asarray(ph.filter(ImageFilter.GaussianBlur(3))).astype(np.float32)/255
w=np.asarray(Image.fromarray((w*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32)/255
# alvo: Tiffany #9FC5BD com a luz da foto (mais claro em cima, mais denso embaixo)
tif=np.array([0x9f,0xc5,0xbd],np.float32)/255
lum=(0.3*a[...,0]+0.59*a[...,1]+0.11*a[...,2])
alvo=tif[None,None,:]*np.clip(lum/0.80,0.9,1.25)[...,None]
alvo=np.clip(alvo,0,1)
out=a*(1-w[...,None])+alvo*w[...,None]
im=Image.fromarray((out*255).astype(np.uint8))
sc=1080/1024; im=im.resize((1080,round(1536*sc)),Image.LANCZOS)
foto=im.crop((0,160,1080,1510))
# degradê para o creme atrás do título
creme=Image.new('RGB',(1080,1350),(0xf0,0xf0,0xe9))
# transição curva e suave: começa mais alto à esquerda (onde fica o título) e mais baixo à
# direita, com curva de suavização e desfoque, para não parecer uma linha reta
xs=np.arange(1080)[None,:]; ys=np.arange(1350)[:,None]
inicio=500+190*(xs/1080)**1.6+18*np.sin(xs/1080*np.pi*1.3)
t=np.clip((ys-inicio)/380,0,1); t=t*t*(3-2*t)
m=Image.fromarray((250*t).astype(np.uint8)).filter(ImageFilter.GaussianBlur(28))
Image.composite(creme,foto,m).save(P+'c-01.jpg',quality=90)
print('ok')
