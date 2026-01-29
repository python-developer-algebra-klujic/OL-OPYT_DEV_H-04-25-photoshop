import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter



MAX_WIDTH = 2000
temp_image = None
original_image = None
def update_temp_image(updated_image: Image.Image):
    global temp_image
    temp_image = updated_image.copy()

def load_image(image_path='./images/Algebra_campus.jpg'):
    global original_image

    image = Image.open(image_path)
    if image.width >= MAX_WIDTH:
        width = int(image.width / 2)
        height = int(image.height / 2)
        image = image.resize(size=(width, height))

    update_temp_image(image)
    original_image = image.copy()
    return image

def get_lbl_image(image=None):
    if image is not None:
        return ImageTk.PhotoImage(image=image)
    else:
        loaded_image = load_image()
        return ImageTk.PhotoImage(image=loaded_image)

def get_image_data():
    return f'Image size:\t{temp_image.size}\nImage format:\t{temp_image.format}\nImage mode:\t{temp_image.mode}'



def to_black_white():
    image = temp_image.copy()
    image = image.convert(mode='L')
    # sacuvaj ove promjene u tmp varijabli
    update_temp_image(image)

    # azurirj korisnicko sucelje (UI)
    lbl_image = ImageTk.PhotoImage(image=image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image

def flip_tb():
    image = temp_image.copy()
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # sacuvaj ove promjene u tmp varijabli
    update_temp_image(image)

    # azurirj korisnicko sucelje (UI)
    lbl_image = ImageTk.PhotoImage(image=image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image

def flip_lr():
    image = temp_image.copy()
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    # sacuvaj ove promjene u tmp varijabli
    update_temp_image(image)

    # azurirj korisnicko sucelje (UI)
    lbl_image = ImageTk.PhotoImage(image=image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image

def blur():
    image = temp_image.copy()
    image = image.filter(ImageFilter.GaussianBlur(radius=5))
    # sacuvaj ove promjene u tmp varijabli
    update_temp_image(image)

    # azurirj korisnicko sucelje (UI)
    lbl_image = ImageTk.PhotoImage(image=image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image



def save():
    temp_image.save('./images/New_image.jpg', format='JPEG')

def open():
    image_path = filedialog.askopenfilename()
    image = load_image(image_path)
    lbl_image = get_lbl_image(image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image
    lbl_image_data_var.set(value=get_image_data())

def reset():
    image = original_image.copy()
    update_temp_image(original_image)
    lbl_image = get_lbl_image(image)
    lbl_display_photo.config(image=lbl_image)
    lbl_display_photo.image = lbl_image



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
                     text='Save',
                     command=save)
btn_save.grid(column=0, row=1, padx=10, pady=10, ipadx=10, ipady=10)
btn_open = tk.Button(frm_actions,
                     text='Open',
                     command=open)
btn_open.grid(column=1, row=1, padx=10, pady=10, ipadx=10, ipady=10)
btn_reset = tk.Button(frm_actions,
                      text='Reset',
                      command=reset)
btn_reset.grid(column=2, row=1, padx=10, pady=10, ipadx=10, ipady=10)


btn_change_to_black_white = tk.Button(frm_actions,
                                      text='To Black \'n white',
                                      command=to_black_white)
btn_change_to_black_white.grid(column=0, columnspan=3, row=2, padx=10, pady=10, ipadx=10, ipady=10)
btn_flip_lr = tk.Button(frm_actions,
                        text='Flip left right',
                        command=flip_lr)
btn_flip_lr.grid(column=0, row=3, padx=10, pady=10, ipadx=10, ipady=10)
btn_flip_tb = tk.Button(frm_actions,
                        text='Flip top bottom',
                        command=flip_tb)
btn_flip_tb.grid(column=2, row=3, padx=10, pady=10, ipadx=10, ipady=10)
btn_blur = tk.Button(frm_actions,
                        text='Blur',
                        command=blur)
btn_blur.grid(column=0, columnspan=3, row=4, padx=10, pady=10, ipadx=10, ipady=10)

#endregion


if __name__ == '__main__':
    root.mainloop()
