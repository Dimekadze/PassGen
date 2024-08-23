from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import customtkinter as ctk
from tkinter import font

# Main Frame
MainFrame = Tk()

screen_x = MainFrame.winfo_screenwidth()
screen_y = MainFrame.winfo_screenheight()
MainFrame_x = 900
MainFrame_y = 400
x = (screen_x // 2) - (MainFrame_x // 2)
y = (screen_y // 2) - (MainFrame_y // 2)

MainFrame.title('Password generator') 
MainFrame.geometry(f'{MainFrame_x}x{MainFrame_y}+{x}+{y}') 
#MainFrame.resizable(False, False)
#MainFrame.attributes("-toolwindow", True)

# Functions
def help():
    showinfo(title="Help", message="Это простейший генератор паролей, какая тут нужна помощь, кусок ты валенка?")

# App Name
label_Name = ttk.Label(text="Password Generator by Dimekadze", font="Arial", borderwidth=1, relief=SOLID, padding=5)
label_Name.grid(row=0)

# Additional Frames
Frame_Options = ttk.Frame(borderwidth=1, relief=SOLID).grid(row=1, column=0, columnspan=2)
#Frame_Length = ttk.Frame(borderwidth=2, relief=SOLID, padding=5).grid(row=0, column=2)
#Frame_Password = ttk.Frame(borderwidth=2, relief=SOLID, padding=5).grid(row=0, column=3, columnspan=2)
#Frame_Clear = ttk.Frame(borderwidth=2, relief=SOLID, padding=5).grid(row=0, column=5)

# Options and Chechbuttons
Label_Options = ttk.Label(text="Options", borderwidth=1, relief=SOLID, padding=5, font=("Arial 16"))
Label_Options.grid(row=1, column=0, columnspan=2)

Label_Symbols = ttk.Label(text="Symbols", borderwidth=1, relief=SOLID, padding=5, font=("Arial 14"))
Label_Symbols.grid(row=2, column=1)

Label_Up_Letters = ttk.Label(Frame_Options, text="Upper Letters", borderwidth=1, relief=SOLID, padding=5, font=("Arial 14"))
Label_Up_Letters.grid(row=3, column=1)

Label_Low_Letters = ttk.Label(Frame_Options, text="Lower Letters", borderwidth=1, relief=SOLID, padding=5, font=("Arial 14"))
Label_Low_Letters.grid(row=4, column=1)

Label_Numbers = ttk.Label(Frame_Options, text="Numbers", borderwidth=1, relief=SOLID, padding=5, font=("Arial 14"))
Label_Numbers.grid(row=5, column=1)

Checkbutton_1 = ttk.Checkbutton(Frame_Options)
Checkbutton_1.grid(row=2, column=0)

Checkbutton_2 = ttk.Checkbutton(Frame_Options)
Checkbutton_2.grid(row=3, column=0)

Checkbutton_3 = ttk.Checkbutton(Frame_Options)
Checkbutton_3.grid(row=4, column=0)

Checkbutton_4 = ttk.Checkbutton(Frame_Options)
Checkbutton_4.grid(row=5, column=0)


'''
# Length
Label_Length = ttk.Label(master=Frame_Length, text="Length")
Label_Length.grid(row=0, column=1)

Scale_Length = ttk.Scale(master=Frame_Length)
Scale_Length.grid(row=1, column=1)

Label_Curr_Value = ttk.Label(master=Frame_Length, text="1...25")
Label_Curr_Value.grid(row=2, column=1)

# Clear
Button_Clear = ttk.Button(master=Frame_Clear, text="Clear All")
Button_Clear.grid(row=3, column=1)

# Generate
Button_Generate = ttk.Button(master=Frame_Password, text="Generate Password")
Button_Generate.grid(row=0, column=2)

Label_Your_Pass = ttk.Label(master=Frame_Password, text="Your Password")
Label_Your_Pass.grid(row=1, column=2)

Label_Password = ttk.Label(master=Frame_Password, text="---------------")
Label_Password.grid(row=2, column=2)

Button_Copy = ttk.Button(master=Frame_Password, text="Copy")
Button_Copy.grid(row=3, column=2)

# Help Button
Button_Help = ttk.Button(text="Help", command=help)
Button_Help.grid(row=0, column=3)
'''



MainFrame.mainloop()

