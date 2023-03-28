from tkinter import messagebox
import tkinter
from tkinter import *
import time
import datetime
import mysql.connector
from PIL import Image, ImageTk
from tkinter import ttk

win = tkinter.Tk()
win.title("Farmer_bot")
win.configure()
win.geometry("1400x700")
win.resizable(False, False)
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Cg_045104", database="mypy")
mycursor = mydb.cursor()

ima2 = Image.open("banjar3.jpg")
tkimg2 = ImageTk.PhotoImage(ima2)

lal3 = Label(win, image=tkimg2)
lal3.pack()


def greet(user):

    andro = ""

    my_time = datetime.datetime.now()
    k = my_time.hour

    if (user == "Hello" or user == "Hi" or user == "Hii") or "andro" in user:
        time.sleep(1)
        andro = "Hello"
    elif user == "Hey" or user == "Hey andro":
        time.sleep(1)
        andro = "Hii"
    elif user == "Good morning" and 3 < k < 12:
        time.sleep(1)
        andro = "Very good morning"
    elif user == "Good afternoon" and 11 < k < 17:
        time.sleep(1)
        andro = "Good afternoon"
    elif user == "Good evening" and (16 < k or k < 3 or 3 < k > 16):
        time.sleep(1)
        andro = "Good evening"
    elif user == "Good night" and (20 < k or k < 3 or 3 < k > 20):
        time.sleep(1)
        andro = "Good night"
    elif user == "Good morning" and (not 3 < k < 12):
        time.sleep(1)
        andro = "It's not morning"
    elif user == "Good afternoon" and (not 11 < k < 17):
        time.sleep(1)
        andro = "It's not afternoon"
    elif user == "Good evening" and (not (16 < k or k < 3 or 3 < k > 16)):
        time.sleep(1)
        andro = "It's not evening"
    elif user == "Good night" and (not (20 < k or k < 3 or 3 < k > 20)):
        time.sleep(2)
        andro = "It's not night"

    return andro


def Questions(user, name2):

    andro = ""

    if user == "What is your name ?":
        time.sleep(1)
        andro = "My name is Andro."
    elif user == "Who are you ?":
        time.sleep(1)
        andro = "I'm a Farmer."
    elif user == "Do you know me ?":
        time.sleep(1)
        andro = "Yes, You are " + name2
    elif user == "Who am i ?":
        time.sleep(1)
        andro = "You are " + name2
    elif user == "How are you ?":
        time.sleep(1)
        andro = "I'm good"
    elif user == "What is use of acemain fertilizer ?" or "acemain" in user:
        andro = "ACEMAIN is a broad spectrum systemic organophosphate insecticide.\n" \
                "               ACEMAIN controls a wide range of chewing and sucking insects.\n"

        lal.config(image=tkimg10)
        lal.pack()
    elif user == "What is use of argon fertilizer ?" or "argon" in user:
        andro = "In modern plant organ fertiliser is produced from natural gas.\n" \
                "               In several transformation step natural gas and Mithen is created by combination\n" \
                "               with argon from the air to form nitrogen's fertiliser."

        lal.config(image=tkimg11)
        lal.pack()
    elif user == "What is use of fatal fertilizer ?" or "fatal" in user:
        andro = "It kills brown and red plant hopper (insects) which sucks elements of plant. "
        lal.config(image=tkimg12)
        lal.pack()
    elif user == "What is use of zinatra700 fertilizer ?" or "zinatra700" in user:
        andro = "It fills the requirement of zinc element in the plant."
        lal.config(image=tkimg13)
        lal.pack()
    elif user == "What is use of bipimain fertilizer ?" or "bipimain" in user:
        andro = "It kills brown and red plant hopper (insects) which sucks elements of plant."
        lal.config(image=tkimg14)
        lal.pack()
    elif user == "What is use of savera fertilizer ?" or "savera" in user:
        andro = "It kills brown and red plant hopper (insects) which sucks elements of plant. "
        lal.config(image=tkimg15)
        lal.pack()
    elif user == "What is use of hamla500 fertilizer ?" or "hamla500" in user:
        andro = "It kills chewing insects in plant."
        lal.config(image=tkimg16)
        lal.pack()
    elif user == "What is use of saaf fertilizer ?" or "saaf" in user:
        andro = "It manages the problem of brown spot in the plant."
        lal.config(image=tkimg19)
        lal.pack()
    elif user == "Who is your father ?":
        time.sleep(2)
        andro = "I'm a bot, created by Mr.Anurag Yadu, So he is my father."

    return andro


