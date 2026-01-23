from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')

print(jpg_fotografija.size) # (3992, 2242)

# Treba unijeti koordinate dviju tocaka - gornja lijevi o donja desno
# napravite crop fotografije tako da uzmete gornju tocku za cetvrtinu
#   desno i dolje te donju tocku za cetvrtinu gore i lijevo
left = jpg_fotografija.size[0] / 4
upper = jpg_fotografija.size[1] / 4
right = jpg_fotografija.size[0] - (jpg_fotografija.size[0] / 4)
lower = jpg_fotografija.size[1] - (jpg_fotografija.size[1] / 4)

box = (left, upper, right, lower)

jpg_fotografija_cropped = jpg_fotografija.crop(box)
jpg_fotografija_cropped.save('jpg_fotografija_cropped.png', 'PNG')
