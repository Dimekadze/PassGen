import secrets as sc
import string

def PassGenFunc(PasswordLength, UseNumbers, UseSymbols, UseUpper, UseLower):
    AllInOne = ''

    if UseNumbers:
        AllInOne += string.digits
    if UseSymbols:
        AllInOne += string.punctuation
    if UseUpper:
        AllInOne += string.ascii_uppercase
    if UseLower:
        AllInOne += string.ascii_lowercase

    FinalRandomPassword = ''.join(sc.choice(AllInOne) for i in range(PasswordLength))

    return FinalRandomPassword