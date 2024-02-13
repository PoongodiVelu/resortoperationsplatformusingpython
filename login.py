from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import HotelManagementSystem
from flask import Flask, render_template, request, redirect, url_for


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("Icon.ico")

        self.bg = ImageTk.PhotoImage(file=r"images\back.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=425)

        img1 = Image.open(r"images\usericon.png")
        img1 = img1.resize((90, 90), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=90, height=90)

        get_str = Label(
            frame,
            text="Get Started",
            font=("times new roman", 20, "bold"),
            fg="black",
            bg="white",
        )
        get_str.place(x=95, y=105)

        # label
        username = lbl = Label(
            frame,
            text="Username",
            font=("times new roman", 12, "bold"),
            fg="black",
            bg="white",
        )
        username.place(x=70, y=150)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=175, width=270)

        password = lbl = Label(
            frame,
            text="Password",
            font=("times new roman", 12, "bold"),
            fg="black",
            bg="white",
        )
        password.place(x=70, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=245, width=270)

        # ***********Icon Images*****************
        img2 = Image.open(r"images\usernameicon.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg1.place(x=650, y=320, width=25, height=25)

        img3 = Image.open(r"images\passwordicon.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        lblimg1.place(x=650, y=392, width=25, height=25)

        # LoginButton
        btn_login = Button(
            frame,
            text="Login",
            borderwidth=3,
            relief=RAISED,
            command=self.login,
            cursor="hand2",
            font=("times new roman", 16, "bold"),
            fg="white",
            bg="red",
            activebackground="#B00857",
        )
        btn_login.place(x=110, y=300, width=120, height=35)

        # registerbutton
        registerbtn = Button(
            frame,
            text="New User Register",
            command=self.rigister_window,
            font=("times new roman", 10, "bold"),
            borderwidth=0,
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="white",
        )
        registerbtn.place(x=15, y=350, width=160)

        # forgetpassbtn
        registerbtn = Button(
            frame,
            text="Forget Password",
            command=self.forgot_password_window,
            font=("times new roman", 10, "bold"),
            borderwidth=0,
            fg="black",
            bg="white",
            activeforeground="white",
            activebackground="white",
        )
        registerbtn.place(x=10, y=375, width=160)

    def rigister_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == " " or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field required")
        # elif self.txtuser.get() == "POO" and self.txtpass.get() == "1234":
        # messagebox.showinfo("Success", "WELCOME TO ISLAND RESORT")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anandhi29@123",
                database="mydata",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "select * from register where email=%s and password=%s",
                (self.txtuser.get(), self.txtpass.get()),
            )

            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Inavalid Username & password")
            else:
                open_main = messagebox.askyesno("Yes No", "Access only admin")

                if open_main > 0:
                    messagebox.showinfo("Success", "WELCOME TO PARADISE RESORT")
                    # self.showimage("iconimage.png")

                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # *******************reset password*********************
    def reset_pass(self):
        if (
            self.combo_securiy_Q.get() == "Select"
            or self.txt_security.get() == ""
            or self.txt_newpass == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Anandhi29@123",
                    database="mydata",
                )
                cur = conn.cursor()
                query = "select * from register where email=%s and securityQ=%s and securityA=%s"
                value = (
                    self.txtuser.get(),
                    self.combo_securiy_Q.get(),
                    self.txt_security.get(),
                )
                cur.execute(query, value)
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror(
                        "Error",
                        "Please select the correct security quetion/Enter answer",
                        parent=self.root2,
                    )
                else:
                    query = "update register set password=%s where email=%s"
                    value = (self.txt_newpass.get(), self.txtuser.get())
                    cur.execute(query, value)
                    # row2 = cur.fetchone()
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Success",
                        "Your password has been reset,Please login with new password",
                        parent=self.root2,
                    )
                    self.root2.destroy()
                    # self.reset()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Due To:{str(es)}", parent=self.root2
                )

    # ****************forgrt password window*********************
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Plaese Enter the Email address to reset password"
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anandhi29@123",
                database="mydata",
            )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error", "Plaese enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.wm_iconbitmap("Icon.ico")

                self.root2.geometry("340x450+610+170")

                l = Label(
                    self.root2,
                    text="Forget Password",
                    font=("times new roman", 20, "bold"),
                    fg="red",
                )
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(
                    self.root2,
                    text="Select Security Questions",
                    font=("times new roman", 15, "bold"),
                    fg="black",
                )
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(
                    self.root2, font=("times new roman", 15, "bold"), state="readonly"
                )
                self.combo_securiy_Q["values"] = (
                    "Select",
                    "Your Birth Place",
                    "Your Girlfriend name",
                    "Your Pet Name",
                )
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(
                    self.root2,
                    text="Security Answer",
                    font=("times new roman", 15, "bold"),
                    fg="black",
                )
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(
                    self.root2, font=("times new roman", 15, "bold")
                )
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(
                    self.root2,
                    text="New Password",
                    font=("times new roman", 15, "bold"),
                    fg="black",
                )
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(
                    self.root2, font=("times new roman", 15, "bold"), show="*"
                )
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(
                    self.root2,
                    text="Reset",
                    command=self.reset_pass,
                    font=("times new roman", 15, "bold"),
                    fg="White",
                    bg="green",
                )
                btn.place(x=120, y=290, width=100)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("Icon.ico")

        # *************VARIABLES**************
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ************BG IMAGE***************
        self.bg = ImageTk.PhotoImage(file=r"images\regipage.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # *************LEFT IMAGE***********************
        self.bg1 = ImageTk.PhotoImage(file=r"images\round.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # **************MAIN FRAME******************
        frame = Frame(self.root, bd=3, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            fg="dodgerblue2",
            bg="white",
        )
        register_lbl.place(x=40, y=20)

        # ************LABEL AND ENTRY***********************

        # ------------------row1
        fname = Label(
            frame, text="First Name", font=("times new roman", 15, "bold"), bg="white"
        )
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15, "bold")
        )
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(
            frame,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold")
        )
        self.txt_lname.place(x=370, y=130, width=250)

        # -----------------row2

        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15, "bold")
        )
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(
            frame,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold")
        )
        self.txt_email.place(x=370, y=200, width=250)

        # ------------------row3

        security_Q = Label(
            frame,
            text="Select Security Questions",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(
            frame,
            textvariable=self.var_securityQ,
            font=("times new roman", 15, "bold"),
            state="readonly",
        )
        self.combo_securiy_Q["values"] = (
            "Select",
            "Your Birth Place",
            "Your Girlfriend name",
            "Your Pet Name",
        )
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A = Label(
            frame,
            text="Security Answer",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_SecurityA, font=("times new roman", 15, "bold")
        )
        self.txt_security.place(x=370, y=270, width=250)

        # ----------------------row4

        pswd = Label(
            frame,
            text="Password ",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame,
            textvariable=self.var_pass,
            font=("times new roman", 15, "bold"),
            show="*",
        )
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(
            frame,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame,
            textvariable=self.var_confpass,
            font=("times new roman", 15, "bold"),
            show="*",
        )
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ***************CHECK BUTTON***************
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(
            frame,
            variable=self.var_check,
            text="I Agree the Terms & Conditions",
            font=("times new roman", 12, "bold"),
            bg="white",
            onvalue=1,
            offvalue=0,
        )
        self.checkbtn.place(x=50, y=380)

        # ****************buttons*************
        img = Image.open(r"images\register3.png")
        img = img.resize((200, 90), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(
            frame,
            image=self.photoimage,
            command=self.register_data,
            borderwidth=0,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="white",
        )
        b1.place(x=40, y=420, width=200)

        img1 = Image.open(r"images\login now3.png")
        img1 = img1.resize((200, 90), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(
            frame,
            image=self.photoimage1,
            command=self.return_login,
            borderwidth=0,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            fg="white",
            bg="white",
        )
        b1.place(x=370, y=420, width=200)

    # **************Function declaration******************

    def register_data(self):
        if (
            self.var_fname.get() == ""
            or self.var_email.get() == ""
            or self.var_securityQ.get() == "Select"
        ):
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Plaese agree our terms ane condition")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anandhi29@123",
                database="mydata",
            )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist,plaese try another email"
                )
            else:
                my_cursor.execute(
                    "insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get(),
                    ),
                )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
