from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Scale
import customtkinter as ctk

# Functions
def help():
    showinfo(title="Help", message="Это простейший генератор паролей, какая тут нужна помощь, кусок ты валенка?")

def length(g):
    value = Scale_Length.get()
    Label_Curr_Value["text"] = Scale_Length.get()
    return value

# Main Frame
MainFrame = Tk()

screen_x = MainFrame.winfo_screenwidth()
screen_y = MainFrame.winfo_screenheight()
MainFrame_x = 440
MainFrame_y = 310
x = (screen_x // 2) - (MainFrame_x // 2)
y = (screen_y // 2) - (MainFrame_y // 2)

MainFrame.title('Password generator') 
MainFrame.geometry(f'{MainFrame_x}x{MainFrame_y}+{x}+{y}') 
MainFrame.resizable(False, False)
MainFrame.attributes("-toolwindow", True)

# Options and Checkbuttons
Label_Options = ttk.Label(text="Password Generator by Dimekadze", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 16")
Label_Options.place(x=10, y=10, height=40, width=420)
# отступ от краев - 10
# отступ между виджетами - 10
Label_Options = ttk.Label(text="Options", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 16")
Label_Options.place(x=10, y=60, height=40, width=160)

Label_Symbols = ttk.Label(text="Symbols", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Symbols.place(x=50, y=110, height=40, width=120)

Label_Up_Letters = ttk.Label(text="Upper Letters", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Up_Letters.place(x=50, y=160, height=40, width=120)

Label_Low_Letters = ttk.Label(text="Lower Letters", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Low_Letters.place(x=50, y=210, height=40, width=120)

Label_Numbers = ttk.Label(text="Numbers", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Numbers.place(x=50, y=260, height=40, width=120)

Checkbutton_1 = ttk.Checkbutton().place(x=20, y=120)
Checkbutton_2 = ttk.Checkbutton().place(x=20, y=170)
Checkbutton_3 = ttk.Checkbutton().place(x=20, y=220)
Checkbutton_4 = ttk.Checkbutton().place(x=20, y=270)

# Length
Label_Length = ttk.Label(text="Length", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 16")
Label_Length.place(x=180, y=60, height=40, width=120)

Scale_Length = Scale(orient=HORIZONTAL, from_=8, to=25, command=length, font="Arial 10", showvalue=0)
Scale_Length.place(x=180, y=120, height=40, width=120)

Label_Curr_Value = ttk.Label(text="", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 16")
Label_Curr_Value.place(x=180, y=160, height=40, width=120)

# Accept 
Button_Accept = ttk.Button(text="Accept")
Button_Accept.place(x=180, y=210, height=40, width=120)

# Reset
Button_Clear = ttk.Button(text="Reset").place(x=180, y=260, height=40, width=120)

# Generate Password
Button_Generate = ttk.Button(text="Generate Password")
Button_Generate.place(x=310, y=60, height=40, width=120)

Label_Your_Pass = ttk.Label(text="Your Password", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Your_Pass.place(x=310, y=110, height=40, width=120)

Label_Password = ttk.Label(text="---------------", borderwidth=1, relief=SOLID, anchor=CENTER, font="Arial 12")
Label_Password.place(x=310, y=160, height=40, width=120)

# Copy
Button_Copy = ttk.Button(text="Copy")
Button_Copy.place(x=310, y=210, height=40, width=120)

# Help
Button_Help = ttk.Button(text="Help", command=help).place(x=310, y=260, height=40, width=120)

MainFrame.mainloop()