def main_f(use):

    an = ""

    if greet(use):
        an = greet(use)
    elif Questions(use, name1):
        an = Questions(use, name1)
    elif use == "I'm good":
        time.sleep(1)
        an = "Nice"
    elif use == "Show me fertilizer":
        print(1)
    elif use == "Show me my image":
        an = "Ok"
        time.sleep(1)
        lal.config(image=tkimg)
        lal.pack()
    elif use == "Show me ben 10":
        an = "Ok"
        time.sleep(1)
        lal.config(image=tkimg4)
        lal.pack()
    elif use == "Spontaneous plants":
        an = "Nominee gold is best chemical fertilizer to resolve spontaneous plants issue\n"
        lal.config(image=tkimg3)
        lal.pack()
    elif use == "Insects, which eat leaves":
        an = "'Barood' and 'Disect' are the fertilizers that deals with the problem of insects\n" \
             "               which eat crops.\n"
        lal.config(image=tkimg5)
        lal.pack()
    elif use == "Insects, which sucks purities of plant":
        an = "'Simbaa' fertilizer kills sucker insects in plant, 'Acemain' fertilizer is an alternative\n " \
             "               of 'Simbaa'.\n"
        lal.config(image=tkimg6)
        lal.pack()
    elif use == "Low growth rate of plant":
        an = "Sometimes it happens that the crops don't get their minerals completely.Root rise\n" \
             "               fulfill the requirement of the minerals of plant and raise the growth rate of plant.\n"
        lal.config(image=tkimg7)
        lal.pack()
    elif use == "Low fertility rate of soil":
        an = "'Uria', D.A.P and 'Potas fulfill the required nitrogen and other elements of soil\n" \
             "               which helps to grow the fertility rate of soil.\n"
        lal.config(image=tkimg8)
        lal.pack()
    elif use == "Blast disease in plant":
        an = "Trust fertilizer which has 75% of Tricyclazole chemical on it manage the problem\n" \
             "               of blast disease."
        lal.config(image=tkimg17)
        lal.pack()
    elif use == "Brown spot in plant":
        an = "Prozole fertilizer manage the problem of brown spot in plant.\n" \
             "                'Saaf' fertilizer is an alternative of it."
        lal.config(image=tkimg18)
        lal.pack()
    elif use == "False smut disease in plant":
        an = "Nector fertilizer manage the disease of false smut in plant."
        lal.config(image=tkimg20)
        lal.pack()
    elif use == "Cls":
        an = "Cls"
    elif use == "I want to place an order" or use == "I want to buy a fertilizer":
        an = "Ok, Enter details to place order."
        NW2()
    elif "price" in use or "rate" in use:
        an = "For any price related query, you can contact to owmer of Yadu Krishi Kendra\n" \
             "               Contact number - +918839747800\n" \
             "               Address - Village Matka, Bemetara, Chhattisgarh\n"
    elif use == "Bye":
        time.sleep(1)
        an = "Bye"
    elif use == "Show order list - ,78329":
        an = "Ok sir."
        order_list()
    else:
        if " ?" in use:
            time.sleep(1)
            an = "I don't know."
        elif use == "":
            an = ""
        else:
            time.sleep(2)
            an = "Sorry, I couldn't understand."

    return an


name1 = "Anurag yadu"
gol = 0
ent = StringVar()
ent.set("Write here")
z = 0


