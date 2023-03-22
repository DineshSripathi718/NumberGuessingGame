# Import required libraries
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random as r

# Create an instance of tkinter window
win = Tk()
win.title("Number Guessing Game")

# Define the geometry of the window
win.geometry("1000x400")
frame = Frame(win, width=700, height=500)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#Menu Bar


# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("D:/java_programs/python/NumberGuessingGame/assests/NGG.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
name_var = StringVar()
Score = 0
Value = 0

def StartGame():
    global img, name_var
    sub = Toplevel()
    sub.title("Start Game")

    sub.geometry("700x400")
    frame1 = Frame(sub, width=700, height=400)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.5)
    img = ImageTk.PhotoImage(Image.open("D:/java_programs/python/NumberGuessingGame/assests/white.jpg"))

# Create a Label Widget to display the text or Image
    label = Label(frame1, image = img)
    label.pack()
       
    Name = Entry(sub, textvariable = name_var).pack()

    def save_entry():
        name = name_var.get()
        Name_Label = Label(sub, text = "Hi !"+ name_var.get()).pack()
        print(name)

        Diff_Label = Label(sub, text = "Hi !"+ name_var.get()+", Select your game difficulty level").pack()
        name_var.set("")
        STAGE = [("Easy","Beginer"),
             ("Medium","intermediate"),
             ("Hard","Advanced")]
    
        U_Stage = StringVar()
        U_Stage.set("")
        # Str_Stage = StringVar()
        # Str_Stage.set("Default")
        U_num = IntVar()
        U_num.set(0)

        for text , lvl in STAGE :
            Radiobutton(sub, 
                        text = text, 
                        variable = U_Stage,
                        value=lvl).pack()

        def RadioEntry(STR_value):
            global Value
            Value = 5 if STR_value.lower() == "beginer" else 3 if STR_value.lower() == "intermediate" else 1

            print(Value)
            Noti = Label(sub, text = "Guess a number").pack()
            
            global Score
            # print("IN while loop")


            def Check(U_value):

                global Score
                global Value 
                Dis = Label(sub, text = "You have "+str(Value)+" chances").pack()
               
                Score_Noti = Label(sub, text = "Your score is "+str(Score)).pack()

                if Value > 0:
                    # print(Value)
                    if U_value == r.randint(1,10):
                        Score += 1 if STR_value.lower() == "beginer" else 3 if STR_value.lower() == "intermediate" else 5
                        # print('Correct Guess \n your score : ',Score)

                        Correct_Noti = Label(sub, text = "Correct Guess").pack()

                    else:
                        Value -= 1
                        # print(Value)
                        # print('Wrong Guess \n you had ' ,Value, " choices")
                        wrong_Noti = Label(sub, text = "Wrong Guess").pack()
                else:
                    res = messagebox.askretrycancel("GameOver!", "Try again?")
                    if res == 'yes':
                       messagebox.showinfo('Response', 'Thanks for playing the game')
                    else:
                        StartGame()

            U_Num = Entry(sub, textvariable = U_num).pack()
            check = Button(sub, text = "Check", command = lambda : Check(U_num.get())).pack()


        EntryButton = Button(sub, 
                         text = "Select",
                         command = lambda: RadioEntry(U_Stage.get())).pack()

        
    Entry_Button = Button(sub, text = "Enter", width=10, command=save_entry).pack()
    
    

     #menu bar secound window
    menu = Menu(sub)
    item = Menu(menu)
    item.add_command(label='yes', command = sub.destroy)
    item.add_command(label='No')
    menu.add_cascade(label='Exit', menu=item)
    sub.config(menu=menu)
    

start_Button = Button(win, text = "Enter", width=10, command=StartGame).pack()
Exit_Button = Button(win, text = "Exit", width=10, command= win.quit).pack()

menu = Menu(win)
item = Menu(menu)
item.add_command(label='Start Game',command=StartGame)
item.add_command(label='stop Game', command = win.quit)
menu.add_cascade(label='File', menu=item)
win.config(menu=menu)

mainloop()