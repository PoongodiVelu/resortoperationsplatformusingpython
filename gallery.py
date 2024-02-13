from tkinter import *
import tkinter
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter.ttk import LabelFrame


class resort_photos:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1305x600+220+210")
        self.root.wm_iconbitmap("Icon.ico")

        title_lbl = Label(
            self.root,
            text="RESORT GALLERY  ",
            font=("times new roman", 18, "bold"),
            bg="navy",
            fg="goldenrod1",
            bd=3,
            relief=RIDGE,
        )
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img0 = Image.open(r"images\logohotel2.png")
        img0 = img0.resize((100, 32), Image.LANCZOS)
        self.photoimage0 = ImageTk.PhotoImage(img0)
        lblimg0 = Label(self.root, image=self.photoimage0, bg="navy", borderwidth=0)
        # lblimg2.place(x=690,y=0,width=220,height=140)
        lblimg0.place(x=5, y=2, width=100, height=32)

        Image_frame = LabelFrame(
            self.root,
            borderwidth=3,
            relief=RIDGE,
        )
        Image_frame.place(x=25, y=50, width=1250, height=500)

        img1 = Image.open("Gallery/img1.jpeg")
        img1 = img1.resize((300, 230), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        l1 = Label(Image_frame, image=self.photoImg1, borderwidth=0)
        l1.place(x=10, y=1)

        img2 = Image.open("Gallery/img2.jpeg")
        img2 = img2.resize((300, 230), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        l2 = Label(Image_frame, image=self.photoImg2, borderwidth=0)
        l2.place(x=315, y=1)

        img3 = Image.open("Gallery/img3.jpeg")
        img3 = img3.resize((300, 230), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        l3 = Label(Image_frame, image=self.photoImg3, borderwidth=0)
        l3.place(x=10, y=235)

        img4 = Image.open("Gallery/img9.jpeg")
        img4 = img4.resize((300, 230), Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        l4 = Label(Image_frame, image=self.photoImg4, borderwidth=0)
        l4.place(x=315, y=235)

        img5 = Image.open("Gallery/img5.jpeg")
        img5 = img5.resize((300, 230), Image.LANCZOS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        l5 = Label(Image_frame, image=self.photoImg5, borderwidth=0)
        l5.place(x=620, y=1)

        img6 = Image.open("Gallery/img6.jpeg")
        img6 = img6.resize((300, 230), Image.LANCZOS)
        self.photoImg6 = ImageTk.PhotoImage(img6)
        l6 = Label(Image_frame, image=self.photoImg6, borderwidth=0)
        l6.place(x=620, y=235)

        img7 = Image.open("Gallery/img7.jpeg")
        img7 = img7.resize((300, 230), Image.LANCZOS)
        self.photoImg7 = ImageTk.PhotoImage(img7)
        l7 = Label(Image_frame, image=self.photoImg7, borderwidth=0)
        l7.place(x=925, y=1)

        img8 = Image.open("Gallery/img8.jpg")
        img8 = img8.resize((300, 230), Image.LANCZOS)
        self.photoImg8 = ImageTk.PhotoImage(img8)
        l8 = Label(Image_frame, image=self.photoImg8, borderwidth=0)
        l8.place(x=925, y=235)


if __name__ == "__main__":
    root = Tk()
    obj = resort_photos(root)
    root.mainloop()
