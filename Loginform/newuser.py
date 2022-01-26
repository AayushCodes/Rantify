import mysql.connector
from cProfile import label
from email.mime import image
from json.tool import main
from tkinter import*
from tkinter import ttk
from xml.sax.handler import feature_namespace_prefixes
from PIL import Image, ImageTk    #pip install pillow
from tkinter import messagebox
import mysql.connector

class newuser:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

# ================ Variables ============================================================================================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_secques = StringVar()
        self.var_secqans = StringVar()
        self.var_password = StringVar()
        self.var_confpass = StringVar()

# ================= bg image ============================================================================================
        self.bg = ImageTk.PhotoImage(file = r"C:\Users\aakas\Desktop\Loginform\pexels-jakub-novacek-924824.jpg")
        bg_lbl = Label(self.root, image = self.bg)
        bg_lbl.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# ================= left image ===========================================================================================
        self.leftbg = ImageTk.PhotoImage(file = r"C:\Users\aakas\Desktop\Loginform\MUSIC for your every rant.jpg")
        left_lbl = Label(self.root, image = self.leftbg)
        left_lbl.place(x = 50, y = 100, width = 389, height = 550)

        frame = Frame(self.root, bg = "white")
        frame.place(x = 439, y = 100, width = 1000, height = 550)

        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman", 20, "bold"),fg = "#4682B4", bg = "white")
        register_lbl.place(x = 20, y = 20)

# ================ label and entry ============================================================================================
    #------------ row 1 ------------------------------------------------------------------------------------------------------

        fname = Label(frame, text = "First Name", font = ("times new roman", 15, "bold"), bg = "white")
        fname.place(x = 50, y = 100)

        fname_entry = ttk.Entry(frame, textvariable = self.var_fname, font = ("times new roman", 15, "bold"))
        fname_entry.place(x = 50, y = 132, width = 250)

        l_name = Label(frame, text = "Last Name", font = ("times new roman", 15, "bold"), bg = "white")
        l_name.place(x = 370, y = 100)

        lname_entry = ttk.Entry(frame, textvariable = self.var_lname, font = ("times new roman", 15, "bold"))
        lname_entry.place(x = 370, y = 130, width = 250)

    #------------ row 2 ------------------------------------------------------------------------------------------------------
         
        contact = Label(frame, text = "Contact No", font = ("times new roman", 15, "bold"), bg = "white")
        contact.place(x = 50, y = 170)

        contact = ttk.Entry(frame, textvariable = self.var_contact, font = ("times new roman", 15, "bold"))
        contact.place(x = 50, y = 200, width = 250) 

        email = Label(frame, text = "Email/Username", font = ("times new roman", 15, "bold"), bg = "white")
        email.place(x = 370, y = 170)

        email = ttk.Entry(frame, textvariable = self.var_email, font = ("times new roman", 15, "bold"))
        email.place(x = 370, y = 200, width = 250) 

    #------------ row 3 ------------------------------------------------------------------------------------------------------

        secques = Label(frame, text = "Select Security Question", font = ("times new roman", 15, "bold"), bg = "white")
        secques.place(x = 50, y = 240)

        self.combo_secques = ttk.Combobox(frame, textvariable = self.var_secques, font = ("times new roman", 15, "bold"), state = "readonly")
        self.combo_secques["values"] = ("Select", "Your Birth Place", "Name of a person you despise", "Your least favourite Superhero", "Your favourite song")
        self.combo_secques.place(x = 50, y = 270, width = 250)
        self.combo_secques.current(0)

        secqans = Label(frame, text = "Security Question answer", font = ("times new roman", 15, "bold"), bg = "white")
        secqans.place(x = 370, y = 240)

        secqans = ttk.Entry(frame, textvariable = self.var_secqans, font = ("times new roman", 15, "bold"))
        secqans.place(x = 370, y = 268, width = 250)
        
    #------------ row 4 ------------------------------------------------------------------------------------------------------

        password = Label(frame, text = "Password", font = ("times new roman", 15, "bold"), bg = "white")
        password.place(x = 50, y = 310)

        password = ttk.Entry(frame, textvariable =  self.var_password, font = ("times new roman", 15, "bold"))
        password.place(x = 50, y = 336, width = 250) 

        cpass = Label(frame, text = "Confirm Password", font = ("times new roman", 15, "bold"), bg = "white")
        cpass.place(x = 370, y = 310)

        cpass = ttk.Entry(frame, textvariable = self.var_confpass, font = ("times new roman", 15, "bold"))
        cpass.place(x = 370, y = 336, width = 250)


    # ========== buttons =============================================================
   
        regnowimg = Image.open(r"C:\Users\aakas\Desktop\Loginform\regnowbutton.png")
        regnowimg = regnowimg.resize((200, 58))
        self.regnimg = ImageTk.PhotoImage(regnowimg)
        regnowbtn = Button(frame, image = self.regnimg, command = self.register_data, borderwidth=0, cursor = "hand2", fg="white")
        regnowbtn.place(x = 40, y = 405, width = 200)


        lognowimg = Image.open(r"C:\Users\aakas\Desktop\Loginform\sign-in-button-icon-isometric.jpg")
        lognowimg = lognowimg.resize((200, 140))
        self.loginimg = ImageTk.PhotoImage(lognowimg)
        lognowbtn = Button(frame, image = self.loginimg, borderwidth=0, cursor = "hand2", fg="white")
        lognowbtn.place(x = 400, y = 365, width = 200)


    # ========= Backend 1 - Function Declaration ====================================================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_secqans.get() == "" or self.var_secques.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords aren't same")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "new_schema")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                              self.var_fname.get(),
                                                                                              self.var_lname.get(),
                                                                                              self.var_contact.get(),
                                                                                              self.var_email.get(),
                                                                                              self.var_secques.get(),
                                                                                              self.var_secqans.get(),
                                                                                              self.var_password.get(),


                                                                                            )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")





if __name__ == "__main__":
        root = Tk()
        app = newuser(root)
        root.mainloop()
    
