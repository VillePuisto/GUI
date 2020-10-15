from tkinter import *
from PIL import ImageTk, Image

window = Tk()
#creating title information
window.title("Ville's GUI Assignment")
window.geometry("1400x900")
#creating headline
top_label = Label(window, text="Ville's GUI Assignment",
                  bg='grey',
                  pady=30,
                  font=('Arial Bold', 30))
top_label.pack(fill=X)

#Creating picture captions
image_label = Label(window, text="Los Angeles Lakers",
                    fg="purple",
                    font="Arial 20 bold")
image_label.place(x=270, y=630)
image_label1 = Label(window, text="Miami Heat",
                     fg="red",
                     font="Arial 20 bold")
image_label1.place(y=630, x=860)

#Creating images
bg_img = ImageTk.PhotoImage(Image.open("lakers.gif"))
bg_label = Label(image=bg_img)
bg_label.place(x=200, y=200)
bg_img1 = ImageTk.PhotoImage(Image.open("heat2.gif"))
bg_label = Label(image=bg_img1)
bg_label.place(x=850, y=250)

#Create sliders
slider = Scale(window, from_=0, to=100)
slider.place(x=50, y=300)
slider = Scale(window, from_=0, to=100, orient=HORIZONTAL)
slider.place(x=30, y=400)


#where and how to open pictures
lakers_image = Image.open("title.jpg")
photo = ImageTk.PhotoImage(lakers_image)
heat_image = Image.open("heatt1.jpg")
photo1 = ImageTk.PhotoImage(heat_image)

def click1():
    lakerslabel = Label(image=photo)
    lakerslabel.lakers_image = photo
    lakerslabel.place(x=150, y=130)


def click2():
    heatlabel = Label(image=photo1)
    heatlabel.heat_image = photo1
    heatlabel.place(x=100, y=130)




#creating a question and buttons
leftLabel = Label(window, text='Which team is going to win the Nba finals?', font="Ariel 15", pady=30)
leftLabel.pack()


button1 = Button(text='Lakers',
                 command=click1,
                 bg='purple',
                 fg='gold',
                 pady=5)
button1.pack()

button2 = Button(text='Heat',
                 command=click2,
                 fg='black',
                 bg='red',
                 pady=7,
                 padx=7)
button2.pack()

Man = StringVar()
def selection():
   selection = "You are a " + str(Man.get())
   radio_label.config(text=selection)

#Creating Radiobuttons
right_label = Label(window, text="Are you a Man or a Women?", padx=20, pady=20)
right_label.pack(anchor=E)
radio1 = Radiobutton(window, text="Man", padx=20, variable=Man, value="Man", command=selection)
radio1.pack(anchor=E)
radio2 = Radiobutton(window, text="Women", padx=20, variable=Man, value="Women", command=selection)
radio2.pack(anchor=E)

radio_label = right_label
right_label.pack(anchor=E)

top_label = Label(window)


#made checkbuttons
checkvar1 = IntVar()

checkvar2 = IntVar()

checkvar3 = IntVar()

chkbtn1 = Checkbutton(window, text="Bulls",fg="red", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)

chkbtn2 = Checkbutton(window, text="Warriors", fg="gold", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)

chkbtn3 = Checkbutton(window, text="Knicks", fg="blue", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)

chkbtn1.place(x=15, y=600)

chkbtn2.place(x=24, y=640)

chkbtn3.place(x=20, y=680)

favlabel = Label(window, text="What teams do you like?")
favlabel.place(x=20, y=550)

#made exit program button
button_quit = Button(window, text="Exit Program", padx=7, command=window.quit)
button_quit.place(x=1300, y=800)

window.mainloop()