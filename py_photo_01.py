from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')
png_fotografija = Image.open('Algebra_campus.png')

print(jpg_fotografija.size)
print(png_fotografija.size)
