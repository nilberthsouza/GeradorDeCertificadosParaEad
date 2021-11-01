from PIL import Image

#cria imagem vazia
img = Image.new('RGB', (1280,800), (255, 255, 255))

#define fonte
title_font = ImageFont.truetype('OldLondon.ttf', 150)

#importa logo
logo = Image.open('logo.png')

#cola logo em img
img.paste(logo, (100, 50))

#define  texto
title_text = "Certificado Formação"

#tona img editavel
image_editable = ImageDraw.Draw(img)

#edita a imagem e salva
image_editable.text((15,15), title_text, (237, 230, 211),font=title_font)
img.save("image.png", "PNG")
