from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from customer import Cust_Win
from gallery import resort_photos
from room import Booking_Room
from details import DetailsAdd


def main_window():
    win = Tk()
    obj = HotelManagementSystem(win)
    win.mainloop()


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("RESORT OPERATIONS")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("Icon.ico")

        # ====================Title===================================
        # title_lbl=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="green",bd=5,relief=RIDGE)
        # title_lbl.pack(side=TOP,fill=X)

        img1 = Image.open(r"images\title8.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(
            self.root, image=self.photoimage1, bg="black", bd=5, relief=RIDGE
        )
        lblimg1.place(x=2, y=2, width=1550, height=140)

        img2 = Image.open(r"images\logo.png")
        img2 = img2.resize((200, 140), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimage2)
        # lblimg2.place(x=690,y=0,width=220,height=140)
        lblimg2.place(x=3, y=3, width=200, height=140)

        # =================MainFrame=====================================
        main_frame = Frame(self.root, bd=3, relief=RIDGE)
        main_frame.place(x=0, y=180, width=1550, height=620)

        title_lbl = Label(
            self.root,
            text="RESORT OPERATIONS PLATFORM",
            font=("times new roman", 38, "bold"),
            bg="navy",
            fg="gold",
            bd=3,
            relief=RIDGE,
        )
        title_lbl.place(x=0, y=140, width=1550, height=50)

        def time():
            string = strftime("%I:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(
            title_lbl,
            font=("times new roman", 17, "bold"),
            background="navy",
            foreground="gold",
        )
        lbl.place(x=0, y=1, width=140)
        time()

        img3 = Image.open(r"images\hotel front.jpg")
        img3 = img3.resize((1310, 600), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimage3, bd=5, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=610)

        # =================== menu buttons frames=========================

        menu_lbl = Label(
            main_frame,
            text="MENU",
            font=("times new roman", 18, "bold"),
            bg="navy",
            fg="gold",
        )
        menu_lbl.place(x=0, y=5, width=230)

        btn_frame = Frame(main_frame, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        img5 = Image.open(r"images\side view.jpg")
        img5 = img5.resize((230, 210), Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimage6, bd=5, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img6 = Image.open(r"images\LOVE.jpg")
        img6 = img6.resize((230, 190), Image.LANCZOS)
        self.photoimage8 = ImageTk.PhotoImage(img6)
        lblimg1 = Label(main_frame, image=self.photoimage8, bd=5, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

        add_cust = Button(
            btn_frame,
            text="CUSTOMER",
            bd=0,
            width=22,
            command=self.cust_details_win,
            font=("times new roman", 14, "bold"),
            bg="navy",
            fg="gold",
            cursor="hand2",
        )
        add_cust.grid(row=0, column=0, pady=1)

        add_cust = Button(
            btn_frame,
            text="BOOKING",
            bd=0,
            relief=RIDGE,
            width=22,
            command=self.booking_room,
            font=("times new roman", 14, "bold"),
            bg="navy",
            fg="gold",
            cursor="hand2",
        )
        add_cust.grid(row=1, column=0, pady=1)

        add_cust = Button(
            btn_frame,
            text="DETAILS",
            bd=0,
            relief=RIDGE,
            width=22,
            command=self.details_add,
            font=("times new roman", 14, "bold"),
            bg="navy",
            fg="gold",
            cursor="hand2",
        )
        add_cust.grid(row=2, column=0, pady=1)

        add_cust = Button(
            btn_frame,
            text="GALLERY",
            bd=0,
            relief=RIDGE,
            width=22,
            command=self.gallery_win,
            font=("times new roman", 14, "bold"),
            bg="navy",
            fg="gold",
            cursor="hand2",
        )
        add_cust.grid(row=3, column=0, pady=1)

        add_cust = Button(
            btn_frame,
            text="LOGOUT ",
            command=self.return_login,
            bd=0,
            relief=RIDGE,
            width=22,
            font=("times new roman", 14, "bold"),
            bg="navy",
            fg="gold",
            cursor="hand2",
        )
        add_cust.grid(row=4, column=0, pady=1)

    def cust_details_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def booking_room(self):
        self.new_window = Toplevel(self.root)
        self.app = Booking_Room(self.new_window)

    def details_add(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsAdd(self.new_window)

    def gallery_win(self):
        self.new_window = Toplevel(self.root)
        self.app = resort_photos(self.new_window)

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main_window()
