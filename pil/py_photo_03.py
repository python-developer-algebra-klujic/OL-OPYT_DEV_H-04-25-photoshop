from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')

print(jpg_fotografija.mode)

jpg_fotografija_converted_L = jpg_fotografija.convert(mode='L')
jpg_fotografija_converted_L.save('jpg_fotografija_converted_L.jpg', 'JPEG')

jpg_fotografija_converted_CMYK = jpg_fotografija.convert(mode='CMYK')
jpg_fotografija_converted_CMYK.save('jpg_fotografija_converted_CMYK.jpg', 'JPEG')
