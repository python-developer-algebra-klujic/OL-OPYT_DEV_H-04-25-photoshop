from PIL import Image

jpg_fotografija = Image.open('Algebra_campus.jpg')

print(jpg_fotografija.size) # (3992, 2242)

# jpg_fotografija_transposed_LR = jpg_fotografija.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# jpg_fotografija_transposed_LR.save('jpg_fotografija_transposed_LR.jpg')

# jpg_fotografija_transposed_TB = jpg_fotografija.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# jpg_fotografija_transposed_TB.save('jpg_fotografija_transposed_TB.jpg')

# jpg_fotografija_transposed_R90 = jpg_fotografija.transpose(Image.Transpose.ROTATE_90)
# jpg_fotografija_transposed_R90.save('jpg_fotografija_transposed_R90.jpg')

jpg_fotografija_transposed_R180 = jpg_fotografija.transpose(Image.Transpose.ROTATE_180)
jpg_fotografija_transposed_R180.save('jpg_fotografija_transposed_R180.jpg')
