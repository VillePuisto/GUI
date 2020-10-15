from tkinter import *
from PIL import ImageTk, Image

def showImage():
        lbl1.configure(image=image_tk)
        btn.configure(text = "load image!", command=showImage1)

def showImage1():
        lbl1.configure(image=image_tk1)
        btn.configure(text = "load image!", command=showImage)

root = Tk()
c = Frame(root, padding=10)
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

fname = "a.jpg"
image_tk = ImageTk.PhotoImage(Image.open(fname))

fname1 = "b.jpg"
image_tk1 = ImageTk.PhotoImage(Image.open(fname1))  # new image object


btn = root.Button(c, text="load image", command=showImage)
lbl1 = root.Label(c)
btn.grid(column=0, row=0, sticky=N, pady=5, padx=5)
lbl1.grid(column=1, row=1, sticky=N, pady=5, padx=5)

root.mainloop()