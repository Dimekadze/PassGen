from tkinter.messagebox import showinfo
from PassGenFunc import PassGenFunc
import customtkinter as ctk
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
        VAL40 = 40
        VAL50 = 50
        VAL100 = 100

        # window size
        ScreenX = self.winfo_screenwidth()
        ScreenY = self.winfo_screenheight()
        x = (ScreenX // 2) - (APP_WIDTH // 2)
        y = (ScreenY // 2) - (APP_HEIGHT // 2)

        self.title('Password Generator') 
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}') 
        self.resizable(False, False)
        self.configure(fg_color=self.OrangeColor)

        self.IncludeNumbers = ctk.BooleanVar(value=True)
        self.IncludeSymbols = ctk.BooleanVar(value=False)
        self.IncludeUpper = ctk.BooleanVar(value=False)
        self.IncludeLower = ctk.BooleanVar(value=False)

        # font size
        self.BigFont = ("Verdana", 30)
        self.MediumFont = ("Verdana", 25)
        self.SmallFont = ("Verdana", 20)

        # frames
        self.OptionsFrame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.OptionsFrame.grid_propagate(False)

        self.LengthFrame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.LengthFrame.grid_propagate(False)
        self.PasswordFrame = ctk.CTkFrame(self, 
                                          width=FRAME_WIDTH, 
                                          height=FRAME_HEIGHT,
                                          corner_radius=VAL15)
        self.PasswordFrame.grid_propagate(False)

        # frames placing
        self.OptionsFrame.grid(row=0, column=0, padx=(VAL20, 0))
        self.LengthFrame.grid(row=0, column=1, padx=(VAL20, VAL20))
        self.PasswordFrame.grid(row=0, column=2, padx=(0, VAL20))

        # frames configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.OptionsFrame.grid_columnconfigure(0, weight=1)
        self.OptionsFrame.grid_rowconfigure(0, weight=1)
        self.OptionsFrame.grid_rowconfigure(1, weight=1)
        self.OptionsFrame.grid_rowconfigure(2, weight=1)
        self.OptionsFrame.grid_rowconfigure(3, weight=1)
        self.OptionsFrame.grid_rowconfigure(4, weight=1)
        self.OptionsFrame.grid_rowconfigure(5, weight=1)

        self.LengthFrame.grid_columnconfigure(0, weight=1)
        self.LengthFrame.grid_columnconfigure(1, weight=1)
        self.LengthFrame.grid_columnconfigure(2, weight=1)
        self.LengthFrame.grid_columnconfigure(3, weight=1)
        self.LengthFrame.grid_columnconfigure(4, weight=1)
        self.LengthFrame.grid_rowconfigure(0, weight=1)
        self.LengthFrame.grid_rowconfigure(1, weight=1)
        self.LengthFrame.grid_rowconfigure(2, weight=1)
        self.LengthFrame.grid_rowconfigure(3, weight=1)
        self.LengthFrame.grid_rowconfigure(4, weight=1)
        self.LengthFrame.grid_rowconfigure(5, weight=1)

        self.PasswordFrame.grid_columnconfigure(0, weight=1)
        self.PasswordFrame.grid_columnconfigure(1, weight=1)
        self.PasswordFrame.grid_columnconfigure(2, weight=1)
        self.PasswordFrame.grid_columnconfigure(3, weight=1)
        self.PasswordFrame.grid_columnconfigure(4, weight=1)
        self.PasswordFrame.grid_rowconfigure(0, weight=1)
        self.PasswordFrame.grid_rowconfigure(1, weight=1)
        self.PasswordFrame.grid_rowconfigure(2, weight=1)
        self.PasswordFrame.grid_rowconfigure(3, weight=1)



        # functions
        def HelpButton():
            showinfo(title="HelpButton", message="This is a simple password generator, what kind of help do you need here, you piece of felt boots?")

        def CopyButton():
            Password = self.LabelPassword.cget("text")
            if Password != "----------------":
                pyperclip.copy(Password)
                showinfo(title="CopyButton", message="Сopied to clipboard")
            else:
                showinfo(title="CopyButton", message="Try to generate a password")

        def ClearButton():
            self.Checkbutton2.deselect()
            self.Checkbutton3.deselect()
            self.Checkbutton4.deselect()
            self.LabelCurrValue.delete(0, '8')
            self.LabelCurrValue.insert(0, '8')

            showinfo(title="ClearButton", message="Cleared")

        def PlusButton():
            PasswordLength = int(self.LabelCurrValue.get())
            if PasswordLength >= 100:
                showinfo(title=MinusButton, message="Password length can't be more than 100")
            else:
                self.LabelCurrValue.delete(0, '8')
                return self.LabelCurrValue.insert(0, str(PasswordLength+1))

        def MinusButton():
            PasswordLength = int(self.LabelCurrValue.get())
            if PasswordLength <= 1:
                showinfo(title=MinusButton, message="Password length can't be less than zero")
            else:
                self.LabelCurrValue.delete(0, '8')
                PasswordLength -= 1
                return self.LabelCurrValue.insert(0, PasswordLength)

        def GenerateButton():
            try:
                PasswordLength = self.LabelCurrValue.get()

                if 1 <= int(PasswordLength) <= 100 and PasswordLength.isdigit():
                    UseNumbers = self.IncludeNumbers.get()
                    UseSymbols = self.IncludeSymbols.get()
                    UseUpper = self.IncludeUpper.get()
                    UseLower = self.IncludeLower.get()

                    FinalPassword = PassGenFunc(int(PasswordLength), UseNumbers, UseSymbols, UseUpper, UseLower)
                    self.LabelPassword.configure(text=FinalPassword)
                else:
                    showinfo(title=GenerateButton, message="Invalid input")
            except ValueError:
                showinfo(title=GenerateButton, message="Invalid input")



        # password options
        self.LabelOptions = ctk.CTkLabel(self.OptionsFrame, 
                                          text="Options", 
                                          font=self.BigFont,
                                          justify='center')
        self.LabelOptions.grid(row=0, column=0, pady=(VAL10, VAL20))

        self.Checkbutton1 = ctk.CTkCheckBox(self.OptionsFrame, 
                                             text='Numbers', 
                                             variable=self.IncludeNumbers, 
                                             state='disabled',
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton1.grid(row=1, column=0, sticky='w', padx=VAL40, pady=VAL10)

        self.Checkbutton2 = ctk.CTkCheckBox(self.OptionsFrame, 
                                             text='Symbols', 
                                             variable=self.IncludeSymbols,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton2.grid(row=2, column=0, sticky='w', padx=VAL40, pady=VAL10)
        
        self.Checkbutton3 = ctk.CTkCheckBox(self.OptionsFrame, 
                                             text='Upper Letters', 
                                             variable=self.IncludeUpper,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton3.grid(row=3, column=0, sticky='w', padx=VAL40, pady=VAL10)
        
        self.Checkbutton4 = ctk.CTkCheckBox(self.OptionsFrame, 
                                             text='Lower Letters', 
                                             variable=self.IncludeLower,
                                             font=self.SmallFont,
                                             fg_color=self.BlackColor,
                                             hover_color=self.GreyColor)
        self.Checkbutton4.grid(row=4, column=0, sticky='w', padx=VAL40, pady=VAL10)
        


        # password length
        self.LabelLength = ctk.CTkLabel(self.LengthFrame, 
                                         text="Length", 
                                         font=self.BigFont)
        self.LabelLength.grid(row=0, column=2, pady=(VAL10, VAL20), sticky='ew')

        self.ButtonPlus = ctk.CTkButton(self.LengthFrame, 
                                         text="+", 
                                         width=VAL40,
                                         fg_color=self.BlackColor,
                                         hover_color=self.GreyColor,
                                         command=PlusButton,
                                         font=self.MediumFont)
        self.ButtonPlus.grid(row=2, column=3, padx=VAL15)

        self.ButtonMinus = ctk.CTkButton(self.LengthFrame, 
                                          text="–", 
                                          width=VAL40,
                                          fg_color=self.BlackColor,
                                          hover_color=self.GreyColor,
                                          command=MinusButton,
                                          font=self.MediumFont)
        self.ButtonMinus.grid(row=2, column=1, padx=VAL15)

        self.LabelCurrValue = ctk.CTkEntry(self.LengthFrame, 
                                             placeholder_text="8", 
                                             font=self.MediumFont,
                                             justify="center",
                                             width=VAL100)
        self.LabelCurrValue.insert(0, '8')
        self.LabelCurrValue.grid(row=2, column=2)

        self.ButtonCurrValue = ctk.CTkButton(self.LengthFrame, 
                                               text="Clear", 
                                               command=ClearButton, 
                                               fg_color=self.BlackColor, 
                                               hover_color=self.GreyColor,
                                               font=self.MediumFont,
                                               height=VAL50)
        self.ButtonCurrValue.grid(row=3, column=2, pady=VAL20)
        
        self.ButtonHelp = ctk.CTkButton(self.LengthFrame, 
                                         text="Help", 
                                         command=HelpButton, 
                                         fg_color=self.BlackColor, 
                                         hover_color=self.GreyColor,
                                         font=self.MediumFont,
                                         height=VAL50)
        self.ButtonHelp.grid(row=4, column=2)



        # password Generator
        self.LabelYourPass = ctk.CTkLabel(self.PasswordFrame, 
                                            text="Your Password", 
                                            font=self.BigFont)
        self.LabelYourPass.grid(row=0, column=2, pady=(VAL10, VAL20))

        self.ButtonGenerate = ctk.CTkButton(self.PasswordFrame, 
                                             text="Generate", 
                                             command=GenerateButton, 
                                             fg_color=self.BlackColor, 
                                             hover_color=self.GreyColor, 
                                             font=self.MediumFont,
                                             height=VAL50)
        self.ButtonGenerate.grid(row=1, column=2)

        self.LabelPassword = ctk.CTkLabel(self.PasswordFrame, 
                                           text="----------------", 
                                           font=self.MediumFont)
        self.LabelPassword.grid(row=2, column=2, pady=VAL20)

        self.ButtonCopy = ctk.CTkButton(self.PasswordFrame, 
                                         text="Copy", 
                                         command=CopyButton, 
                                         fg_color=self.BlackColor, 
                                         hover_color=self.GreyColor,
                                         font=self.MediumFont,
                                         height=VAL50)
        self.ButtonCopy.grid(row=3, column=2)

# window
App = AppWindow()
App.mainloop()