def order_list():
    win3 = Toplevel(win)
    win3.title("Order_list")
    win3.resizable(False, False)

    count = 0
    table = ttk.Treeview(win3, columns=('', '', '', '', ''))

    table.heading('#0', text='Order_number')
    table.heading('#1', text='Full_name')
    table.heading('#2', text='Mobile_number')
    table.heading('#3', text='Address')
    table.heading('#4', text='Product')
    table.heading('#5', text='P.amount')

    table.column('#1', anchor='center')
    table.column('#2', anchor='center')
    table.column('#3', anchor='center')
    table.column('#4', anchor='center')
    table.column('#5', anchor='center')

    mycursor.execute("select*from order_l")
    for i in mycursor:
        count = count + 1
        count = str(count)
        table.insert('', 'end', text="Order_" + count, values=(i[0], i[1], i[2], i[3], i[4]))
        count = int(count)

    table.pack()


def ki():
    tet = ent.get()
    ent.set("")

    if tet:
        ten.configure(state="normal")
        ten.insert(END, "You:  " + tet + "\n")
    else:
        messagebox.showerror("Error", "Blank input does not allow.")

    ans = main_f(tet.capitalize())

    if ans == "Bye" or ans == "Good night":
        win.destroy()
    elif ans == "Cls":
        ten.delete("13.0", END)
        ten.insert("12.0", "\n")
    else:
        ten.insert(END, "Andro:  " + ans + "\n\n")

    ten.configure(state="disabled")


def NW2():
    win2 = Toplevel(win)
    win2.title("Product_Order")
    win2.geometry("770x730")
    win2.resizable(False, False)
    win2.configure(bg="cyan")

    ent1 = StringVar()
    ent2 = StringVar()
    ent3 = StringVar()
    ent4 = StringVar()
    ent5 = StringVar()

    def submit1():
        aa1 = ent1.get()
        aa2 = ent2.get()
        aa3 = ent3.get()
        aa4 = ent4.get()
        aa5 = ent5.get()

        if aa1 and aa2 and aa3 and aa4 and aa5:
            ent1.set("")
            ent2.set("")
            ent3.set("")
            ent4.set("")
            ent5.set("")

            lid = (aa1, aa2, aa3, aa4, aa5)
            mycursor.execute("insert into order_l values(%s, %s, %s, %s, %s)", lid)
            mydb.commit()
            messagebox.showinfo("Submitted", "Your details submitted successfully.")
            win2.destroy()
        else:
            messagebox.showerror("Error", "Missing something. Blank entry does not allow, Fill all entries")

    lab3 = Label(win2, text="Enter full name", bg="Lightblue", fg="black")
    lab3.config(width=25, height=1, font=("Calibri", 11))
    lab4 = Label(win2, text="Enter mobile number", bg="Lightblue", fg="black")
    lab4.config(width=25, height=1, font=("Calibri", 11))
    lab5 = Label(win2, text="Enter address", bg="Lightblue", fg="black")
    lab5.config(width=25, height=1, font=("Calibri", 11))
    lab6 = Label(win2, text="Enter product name", bg="Lightblue", fg="black")
    lab6.config(width=25, height=1, font=("Calibri", 11))
    lab7 = Label(win2, text="Enter product amount", bg="Lightblue", fg="black")
    lab7.config(width=25, height=1, font=("Calibri", 11))
    labm = Label(win2, text="Order Details", font=("Times new roman", 20), bg="Navy", fg="white")
    labm.config(width=100, justify="center")

    en1 = Entry(win2, textvariable=ent1, bd=2, bg="mistyrose", foreground="black")
    en1.configure(width=31, font=("Helventica", 12), )
    en2 = Entry(win2, textvariable=ent2, bd=2, bg="mistyrose", foreground="black")
    en2.configure(width=31, font=("Helventica", 12), )
    en3 = Entry(win2, textvariable=ent3, bd=2, bg="mistyrose", foreground="black")
    en3.configure(width=31, font=("Helventica", 12), )
    en4 = Entry(win2, textvariable=ent4, bd=2, bg="mistyrose", foreground="black")
    en4.configure(width=31, font=("Helventica", 12), )
    en5 = Entry(win2, textvariable=ent5, bd=2, bg="mistyrose", foreground="black")
    en5.configure(width=31, font=("Helventica", 12), )

    bt2 = Button(win2, text="Submit", bg="Orchid", fg="black", font=("Arial", 11), command=submit1)
    bt2.config(width=13)

    labm.pack()

    lab3.place(x="285", y="80")
    en1.place(x="245", y="120")
    lab4.place(x="285", y="180")
    en2.place(x="245", y="220")
    lab5.place(x="285", y="280")
    en3.place(x="245", y="320")
    lab6.place(x="285", y="380")
    en4.place(x="245", y="420")
    lab7.place(x="285", y="480")
    en5.place(x="245", y="520")

    bt2.place(x="320", y="600")


