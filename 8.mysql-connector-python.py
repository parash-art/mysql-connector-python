from tkinter import *
import mysql.connector #pip install mysql-connector-python-rf and pip install mysql-connector
 
 
class Window():
    def __init__(self, master):
        self.master = master
 
        self.Main = Frame(self.master)
 
 
        # ----- Section 1
 
        self.section1 = Frame(self.Main)
 
        self.L1 = Label(self.section1, text = "First Name")
        self.L1.pack(padx = 5, pady = 5, side = LEFT)
 
        self.E1 = Entry(self.section1)
        self.E1.pack(padx = 5, pady = 5, side = LEFT)
 
        self.L2 = Label(self.section1, text = "Last Name")
        self.L2.pack(padx = 5, pady = 5, side = LEFT)
 
        self.E2 = Entry(self.section1)
        self.E2.pack(padx = 5, pady = 5, side = LEFT)
         
        self.section1.pack(padx = 5, pady = 5, expand = True, fill = X)
 
        # ----- Section 1
 
 
        # ----- Section 2
 
        self.section2 = Frame(self.Main)
 
        self.L3 = Label(self.section2, text = "Address")
        self.L3.pack(padx = 5, pady = 5, side = LEFT)
 
        self.E3 = Entry(self.section2, width = 30)
        self.E3.pack(padx = 5, pady = 5, side = LEFT, expand = True, fill = X)
 
        self.L4 = Label(self.section2, text = "Postal Code")
        self.L4.pack(padx = 5, pady = 5, side = LEFT)
 
        self.E4 = Entry(self.section2, width = 6)
        self.E4.pack(padx = 5, pady = 5, side = LEFT)
 
         
        self.section2.pack(padx = 5, pady = 5, expand = True, fill = X)
 
        # ----- Section 2
 
 
 
        # ----- Section 3
        self.section3 = Frame(self.Main)
        ## ---- Section 3 sub-frame 1
         
        self.section3_1 = Frame(self.section3)        
 
        self.L5 = Label(self.section3_1, text = "Pick your Gender")
        self.L5.pack(padx = 5, pady = 5)
 
        self.Rvar1 = IntVar()
 
        self.R1 = Radiobutton(self.section3_1, text = "Male", variable = self.Rvar1, value = 1)
        self.R1.pack(padx = 5, pady = 5)
        self.R2 = Radiobutton(self.section3_1, text = "Female", variable = self.Rvar1, value = 2)
        self.R2.pack(padx = 5, pady = 5)
        self.R3 = Radiobutton(self.section3_1, text = "Other", variable = self.Rvar1, value = 3)
        self.R3.pack(padx = 5, pady = 5)
 
        self.section3_1.pack(padx = 50, pady = 5, side = LEFT)
 
        ## ---- Section 3 sub-frame 1
 
 
        ## ---- Section 3 sub-frame 2
         
        self.section3_2 = Frame(self.section3)        
 
        self.L5 = Label(self.section3_2, text = "Pick an Option")
        self.L5.pack(padx = 5, pady = 5)
 
        self.Cvar1 = IntVar()
        self.Cvar2 = IntVar()
        self.Cvar3 = IntVar()
 
        self.C1 = Checkbutton(self.section3_2, text = "Option1", variable = self.Cvar1)
        self.C1.pack(padx = 5, pady = 5)
        self.C2 = Checkbutton(self.section3_2, text = "Option2", variable = self.Cvar2)
        self.C2.pack(padx = 5, pady = 5)
        self.C3 = Checkbutton(self.section3_2, text = "Option3", variable = self.Cvar3)
        self.C3.pack(padx = 5, pady = 5)
 
        self.section3_2.pack(padx = 50, pady = 5, side = RIGHT)
         
        ## ---- Section 3 sub-frame 2
         
 
        self.section3.pack(padx = 5, pady = 5, expand = True, fill = X)
        # ----- Section 3
 
 
        # ----- Section 4
 
        self.section4 = Frame(self.Main)
 
        self.L6 = Label(self.section4, text = "About yourself: ")
        self.L6.pack(padx = 5, pady = 5)
 
        self.T1 = Text(self.section4, height = 5, width = 30)
        self.T1.pack(padx =5, pady = 5, expand = True, fill = X)
 
        self.section4.pack(padx = 5, pady = 5, expand = True, fill = X)
         
 
        # ----- Section 4
 
        self.B0 = Button(self.Main, text = "Connect", command = self.connect)
        self.B0.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B1 = Button(self.Main, text = "Create Table", command = self.create_table)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B2 = Button(self.Main, text = "Submit", command = self.submit)
        self.B2.pack(padx = 5, pady = 5, side = RIGHT)
 
        self.Main.pack(padx = 5, pady = 5, expand = True, fill = X)
 
 
    def connect(self):
        try:
            self.db = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database = "data")
 
            self.cursor = self.db.cursor()
            print("Connection Succeeded")
        except:
            print("Connection Failed")
 
 
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE regis_data
                                (firstname VARCHAR(30),
                                 lastname VARCHAR(30),
                                 address VARCHAR(100),
                                 postal_code INT,
                                 gender INT,
                                 choice INT,
                                 comments TEXT)""")
        except:
            print("Table already created")
 
 
    def submit(self):
        sql = """INSERT INTO regis_data (firstname, lastname, address, postal_code, gender, choice, comments)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (self.E1.get(), self.E2.get(), self.E3.get(), self.E4.get(), str(self.Rvar1.get()),
                  str(self.Cvar1.get()) + str(self.Cvar2.get()) + str(self.Cvar3.get()), self.T1.get("1.0", "end"))
 
        self.cursor.execute(sql, values)
        self.db.commit()
         
 
 
root = Tk()

































window = Window(root)
root.mainloop()