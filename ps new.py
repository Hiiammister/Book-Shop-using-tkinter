from tkinter import*
from tkinter.filedialog import askopenfilename
import os
import sqlite3
from random import randint, randrange
import tkinter.messagebox
import webbrowser

root=Tk()
root.wm_title("A mystical Book Shop")
root.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
root.geometry('1920x1080+0+0')


root.configure(bg='#EEAA00')
C =Canvas(root, height=3840, width=2160)

def Novels():
   
    books = {"Wuthering Heights , price : 2900": 2900, " Middlemarch , price: 4000": 4000, "Nineteen Eighty-Four , price : 4900": 4900, "The Lord of the Rings , price : 7000": 7000, "Diary of a Nobody, price: 5600": 5600}
    variable = StringVar()
    variable.set(list(books.keys())[0])

    def delete():
        Window9.destroy()
        
    def connect():
            
        root.state('iconic')
        if len(Entry1.get())==0:
            ans=tkinter.messagebox.showerror("warning","enter valid name")
        elif len(Entry3.get())!=10:
            bans=tkinter.messagebox.showerror("warning","enter valid phone number")
        elif len(Entry2.get())==0:
            hans=tkinter.messagebox.showerror("warning","enter valid name and surname")
        elif len(Entry1.get())==0 and len(Entry2.get())==0 and len(Entry3.get())==0:
            vans=tkinter.messagebox.showerror("warning","enter valid information")
        elif len(Entry6.get())==0:
            tans=tkinter.messagebox.showerror("warning","enter valid address")
            
            
        else:
            book=variable.get()
            ans=tkinter.messagebox.showinfo("Confirmation", "You are purchasing " + str(book))

            name = Entry1.get()
            surname = Entry2.get()
            phone_num = Entry3.get()
            book = variable.get()
            selected_book_cost = books[book]
            Address=Entry6.get()
            conn = sqlite3.connect('manganew7.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Novels_Purchased
                    (First_Name TEXT, Surname TEXT, phone_no INT, Book_purchased TEXT, Address TEXT, Cost INT)
                    '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Novels_Purchased(First_name, Surname, phone_no, Book_purchased, Address, Cost)VALUES
            (?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, phone_num, book, Address, selected_book_cost)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
    Window9=Toplevel(root)
    Window9.geometry('1920x1080')
    Window9.state('zoomed')
    Window9.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C10 =Canvas(Window9, height=3840, width=2160)
    img=PhotoImage(file = "novels.gif")
    C10.create_image(700,350,anchor=CENTER,image=img)
    C10.pack()
    Label1=Label(Window9, text="Welcome to the Novels section 📚!!!", bg="#ca5047", font="Times 34", borderwidth=5, relief="raised")
    Label1.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    Label2=Label(Window9, text="This more Sophisticated Section, So no weird introduction, enjoy your tea and biscuits", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label2.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    Label3=Label(Window9, text="Please Enter your Details for the same:-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label3.place(relx = 0.1, rely = 0.3)
    Label4=Label(Window9, text="Name:-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.4)
    Entry1=Entry(Window9, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry1.place(relx = 0.1, rely = 0.49)
    Label4=Label(Window9, text="SurName:-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.6)
    Entry2=Entry(Window9, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry2.place(relx = 0.1, rely = 0.69)
    Label4=Label(Window9, text="Mobile Number:-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.8)
    Entry3=Entry(Window9, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry3.place(relx = 0.1, rely = 0.89)
    Label4=Label(Window9, text="Book to be purchased ▼ :-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.35, rely = 0.40)
    #Entry4=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    #Entry4.place(relx = 0.35, rely = 0.49)
    combo = OptionMenu(Window9, variable, *books, command=connect)
    combo.config(bg="#f2d4a2")
    combo.config(height=2)
    combo.config(width=45)
    combo.config(font="Times 10")
    combo.place(relx=0.35, rely=0.49)
    Label5=Label(Window9, text="Address:-", bg="#ca5047", font="Times 20", borderwidth=5, relief="raised")
    Label5.place(relx=0.35, rely=0.6)
    Entry6=Entry(Window9, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry6.place(relx=0.35, rely=0.69)
    Button2=Button(Window9,text="Purchase" ,font="Times 20", bg="#ca5047", borderwidth=5, relief="raised", command=connect)
    Button2.place(relx = 0.35, rely = 0.79)
    button1=Button(Window9, bg="#ca5047", text="Go Back", font="Times  20",fg="Black", relief="raised", command=delete)    
    button1.place(relx=0.9, rely= 0.85)
    
    Window9.mainloop()
    
    

def Fiction():
    
    books = {"Age of Vice , price : 2600": 2600, "City Under One Roof , price: 3800": 3800, "Dune , price : 4800": 4800, "The Hitchhiker's Guide to the Galaxy , price : 5500": 5500, "Fahrenheit 451, price: 5600": 5600}
    variable = StringVar()
    variable.set(list(books.keys())[0])

    def delete():
        Window8.destroy()
    def connect():
            
        root.state('iconic')
        if len(Entry1.get())==0:
            ans=tkinter.messagebox.showerror("warning","enter valid name")
        elif len(Entry3.get())!=10:
            bans=tkinter.messagebox.showerror("warning","enter valid phone number")
        elif len(Entry2.get())==0:
            hans=tkinter.messagebox.showerror("warning","enter valid name and surname")
        elif len(Entry1.get())==0 and len(Entry2.get())==0 and len(Entry3.get())==0:
            vans=tkinter.messagebox.showerror("warning","enter valid information")
        elif len(Entry6.get())==0:
            tans=tkinter.messagebox.showerror("warning","enter valid address")
            
            
        else:
            book=variable.get()
            ans=tkinter.messagebox.showinfo("Confirmation", "You are purchasing " + str(book))

            name = Entry1.get()
            surname = Entry2.get()
            phone_num = Entry3.get()
            book = variable.get()
            selected_book_cost = books[book]
            Address=Entry6.get()
            conn = sqlite3.connect('manganew7.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Fiction_Purchased
                    (First_Name TEXT, Surname TEXT, phone_no INT, Book_purchased TEXT, Address TEXT, Cost INT)
                    '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Fiction_Purchased(First_name, Surname, phone_no, Book_purchased, Address, Cost)VALUES
            (?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, phone_num, book, Address, selected_book_cost)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
    Window8=Toplevel(root)
    Window8.geometry('1920x1080')
    Window8.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    Window8.state('zoomed')
    C9 =Canvas(Window8, height=3840, width=2160)
    img=PhotoImage(file = "fiction.gif")
    C9.create_image(700,350,anchor=CENTER,image=img)
    C9.pack()
    Label1=Label(Window8, text="Welcome to the Fiction section 🛸!!!", bg="#ff6a00", font="Times 34", borderwidth=5, relief="raised")
    Label1.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    Label2=Label(Window8, text="In this section, you can ask what is your model number ?, Welcome to the Fiction Section", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label2.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    Label3=Label(Window8, text="Please Enter your Details for the same:-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label3.place(relx = 0.1, rely = 0.3)
    Label4=Label(Window8, text="Name:-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.4)
    Entry1=Entry(Window8, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry1.place(relx = 0.1, rely = 0.49)
    Label4=Label(Window8, text="SurName:-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.6)
    Entry2=Entry(Window8, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry2.place(relx = 0.1, rely = 0.69)
    Label4=Label(Window8, text="Mobile Number:-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.8)
    Entry3=Entry(Window8, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry3.place(relx = 0.1, rely = 0.89)
    Label4=Label(Window8, text="Book to be purchased ▼ :-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.35, rely = 0.40)
    #Entry4=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    #Entry4.place(relx = 0.35, rely = 0.49)
    combo = OptionMenu(Window8, variable, *books, command=connect)
    combo.config(bg="#f2d4a2")
    combo.config(height=2)
    combo.config(width=45)
    combo.config(font="Times 10")
    combo.place(relx=0.35, rely=0.49)
    Label5=Label(Window8, text="Address:-", bg="#ff6a00", font="Times 20", borderwidth=5, relief="raised")
    Label5.place(relx=0.35, rely=0.6)
    Entry6=Entry(Window8, font="Times 15", bg="#f2d4a2", borderwidth=5, relief="raised")
    Entry6.place(relx=0.35, rely=0.69)
    Button2=Button(Window8,text="Purchase" ,font="Times 20", bg="#ff6a00", borderwidth=5, relief="raised", command=connect)
    Button2.place(relx = 0.35, rely = 0.79)
    button1=Button(Window8, bg="#ff6a00", text="Go Back", font="Times  20",fg="Black", relief="raised", command=delete)    
    button1.place(relx=0.9, rely= 0.85)
    
    Window8.mainloop()
    

def Horror():
    
    
    def delete():
        Window7.destroy()
    def connect():
            
        root.state('iconic')
        if len(Entry1.get())==0:
            ans=tkinter.messagebox.showerror("warning","enter valid name")
        elif len(Entry3.get())!=10:
            bans=tkinter.messagebox.showerror("warning","enter valid phone number")
        elif len(Entry2.get())==0:
            hans=tkinter.messagebox.showerror("warning","enter valid name and surname")
        elif len(Entry1.get())==0 and len(Entry2.get())==0 and len(Entry3.get())==0:
            vans=tkinter.messagebox.showerror("warning","enter valid information")
        elif len(Entry6.get())==0:
            tans=tkinter.messagebox.showerror("warning","enter valid address")
            
            
        else:
            book=variable.get()
            ans=tkinter.messagebox.showinfo("Confirmation", "You are purchasing " + str(book))

            name = Entry1.get()
            surname = Entry2.get()
            phone_num = Entry3.get()
            book = variable.get()
            selected_book_cost = books[book]
            Address=Entry6.get()
            conn = sqlite3.connect('manganew7.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Horror_Purchased
                    (First_Name TEXT, Surname TEXT, phone_no INT, Book_purchased TEXT, Address TEXT, Cost INT)
                    '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Horror_Purchased(First_name, Surname, phone_no, Book_purchased, Address, Cost)VALUES
            (?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, phone_num, book, Address, selected_book_cost)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
    books = {"The Haunting of Hill House: 2000": 2000, "Dracula, price: 3000": 3000, "Mexican Gothic, price: 3500": 3500, "The Stand, price: 4500": 4500, "Caroline, price: 5000": 5000}
    variable = StringVar()
    variable.set(list(books.keys())[0])
    
    Window7=Toplevel(root)
    Window7.geometry('1920x1080')
    Window7.state('zoomed')
    Window7.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C8 =Canvas(Window7, height=3840, width=2160)
    img=PhotoImage(file = "nun2.gif")
    C8.create_image(700,350,anchor=CENTER,image=img)
    C8.pack()
    Label1=Label(Window7, text="Welcome to the HOrror section 💀!!!", bg="#678286", font="Times 34", borderwidth=5, relief="raised")
    Label1.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    Label2=Label(Window7, text="We have all sinned, now suffer and perish in this hell of the Horror Section", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label2.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    Label3=Label(Window7, text="Please Enter your Details for the same:-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label3.place(relx = 0.1, rely = 0.3)
    Label4=Label(Window7, text="Name:-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.4)
    Entry1=Entry(Window7, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry1.place(relx = 0.1, rely = 0.49)
    Label4=Label(Window7, text="SurName:-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.6)
    Entry2=Entry(Window7, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry2.place(relx = 0.1, rely = 0.69)
    Label4=Label(Window7, text="Mobile Number:-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.8)
    Entry3=Entry(Window7, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry3.place(relx = 0.1, rely = 0.89)
    Label4=Label(Window7, text="Book to be purchased ▼ :-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.35, rely = 0.40)
    #Entry4=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    #Entry4.place(relx = 0.35, rely = 0.49)
    combo = OptionMenu(Window7, variable, *books, command=connect)
    combo.config(bg="#dfdfdf")
    combo.config(height=2)
    combo.config(width=30)
    combo.config(font="Times 10")
    combo.place(relx=0.35, rely=0.49)
    Label5=Label(Window7, text="Address:-", bg="#678286", font="Times 20", borderwidth=5, relief="raised")
    Label5.place(relx=0.35, rely=0.6)
    Entry6=Entry(Window7, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry6.place(relx=0.35, rely=0.69)
    Button2=Button(Window7,text="Purchase" ,font="Times 20", bg="#dfdfdf", borderwidth=5, relief="raised", command=connect)
    Button2.place(relx = 0.35, rely = 0.79)
    button1=Button(Window7, bg="Black", text="Go Back", font="Times  20",fg="White", relief="raised", command=delete)    
    button1.place(relx=0.9, rely= 0.85)
    
    Window7.mainloop()
    


def Manga():
    
    books = {"Attack On Titan, price: 2000": 2000, "Berserk, price: 3000": 3000, "Chainsaw Man, price: 3500": 3500, "Dragon ball Z, price: 4500": 4500, "Echanted, price: 5000": 5000}
    variable = StringVar()
    variable.set(list(books.keys())[0])

    def delete():
        Window6.destroy()

    def connect():
            
        root.state('iconic')
        if len(Entry1.get())==0:
            ans=tkinter.messagebox.showerror("warning","enter valid name")
        elif len(Entry3.get())!=10:
            bans=tkinter.messagebox.showerror("warning","enter valid phone number")
        elif len(Entry2.get())==0:
            hans=tkinter.messagebox.showerror("warning","enter valid name and surname")
        elif len(Entry1.get())==0 and len(Entry2.get())==0 and len(Entry3.get())==0:
            vans=tkinter.messagebox.showerror("warning","enter valid information")
        elif len(Entry6.get())==0:
            tans=tkinter.messagebox.showerror("warning","enter valid address")
            
            
        else:
            book=variable.get()
            ans=tkinter.messagebox.showinfo("Confirmation", "You are purchasing " + str(book))

            name = Entry1.get()
            surname = Entry2.get()
            phone_num = Entry3.get()
            book = variable.get()
            selected_book_cost = books[book]
            Address=Entry6.get()
            
            conn = sqlite3.connect('manganew7.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Manga_Purchased
                    (First_Name TEXT, Surname TEXT, phone_no INT, Book_purchased TEXT, Address TEXT, Cost INT)
                    '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Manga_Purchased(First_name, Surname, phone_no, Book_purchased, Address, Cost)VALUES
            (?,?,?,?,?,?)'''
            data_insert_tuple = (name, surname, phone_num, book, Address, selected_book_cost)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

    Window6=Toplevel(root)
    Window6.geometry('1920x1080')
    Window6.state('zoomed')
    Window6.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C7 =Canvas(Window6, height=3840, width=2160)
    img=PhotoImage(file = "bnha.gif")
    C7.create_image(800,150,anchor=CENTER,image=img)
    C7.pack()
    Label1=Label(Window6, text="Welcome to the Manga section!!!", bg="#606060", font="Times 34", borderwidth=5, relief="raised")
    Label1.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    Label2=Label(Window6, text="We have all the mangas you can have, just tell us the name and we shall get it for you", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label2.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    Label3=Label(Window6, text="Please Enter your Details for the same:-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label3.place(relx = 0.1, rely = 0.3)
    Label4=Label(Window6, text="Name:-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.4)
    Entry1=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry1.place(relx = 0.1, rely = 0.49)
    Label4=Label(Window6, text="SurName:-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.6)
    Entry2=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry2.place(relx = 0.1, rely = 0.69)
    Label4=Label(Window6, text="Mobile Number:-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.1, rely = 0.8)
    Entry3=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry3.place(relx = 0.1, rely = 0.89)
    Label4=Label(Window6, text="Book to be purchased ▼ :-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label4.place(relx = 0.35, rely = 0.40)
    #Entry4=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    #Entry4.place(relx = 0.35, rely = 0.49)
    combo = OptionMenu(Window6, variable, *books, command=connect)
    combo.config(bg="#dfdfdf")
    combo.config(height=2)
    combo.config(width=25)
    combo.config(font="Times 10")
    combo.place(relx=0.35, rely=0.49)
    Label5=Label(Window6, text="Address:-", bg="#606060", font="Times 20", borderwidth=5, relief="raised")
    Label5.place(relx=0.35, rely=0.6)
    Entry6=Entry(Window6, font="Times 15", bg="#dfdfdf", borderwidth=5, relief="raised")
    Entry6.place(relx=0.35, rely=0.69)
    Button2=Button(Window6,text="Purchase" ,font="Times 20", bg="#dfdfdf", borderwidth=5, relief="raised", command=connect)
    Button2.place(relx = 0.35, rely = 0.79)
    button1=Button(Window6, bg="Black", text="Go Back", font="Times  20",fg="White", relief="raised", command=delete )    
    button1.place(relx=0.9, rely= 0.85)
    
    
    Window6.mainloop()


def Buy():
    def NewScreen():
        def delete():
            Window4.destroy()

        Window4=Toplevel(root)
        Window4.geometry('1920x1080')
        Window4.state('zoomed')
        Window4.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
        C5 =Canvas(Window4, height=3840, width=2160)
        img=PhotoImage(file = "book1.gif")
        C5.create_image(800,150,anchor=CENTER,image=img)
        C5.pack()
        Label1=Label(Window4,text="We have all the books of the world, what do you want?", bg="#887778", font="Times 34", borderwidth=5, relief="raised")
        Label1.place(relx=0.5, rely=0.35, anchor=CENTER)
        Button1=Button(Window4, text="Manga", bg="#ce5b65", font="Times 25", borderwidth=5, relief="raised", command=Manga)
        Button1.place(relx=0.5, rely=0.55, anchor=CENTER)
        Button2=Button(Window4, text="Horror", bg="#ce5b65", font="Times 25", borderwidth=5, relief="raised", command=Horror)
        Button2.place(relx=0.35, rely=0.60)
        Button3=Button(Window4, text="Fiction", bg="#ce5b65", font="Times 25", borderwidth=5, relief="raised", command=Fiction)
        Button3.place(relx=0.56, rely=0.60)
        Button3=Button(Window4, text="Novels", bg="#ce5b65", font="Times 25", borderwidth=5, relief="raised", command=Novels)
        Button3.place(relx=0.45, rely=0.71)
        Label5=Label(Window4, text="TYPES", bg="#887778", font="Times 30", borderwidth=5, relief="raised")
        Label5.place(relx=0.45, rely=0.61)
        button1=Button(Window4, bg="#ce5b65", text="Go Back", font="Times  20", relief="raised", command=delete )    
        button1.place(relx=0.9, rely= 0.85)
        Window4.mainloop()
    def delete():
        Window3.destroy()
        root.state('zoomed')
    Window3=Toplevel(root)
    Window3.state('zoomed')
    Window3.geometry('1920x1080')
    Window3.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C3 =Canvas(Window3, height=3840, width=2160)
    img=PhotoImage(file = "library.gif")
    C3.create_image(800,150,anchor=CENTER,image=img)
    C4=Canvas(Window3, height=200, width=800)
    C4.create_image(800, 150, image=img)
    Label1=Label(Window3,text="Welcome to this humble abode!!!", bg="#80B280", font="Times 34", borderwidth=5, relief="raised")
    Label1.place(relx=0.5, rely=0.35, anchor=CENTER)
    Label2=Label(Window3, text="In this humble abode, you can buy all sorts of books from Earthy to Heavenly"
                 "\nWhile this offers all sorts of spells, simply story books, it can be very useful"
                 "\nSO,i'll end my introduction with a quote 'with stars being as bright as dark as night sky, let knowledge be your light'",bg="#80B280", font="Times 20", borderwidth=5, relief="raised")
    Label2.place(relx=0.5, rely=0.55, anchor=CENTER)
    button1=Button(Window3, bg="#4D934D", text="Go Back", font="Times  20", relief="raised", command=delete )    
    button1.place(relx=0.9, rely= 0.85)
    Button2=Button(Window3, text="-------Continue-------", font="Times  20", bg="#4D934D", relief="raised",command=NewScreen )
    Button2.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    C3.pack()
    Window3.mainloop()
    


def Resolution():
    
    def oR0():
        root.geometry('1920x1080')
        Window1.destroy()
        root.state('zoomed')
    def oR():
        root.geometry('1660x480')
        Window1.destroy()
    def oR1():
        root.geometry('1280x720')
        
        
        Window1.destroy()
    def delete():
        Window1.destroy()
    Window1=Toplevel(root)
    Window1.state('zoomed')
    Window1.geometry('1920x1080')
    Window1.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C2 =Canvas(Window1, height=3840, width=2160)
    img=PhotoImage(file = "library.gif")
    C2.create_image(800,150,anchor=CENTER,image=img)

    Title=Label(Window1, relief="ridge", text="Resolutions",bg="#80B280", font="Times 34", borderwidth=5)
    Title.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    button1=Button(Window1, bg="#4D934D" ,text="1920 x 1080", font="Times 20", relief="raised", command=oR0)
    button1.place(relx=0.5, rely=0.45, anchor=CENTER)
    
    button1=Button(Window1, bg="#4D934D" ,text="1660 x 480", font="Times 20", relief="raised", command=oR)
    button1.place(relx=0.5, rely=0.55, anchor=CENTER)
    button2=Button(Window1, bg="#4D934D" ,text="1280 x 720", font="Times 20", relief="raised", command=oR1)
    button2.place(relx=0.5, rely=0.55, anchor=CENTER)
    button5=Button(Window1, bg="#4D934D", text="Go Back", font="Times  20", relief="raised", command=delete )
    button5.place(relx=0.9, rely= 0.85)
    C2.pack()
    Window1.mainloop()

def settings():
    
    def delete():
        Window.destroy()
    
    
    Window = Toplevel(root)
    Window.state('zoomed')
    Window.geometry('1920x1080')
    Window.wm_iconbitmap("TCET_Logo_Transparent_Bg.ico")
    C1 =Canvas(Window, height=3840, width=2160)
    img=PhotoImage(file = "library.gif")
    C1.create_image(800,150,anchor=CENTER,image=img)
    lable1=Label(Window, bg="#4D934D", text="Settings", font="Times 20", relief="raised")
    lable1.place(relx=0.5, rely=0.1, anchor=CENTER)
    button4=Button(Window, bg="#4D934D", text="Change Resolution!!", font="Times  20", relief="raised", command=Resolution )
        
    button4.place(relx=0.5, rely= 0.55, anchor=CENTER)
    button5=Button(Window, bg="#4D934D", text="Go Back", font="Times  20", relief="raised", command=delete )
        
    button5.place(relx=0.9, rely= 0.85)
    C1.pack()
    Window.mainloop()

def Git():
    webbrowser.open_new(r"https://github.com/Hiiammister")
    
    
    
def mainscreen():
    def exit1():
        gans=tkinter.messagebox.askquestion("Exit", "Are you sure you want to exit the Book Shop 🥲 ?")
        if gans=="yes":
            root.destroy()
        

    #menu=Menu(root)

    #root.config(menu=menu)
    #filemenu=Menu(menu)
    #menu.add_cascade(label='file', menu=filemenu)
    #filemenu.add_command(label="New")
    #filemenu.add_command(label="Open")
    #filemenu.add_command(label="Exit")

    img=PhotoImage(file = "library.gif")
    C.create_image(800,150,anchor=CENTER,image=img)
    root.state('zoomed')
            


    Title=Label(C, relief="ridge", text="Welcome to the Mystical Book Shop ",bg="#80B280", font="Times 34", borderwidth=5)
    Title.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    Welcome=Label(C, relief="groove",bg="#80B280", text="In this library store you will gets all sorts of books, ranging from novels to mangas", font="Times 20", borderwidth=5)
    Welcome.place(relx = 0.5, rely = 0.2, anchor=CENTER)
    #Welcome1=Label(C, relief="ridge",bg="#80B280", text="", font="Times 20", borderwidth=5)
    #Welcome1.place(relx = 0.5, rely = 0.4, anchor=CENTER)

    Button1=Button(C,bg="#4D934D", text="Start Shopping!!", font="Times  20", relief="raised", command=Buy) 
    Button1.place(relx=0.5, rely= 0.45, anchor=CENTER)

    Button2=Button(C, bg="#4D934D", text="Settings ⚙️ ", font="Times 20", relief="raised", command=settings)
    Button2.place(relx=0.5, rely=0.55, anchor=CENTER)

    Button2=Button(C, bg="#4D934D", text="About Us (Github)", font="Times 20", relief="raised", command=Git)
    Button2.place(relx=0.5, rely=0.65, anchor=CENTER)

    Button3=Button(C, bg="#4D934D", text="------Exit------", font="Times 20", relief="raised", command=exit1)
    Button3.place(relx=0.5, rely=0.75, anchor=CENTER)

    acc=Label(C,relief="groove", bg="#80B280", text="Made by:  18 Aditya Borkar, 17 Sneha Biyala, 19 Hitanshu Budhdev, 20 Durgesh Chaudhari  ", font="Times 15")
    acc.place(relx= 0.5, rely = 0.9, anchor=CENTER)

    C.pack()
    root.mainloop()
if __name__ == "__main__":
    mainscreen()

