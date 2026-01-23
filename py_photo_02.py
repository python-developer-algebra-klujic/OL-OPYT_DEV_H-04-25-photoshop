from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')

print(jpg_fotografija.size) # (3992, 2242)

# Treba unijeti koordinate dviju tocaka - gornja lijevi o donja desno
# napravite crop fotografije tako da uzmete gornju tocku za cetvrtinu
#   desno i dolje te donju tocku za cetvrtinu gore i lijevo
jpg_fotografija.crop()