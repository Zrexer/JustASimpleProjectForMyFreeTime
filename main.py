from colorama import Fore as f
from os import system
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from subprocess import getoutput
from time import sleep
import wikipedia

system("cls")


print(f""" {f.LIGHTGREEN_EX}
██╗  ██╗ ██████╗ ███████╗████████╗ ██╗██╗     ███████╗████████╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝███║██║     ██╔════╝╚══██╔══╝
███████║██║   ██║███████╗   ██║   ╚██║██║     █████╗     ██║   
██╔══██║██║   ██║╚════██║   ██║    ██║██║     ██╔══╝     ██║   
██║  ██║╚██████╔╝███████║   ██║    ██║███████╗███████╗   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═╝╚══════╝╚══════╝   ╚═╝   
{f.RED}-------------------------------------------------------------------                                                               """)


print(f"""
{f.GREEN}[{f.YELLOW}1{f.GREEN}]{f.YELLOW} My Number 
{f.GREEN}[{f.YELLOW}2{f.GREEN}]{f.YELLOW} Web Hacking
{f.GREEN}[{f.YELLOW}3{f.GREEN}]{f.YELLOW} Open Calculator
{f.GREEN}[{f.YELLOW}4{f.GREEN}]{f.YELLOW} Github 
{f.GREEN}[{f.YELLOW}5{f.GREEN}]{f.YELLOW} Open File And Write
{f.GREEN}[{f.YELLOW}6{f.GREEN}]{f.YELLOW} Get Your ClipBoard
{f.GREEN}[{f.YELLOW}7{f.GREEN}]{f.YELLOW} Search Wikipedia
 """)

x = int(input(f"{f.LIGHTGREEN_EX}set{f.WHITE}> "))

if x == 1:
    print(f"{f.CYAN}0912345678")

elif x == 2:
    while True:
        print(f"{f.RED}The Website Was Hack !")

elif x == 3:
        
    window = tk.Tk()
    window.title('Calculator-GeeksForGeeks')
    frame = tk.Frame(master=window, bg="skyblue", padx=10)
    frame.pack()
    entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
    entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
    
    
    def myclick(number):
        entry.insert(tk.END, number)
    
    
    def equal():
        try:
            y = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, y)
        except:
            tkinter.messagebox.showinfo("Error", "Syntax Error")
    
    
    def clear():
        entry.delete(0, tk.END)
    
    
    button_1 = tk.Button(master=frame, text='1', padx=15,
                        pady=5, width=3, command=lambda: myclick(1))
    button_1.grid(row=1, column=0, pady=2)
    button_2 = tk.Button(master=frame, text='2', padx=15,
                        pady=5, width=3, command=lambda: myclick(2))
    button_2.grid(row=1, column=1, pady=2)
    button_3 = tk.Button(master=frame, text='3', padx=15,
                        pady=5, width=3, command=lambda: myclick(3))
    button_3.grid(row=1, column=2, pady=2)
    button_4 = tk.Button(master=frame, text='4', padx=15,
                        pady=5, width=3, command=lambda: myclick(4))
    button_4.grid(row=2, column=0, pady=2)
    button_5 = tk.Button(master=frame, text='5', padx=15,
                        pady=5, width=3, command=lambda: myclick(5))
    button_5.grid(row=2, column=1, pady=2)
    button_6 = tk.Button(master=frame, text='6', padx=15,
                        pady=5, width=3, command=lambda: myclick(6))
    button_6.grid(row=2, column=2, pady=2)
    button_7 = tk.Button(master=frame, text='7', padx=15,
                        pady=5, width=3, command=lambda: myclick(7))
    button_7.grid(row=3, column=0, pady=2)
    button_8 = tk.Button(master=frame, text='8', padx=15,
                        pady=5, width=3, command=lambda: myclick(8))
    button_8.grid(row=3, column=1, pady=2)
    button_9 = tk.Button(master=frame, text='9', padx=15,
                        pady=5, width=3, command=lambda: myclick(9))
    button_9.grid(row=3, column=2, pady=2)
    button_0 = tk.Button(master=frame, text='0', padx=15,
                        pady=5, width=3, command=lambda: myclick(0))
    button_0.grid(row=4, column=1, pady=2)
    
    button_add = tk.Button(master=frame, text="+", padx=15,
                        pady=5, width=3, command=lambda: myclick('+'))
    button_add.grid(row=5, column=0, pady=2)
    
    button_subtract = tk.Button(
        master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
    button_subtract.grid(row=5, column=1, pady=2)
    
    button_multiply = tk.Button(
        master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
    button_multiply.grid(row=5, column=2, pady=2)
    
    button_div = tk.Button(master=frame, text="/", padx=15,
                        pady=5, width=3, command=lambda: myclick('/'))
    button_div.grid(row=6, column=0, pady=2)
    
    button_clear = tk.Button(master=frame, text="clear",
                            padx=15, pady=5, width=12, command=clear)
    button_clear.grid(row=6, column=1, columnspan=2, pady=2)
    
    button_equal = tk.Button(master=frame, text="=", padx=15,
                            pady=5, width=9, command=equal)
    button_equal.grid(row=7, column=0, columnspan=3, pady=2)
    
    window.mainloop()


elif x == 4:
    print(f"{f.GREEN}https://github.com/Zrexer")

elif x == 5:
    nmfile = input(f"{f.GREEN}Name File{f.WHITE}> ")
    wr = input(f"{f.GREEN}Write{f.WHITE}> ")
    with open(nmfile, 'a') as a:
        for i in range(1):
            a.write(wr)
    print(f"{f.LIGHTBLACK_EX}Your Text File Was Created And Your Message Was Writed in Your Text File !")

elif x == 6:
    print(f"{f.RED}Please Wait . . .")
    sleep(2)
    gtclp = getoutput("powershell get-clipboard")
    print(f"{f.GREEN}{gtclp}")
    print("")

elif x == 7:
    sea = str(input(f"{f.GREEN}search{f.WHITE}> "))
    wksea = wikipedia.search(sea)
    print(wksea)

else:
    print("")