lin1 = "You can ask me farming related problems and I'll suggest you fertilizers.\n\n"
lin2 = "Problems in crops are like - \n"
pobm1 = "Spontaneous plants\n"
pobm2 = "Insects, which eat leaves\n"
pobm3 = "Insects, which sucks purities of plant\n"
pobm4 = "Low growth rate of plant\n"
pobm5 = "Low fertility rate of soil\n\n"
lin3 = "Which problem do you have on your crops ?\n"
lin4 = "Write below and Send.\n\n"
b = "* "

img = Image.open("anu1c.jpg")
tkimg = ImageTk.PhotoImage(img)

img4 = Image.open("images-48.jpg")
tkimg4 = ImageTk.PhotoImage(img4)

img3 = Image.open("ng.jpg")
tkimg3 = ImageTk.PhotoImage(img3)

img5 = Image.open("fe1.jpg")
tkimg5 = ImageTk.PhotoImage(img5)

img6 = Image.open("simba.jpg")
tkimg6 = ImageTk.PhotoImage(img6)

img7 = Image.open("grof.jpg")
tkimg7 = ImageTk.PhotoImage(img7)

img8 = Image.open("hqdefault.jpg")
tkimg8 = ImageTk.PhotoImage(img8)

img9 = Image.open("068.jpg")
tkimg9 = ImageTk.PhotoImage(img9)

img10 = Image.open("acimen.jpg")
tkimg10 = ImageTk.PhotoImage(img10)

img11 = Image.open("argon.jpg")
tkimg11 = ImageTk.PhotoImage(img11)

img12 = Image.open("Fatal.jpg")
tkimg12 = ImageTk.PhotoImage(img12)

img13 = Image.open("zinatra700.jpg")
tkimg13 = ImageTk.PhotoImage(img13)

img14 = Image.open("bipiman.jpg")
tkimg14 = ImageTk.PhotoImage(img14)

img15 = Image.open("zinatra700.jpg")
tkimg15 = ImageTk.PhotoImage(img15)

img16 = Image.open("Hamla550.jpg")
tkimg16 = ImageTk.PhotoImage(img16)

img17 = Image.open("Thrust.jpg")
tkimg17 = ImageTk.PhotoImage(img17)

img18 = Image.open("Prozol.jpg")
tkimg18 = ImageTk.PhotoImage(img18)

img19 = Image.open("Saaf.jpg")
tkimg19 = ImageTk.PhotoImage(img19)

img20 = Image.open("nector.jpg")
tkimg20 = ImageTk.PhotoImage(img20)

img21 = Image.open("advance.jpg")
tkimg21 = ImageTk.PhotoImage(img21)

fr = Frame(win, width=300, height=300)
fr.place(x="800", y="130")

lal = Label(fr, image=tkimg)

lal2 = Label(win, text="Yadu Fertilizers", bg="blue", fg="White", font=("Times", 25))
lal2.configure(width=80, justify="center")
lal2.place(x="0", y="0")

btn = Button(text="Send", bg="Navyblue", foreground="white", height="2", width="10", command=ki)
btn.configure(activebackground="green yellow")
btn.place(x="620", y="570")

ten = Text(win, state="disabled", bg="lawn green", fg="black", bd=10)
ten.configure(font=("Calibri", 13), width=70, height=20, state="normal")
ten.insert(END, lin1 + lin2 + b + pobm1 + b + pobm2 + b + pobm3 + b + pobm4 + b + pobm5 + lin3 + lin4)
ten.configure(state="disabled")
ten.place(x="120", y="100")

en = Entry(win, textvariable=ent, bd=2, bg="green yellow", foreground="black")
en.configure(width=38, font=("Helventica", 15),)
en.place(x="195", y="580")


win.mainloop()
