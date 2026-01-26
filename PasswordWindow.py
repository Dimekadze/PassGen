from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Scale
import customtkinter as ctk # pyright: ignore[reportMissingImports]
import secrets as sc
import string
import pyperclip

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.BlackColor = '#000000'
        self.GreyColor="#2A2A2A"
        self.OrangeColor = "#E9560C"

        APP_WIDTH = 1100
        APP_HEIGHT = 550

        FRAME_WIDTH = 250
        FRAME_HEIGHT = 350

        PADX = 10
        PADY = 10

        BUTTON_WIDTH = 40
        BUTTON_HEIGHT = 40

        screen_x = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x = (screen_x // 2) - (APP_WIDTH // 2)
        y = (screen_y // 2) - (APP_HEIGHT // 2)

        self.title('Password Generator') 
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x+800}+{y}') 
        self.resizable(False, False)
        self.configure(fg_color=self.OrangeColor)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

        self.include_numbers = ctk.BooleanVar(value=True)
        self.include_symbols = ctk.BooleanVar(value=False)
        self.include_upper = ctk.BooleanVar(value=False)
        self.include_lower = ctk.BooleanVar(value=False)


        self.BigFont = ("Verdana", 30)
        self.MediumFont = ("Verdana", 25)
        self.SmallFont = ("Verdana", 20)


        self.options_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=15)
        self.options_frame.grid_propagate(False)

        self.length_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=15)
        self.length_frame.grid_propagate(False)
        self.password_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=15)
        self.password_frame.grid_propagate(False)


        self.options_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky='w')
        self.length_frame.grid(row=0, column=1, padx=PADX, pady=PADY, sticky='w')
        self.password_frame.grid(row=0, column=2, padx=PADX, pady=PADY, sticky='w')

        # for frame in [self.options_frame, self.length_frame, self.password_frame]:
        #     frame.grid_rowconfigure(0, weight=1)  # верхний отступ
        #     frame.grid_rowconfigure(5, weight=1)  # нижний отступ
        #     frame.grid_columnconfigure(0, weight=1)  # левый отступ
        #     frame.grid_columnconfigure(2, weight=1)  # правый отступ

        # функции
        def HelpButton():
            showinfo(title="HelpButton", message="Это простейший генератор паролей, какая тут нужна помощь, кусок ты валенка?")

        def CopyButton():
            password = self.Label_Password.cget("text")
            if password != "----------------":
                pyperclip.copy(password)
                showinfo(title="CopyButton", message="Сopied to clipboard")
            else:
                showinfo(title="CopyButton", message="Try to generate a password")

        def ClearButton():
            showinfo(title="ClearButton", message="Cleared")

        def LengthUpdate(var):
            self.Label_Curr_Value.configure(text=str(int(self.Scale_Length.get())))

        def PlusButton():
            length = int(self.Label_Curr_Value.get())
            if length > 99:
                showinfo(title=MinusButton, message="Password length can't be more than 100")
            else:
                self.Label_Curr_Value.delete(0, '8')
                return self.Label_Curr_Value.insert(0, str(length+1))

        def MinusButton():
            length = int(self.Label_Curr_Value.get())
            if length < 2:
                showinfo(title=MinusButton, message="Password length can't be less than zero")
            else:
                self.Label_Curr_Value.delete(0, '8')
                length -= 1
                return self.Label_Curr_Value.insert(0, length)

        def GenerateButton():
            length = int(self.Label_Curr_Value.get())

            use_numbers = self.include_numbers.get()
            use_symbols = self.include_symbols.get()
            use_upper = self.include_upper.get()
            use_lower = self.include_lower.get()

            password = PassGenFunc(length, use_numbers, use_symbols, use_upper, use_lower)
            self.Label_Password.configure(text=password)

        def PassGenFunc(length, use_numbers=True, use_symbols=True, use_upper=True, use_lower=True):
            all_in_one = ''

            if use_numbers:
                all_in_one += string.digits
            if use_symbols:
                all_in_one += string.punctuation
            if use_upper:
                all_in_one += string.ascii_uppercase
            if use_lower:
                all_in_one += string.ascii_lowercase

            random_password = ''.join(sc.choice(all_in_one) for i in range(length))
            
            return random_password






        self.Label_Options = ctk.CTkLabel(self.options_frame, text="Options", font=self.BigFont)
        self.Label_Options.grid(row=0, column=0)

        # чекбоксы
        self.Checkbutton_1 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Numbers', 
                                             variable=self.include_numbers, 
                                             state='disabled',
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_1.grid(row=1, column=0, sticky="w")

        self.Checkbutton_2 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Symbols', 
                                             variable=self.include_symbols,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_2.grid(row=2, column=0, sticky="w")
        
        self.Checkbutton_3 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Upper Letters', 
                                             variable=self.include_upper,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_3.grid(row=3, column=0, sticky="w")
        
        self.Checkbutton_4 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Lower Letters', 
                                             variable=self.include_lower,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_4.grid(row=4, column=0, sticky="w")
        




        # длина пароля
        # self.options_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsw')
        self.Label_Length = ctk.CTkLabel(self.length_frame, text="Length", font=self.BigFont)
        self.Label_Length.grid(row=0, column=2)

        # self.Scale_Length = ctk.CTkSlider(self.length_frame, 
        #                                   from_=8, 
        #                                   to=25, 
        #                                   command=LengthUpdate,
        #                                   progress_color=self.BlackColor,
        #                                   button_color=self.GreyColor)
        # self.Scale_Length.set(8)
        # self.Scale_Length.grid(row=1, column=1, padx=20, pady=20)

        self.Button_Plus = ctk.CTkButton(self.length_frame, 
                                         text="+", 
                                         width=BUTTON_WIDTH,
                                         fg_color=self.BlackColor,
                                         hover_color=self.GreyColor,
                                         command=PlusButton)
        self.Button_Plus.grid(row=2, column=3)

        self.Button_Minus = ctk.CTkButton(self.length_frame, 
                                          text="-", 
                                          width=BUTTON_WIDTH,
                                          fg_color=self.BlackColor,
                                          hover_color=self.GreyColor,
                                          command=MinusButton)
        self.Button_Minus.grid(row=2, column=1)

        self.Label_Curr_Value = ctk.CTkEntry(self.length_frame, 
                                             placeholder_text="8", 
                                             font=self.MediumFont,
                                             justify="center")
        self.Label_Curr_Value.insert(0, '8')
        self.Label_Curr_Value.grid(row=2, column=2)

        self.Button_Curr_Value = ctk.CTkButton(self.length_frame, text="Clear", 
                                          command=ClearButton, 
                                          fg_color=self.BlackColor, 
                                          hover_color=self.GreyColor,
                                          font=self.MediumFont)
        self.Button_Curr_Value.grid(row=3, column=2)
        
        # HelpButton
        self.Button_Help = ctk.CTkButton(self.length_frame, text="Help", 
                                    command=HelpButton, 
                                    fg_color=self.BlackColor, 
                                    hover_color=self.GreyColor,
                                    font=self.MediumFont)
        self.Button_Help.grid(row=4, column=2)









        # Generate Password
        self.Label_Your_Pass = ctk.CTkLabel(self.password_frame, text="Your Password", font=self.BigFont)
        self.Label_Your_Pass.grid(row=0, column=4)

        self.Button_Generate = ctk.CTkButton(self.password_frame, text="Generate Password", 
                                        command=GenerateButton, 
                                        fg_color=self.BlackColor, 
                                        hover_color=self.GreyColor, 
                                        font=self.MediumFont)
        self.Button_Generate.grid(row=1, column=4)

        self.Label_Password = ctk.CTkLabel(self.password_frame, text="----------------", font=self.MediumFont)
        self.Label_Password.grid(row=2, column=4)

        # Copy
        self.Button_Copy = ctk.CTkButton(self.password_frame, text="Copy", 
                                    command=CopyButton, 
                                    fg_color=self.BlackColor, 
                                    hover_color=self.GreyColor,
                                    font=self.MediumFont)
        self.Button_Copy.grid(row=3, column=4)

# окошечко
APP = AppWindow()
APP.mainloop()