import os

SPACING = "\t\t"
LOGO = f"""{SPACING}╦ ╦╔═╗╦═╗╔╦╗╦  ╔═
{SPACING}╙╨╜╙─╜╨╙─ ╨╜╨─╜╙─"""

class Screen:    
    def clear_screen(self):
        os_name = os.name.lower()
        if os_name == 'posix':  # Unix/Linux/MacOS
            os.system("clear")
        elif os_name == 'nt':   # Windows
            os.system("cls")