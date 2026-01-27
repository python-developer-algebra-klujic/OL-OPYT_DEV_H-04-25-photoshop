from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')

print(jpg_fotografija.size) # (3992, 2242)

jpg_fotografija_resized = jpg_fotografija.resize(size=(int(3992/2), int(2242/2)))
jpg_fotografija_resized.save('jpg_fotografija_resized.jpg')

print(jpg_fotografija_resized.size)