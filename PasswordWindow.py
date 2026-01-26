from tkinter.messagebox import showinfo
import customtkinter as ctk
import secrets as sc
import string
import pyperclip

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # variables
        self.BlackColor = '#000000'
        self.GreyColor="#393939"
        self.OrangeColor = "#E9560C"
        self.WhiteColor = "#FFFFFF"

        APP_WIDTH = 900
        APP_HEIGHT = 350

        FRAME_WIDTH = 270
        FRAME_HEIGHT = 320

        VAL10 = 10
        VAL15 = 15
        VAL20 = 20
        VAL30 = 30
        VAL40 = 40
        VAL50 = 50
        VAL100 = 100

        # window size
        screen_x = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        x = (screen_x // 2) - (APP_WIDTH // 2)
        y = (screen_y // 2) - (APP_HEIGHT // 2)

        self.title('Password Generator') 
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}') 
        self.resizable(False, False)
        self.configure(fg_color=self.OrangeColor)

        self.include_numbers = ctk.BooleanVar(value=True)
        self.include_symbols = ctk.BooleanVar(value=False)
        self.include_upper = ctk.BooleanVar(value=False)
        self.include_lower = ctk.BooleanVar(value=False)

        # font size
        self.BigFont = ("Verdana", 30)
        self.MediumFont = ("Verdana", 25)
        self.SmallFont = ("Verdana", 20)

        # frames
        self.options_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.options_frame.grid_propagate(False)

        self.length_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.length_frame.grid_propagate(False)
        self.password_frame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.password_frame.grid_propagate(False)

        # frames placing
        self.options_frame.grid(row=0, column=0, padx=(VAL20, 0))
        self.length_frame.grid(row=0, column=1, padx=(VAL20, VAL20))
        self.password_frame.grid(row=0, column=2, padx=(0, VAL20))

        # frames configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.options_frame.grid_columnconfigure(0, weight=1)
        self.options_frame.grid_rowconfigure(0, weight=1)
        self.options_frame.grid_rowconfigure(1, weight=1)
        self.options_frame.grid_rowconfigure(2, weight=1)
        self.options_frame.grid_rowconfigure(3, weight=1)
        self.options_frame.grid_rowconfigure(4, weight=1)
        self.options_frame.grid_rowconfigure(5, weight=1)

        self.length_frame.grid_columnconfigure(0, weight=1)
        self.length_frame.grid_columnconfigure(1, weight=1)
        self.length_frame.grid_columnconfigure(2, weight=1)
        self.length_frame.grid_columnconfigure(3, weight=1)
        self.length_frame.grid_columnconfigure(4, weight=1)
        self.length_frame.grid_rowconfigure(0, weight=1)
        self.length_frame.grid_rowconfigure(1, weight=1)
        self.length_frame.grid_rowconfigure(2, weight=1)
        self.length_frame.grid_rowconfigure(3, weight=1)
        self.length_frame.grid_rowconfigure(4, weight=1)
        self.length_frame.grid_rowconfigure(5, weight=1)

        self.password_frame.grid_columnconfigure(0, weight=1)
        self.password_frame.grid_columnconfigure(1, weight=1)
        self.password_frame.grid_columnconfigure(2, weight=1)
        self.password_frame.grid_columnconfigure(3, weight=1)
        self.password_frame.grid_columnconfigure(4, weight=1)
        self.password_frame.grid_rowconfigure(0, weight=1)
        self.password_frame.grid_rowconfigure(1, weight=1)
        self.password_frame.grid_rowconfigure(2, weight=1)
        self.password_frame.grid_rowconfigure(3, weight=1)



        # functions
        def HelpButton():
            showinfo(title="HelpButton", message="This is a simple password generator, what kind of help do you need here, you piece of felt boots?")

        def CopyButton():
            password = self.Label_Password.cget("text")
            if password != "----------------":
                pyperclip.copy(password)
                showinfo(title="CopyButton", message="Сopied to clipboard")
            else:
                showinfo(title="CopyButton", message="Try to generate a password")

        def ClearButton():
            self.Checkbutton_2.deselect()
            self.Checkbutton_3.deselect()
            self.Checkbutton_4.deselect()
            self.Label_Curr_Value.delete(0, '8')
            self.Label_Curr_Value.insert(0, '8')

            showinfo(title="ClearButton", message="Cleared")

        def PlusButton():
            length = int(self.Label_Curr_Value.get())
            if length >= 100:
                showinfo(title=MinusButton, message="Password length can't be more than 100")
            else:
                self.Label_Curr_Value.delete(0, '8')
                return self.Label_Curr_Value.insert(0, str(length+1))

        def MinusButton():
            length = int(self.Label_Curr_Value.get())
            if length <= 1:
                showinfo(title=MinusButton, message="Password length can't be less than zero")
            else:
                self.Label_Curr_Value.delete(0, '8')
                length -= 1
                return self.Label_Curr_Value.insert(0, length)

        def GenerateButton():
            try:
                length = self.Label_Curr_Value.get()

                if 1 <= int(length) <= 100 and length.isdigit():
                    use_numbers = self.include_numbers.get()
                    use_symbols = self.include_symbols.get()
                    use_upper = self.include_upper.get()
                    use_lower = self.include_lower.get()

                    password = PassGenFunc(int(length), use_numbers, use_symbols, use_upper, use_lower)
                    self.Label_Password.configure(text=password)
                else:
                    showinfo(title=GenerateButton, message="Invalid input")
            except ValueError:
                showinfo(title=GenerateButton, message="Invalid input")

        def PassGenFunc(length, use_numbers, use_symbols, use_upper, use_lower):
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



        # password options
        self.Label_Options = ctk.CTkLabel(self.options_frame, 
                                          text="Options", 
                                          font=self.BigFont,
                                          justify='center')
        self.Label_Options.grid(row=0, column=0, pady=(VAL10, VAL20))

        self.Checkbutton_1 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Numbers', 
                                             variable=self.include_numbers, 
                                             state='disabled',
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_1.grid(row=1, column=0, sticky='w', padx=VAL40, pady=VAL10)

        self.Checkbutton_2 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Symbols', 
                                             variable=self.include_symbols,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_2.grid(row=2, column=0, sticky='w', padx=VAL40, pady=VAL10)
        
        self.Checkbutton_3 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Upper Letters', 
                                             variable=self.include_upper,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_3.grid(row=3, column=0, sticky='w', padx=VAL40, pady=VAL10)
        
        self.Checkbutton_4 = ctk.CTkCheckBox(self.options_frame, 
                                             text='Lower Letters', 
                                             variable=self.include_lower,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton_4.grid(row=4, column=0, sticky='w', padx=VAL40, pady=VAL10)
        


        # password length
        self.Label_Length = ctk.CTkLabel(self.length_frame, 
                                         text="Length", 
                                         font=self.BigFont)
        self.Label_Length.grid(row=0, column=2, pady=(VAL10, VAL20), sticky='ew')

        self.Button_Plus = ctk.CTkButton(self.length_frame, 
                                         text="+", 
                                         width=VAL40,
                                         fg_color=self.BlackColor,
                                         hover_color=self.GreyColor,
                                         command=PlusButton,
                                         font=self.MediumFont)
        self.Button_Plus.grid(row=2, column=3, padx=VAL15)

        self.Button_Minus = ctk.CTkButton(self.length_frame, 
                                          text="–", 
                                          width=VAL40,
                                          fg_color=self.BlackColor,
                                          hover_color=self.GreyColor,
                                          command=MinusButton,
                                          font=self.MediumFont)
        self.Button_Minus.grid(row=2, column=1, padx=VAL15)

        self.Label_Curr_Value = ctk.CTkEntry(self.length_frame, 
                                             placeholder_text="8", 
                                             font=self.MediumFont,
                                             justify="center",
                                             width=VAL100)
        self.Label_Curr_Value.insert(0, '8')
        self.Label_Curr_Value.grid(row=2, column=2)

        self.Button_Curr_Value = ctk.CTkButton(self.length_frame, 
                                               text="Clear", 
                                               command=ClearButton, 
                                               fg_color=self.BlackColor, 
                                               hover_color=self.GreyColor,
                                               font=self.MediumFont,
                                               height=VAL50)
        self.Button_Curr_Value.grid(row=3, column=2, pady=VAL20)
        
        self.Button_Help = ctk.CTkButton(self.length_frame, 
                                         text="Help", 
                                         command=HelpButton, 
                                         fg_color=self.BlackColor, 
                                         hover_color=self.GreyColor,
                                         font=self.MediumFont,
                                         height=VAL50)
        self.Button_Help.grid(row=4, column=2)



        # password Generator
        self.Label_Your_Pass = ctk.CTkLabel(self.password_frame, 
                                            text="Your Password", 
                                            font=self.BigFont)
        self.Label_Your_Pass.grid(row=0, column=2, pady=(VAL10, VAL20))

        self.Button_Generate = ctk.CTkButton(self.password_frame, 
                                             text="Generate", 
                                             command=GenerateButton, 
                                             fg_color=self.BlackColor, 
                                             hover_color=self.GreyColor, 
                                             font=self.MediumFont,
                                             height=VAL50)
        self.Button_Generate.grid(row=1, column=2)

        self.Label_Password = ctk.CTkLabel(self.password_frame, 
                                           text="----------------", 
                                           font=self.MediumFont)
        self.Label_Password.grid(row=2, column=2, pady=VAL20)

        self.Button_Copy = ctk.CTkButton(self.password_frame, 
                                         text="Copy", 
                                         command=CopyButton, 
                                         fg_color=self.BlackColor, 
                                         hover_color=self.GreyColor,
                                         font=self.MediumFont,
                                         height=VAL50)
        self.Button_Copy.grid(row=3, column=2)

# window
APP = AppWindow()
APP.mainloop()