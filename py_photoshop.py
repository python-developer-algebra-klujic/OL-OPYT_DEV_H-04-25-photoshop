import tkinter as tk
from PIL import Image, ImageTk



def load_image():
    image = Image.open('./images/Algebra_campus.jpg')
    width = int(image.width / 2)
    height = int(image.height / 2)
    image = image.resize(size=(width, height))
    return image

def get_lbl_image():
    image = load_image()
    return ImageTk.PhotoImage(image=image)

def get_image_data():
    image = load_image()
    return f'Image size:\t{image.size}\nImage format:\t{image.format}\nImage mode:\t{image.mode}'


root = tk.Tk()
root.title('Py Tkinter Photoshop')

#region Photo Frame
# Lijevi stupac za prikaz fotografije
frm_photo = tk.Frame(root)
frm_photo.grid(column=0, row=0, padx=10, pady=10, ipadx=5, ipady=5)

lbl_image = get_lbl_image()
lbl_display_photo = tk.Label(frm_photo,
                             text='FOTOGRAFIJA',
                             image=lbl_image)
lbl_display_photo.grid(column=0, row=0, sticky='NSEW')

#endregion

#region Actions Frame
# Desni stupac s akcijama
frm_actions = tk.Frame(root)
frm_actions.grid(column=1, row=0, padx=10, pady=10, ipadx=5, ipady=5)


lbl_image_data_var = tk.StringVar(value=get_image_data())
lbl_image_data = tk.Label(frm_actions,
                          text='Podaci o fotografiji',
                          textvariable=lbl_image_data_var,
                          justify=tk.LEFT)
lbl_image_data.grid(column=0, row=0, columnspan=3,
                    padx=10, pady=10, ipadx=10, ipady=10,
                    sticky='EW')

btn_save = tk.Button(frm_actions,
                     text='Save')
btn_save.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10)
btn_open = tk.Button(frm_actions,
                     text='Open')
btn_open.grid(column=1, row=1, padx=10, pady=10, ipadx=10, ipady=10)
btn_reset = tk.Button(frm_actions,
                      text='Reset')
btn_reset.grid(column=2, row=1, padx=10, pady=10, ipadx=10, ipady=10)

#endregion

if __name__ == '__main__':
    root.mainloop()
