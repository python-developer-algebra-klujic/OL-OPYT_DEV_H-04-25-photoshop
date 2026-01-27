from PIL import Image, ImageDraw

jpg_fotografija = Image.open('Algebra_campus.jpg')
jpg_fotografija_draw = ImageDraw.Draw(jpg_fotografija)

jpg_fotografija_draw.rounded_rectangle(xy=[(250, 150), (3992-250, 2242-150)],
                                       radius=500)

jpg_fotografija.save('jpg_fotografija_rounded.jpg', 'JPEG')
