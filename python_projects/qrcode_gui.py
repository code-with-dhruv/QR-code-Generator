import qrcode
from PIL import Image
from tkinter import *
import sys
from PIL import ImageTk, Image

win=Tk()
win.resizable(False,False)
win.geometry("1000x1000")
win.title("Qr_Codify")








def quit1():
    win.destroy()


def qrcodemake(k):
    qr=qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(k)

    qr.make(fit=True)
    

    img=qr.make_image(fill_color='black',back_color='white')
    img.save('Example.png')
    img=Image.open('Example.png')
def display_image():
    img.show()
def add_input():
        k=input("Path to be redirected to")

img = ImageTk.PhotoImage(Image.open("Example.png"))
button=Button(win,text='convert to qr code',height= 1, width=20,command=qrcodemake)#done
button1=Button(win,text='exit',height= 1, width=20,command=quit1)#done
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

button.place(relx= .5, rely= .6, anchor= CENTER)
button1.place(relx= .5, rely= .65, anchor= CENTER)

# Create a Label Widget to display the text or Image
label = Label(win, image = img)
label.pack()

win.mainloop()



