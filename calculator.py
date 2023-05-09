from tkinter import *


screen_text  = ""


def add_value(value):
    global screen_text
    
    if value == "=":
        calculations()
    
    elif value == "C":
        clear()
        
    else:
        screen_text = screen_text + str(value)

        field.delete("1.0", "end")
        field.insert("1.0", screen_text)
    

def calculations():

    global screen_text
    try:
        result = str(eval(screen_text))
        screen_text = ""
        
        field.delete("1.0", "end") 
        field.insert("1.0", result)
        
    except:
        screen_text = ""
        field.delete("1.0", "end") 
        field.insert("1.0", "Error")
    

def clear():
    global screen_text
    screen_text = ""
    field.delete("1.0", "end")
    

def buttons():
    
    btn1 = Button(window, text = "1", command = lambda: add_value(1),width=4, font=("Arial", 14))
    btn1.grid(row=2, column=1)

    btn2 = Button(window, text = "2", command = lambda: add_value(2), width=4, font=("Arial", 14))
    btn2.grid(row=2, column=2)
    
    btn3 = Button(window, text = "3", command = lambda: add_value(3), width=4, font=("Arial", 14))
    btn3.grid(row=2, column=3)
    
    btn_add = Button(window, text = "+", command = lambda: add_value("+"), width=4, font=("Arial", 14))
    btn_add.grid(row=2, column=4)
    
    btn4 = Button(window, text = "4", command = lambda: add_value(4), width=4, font=("Arial", 14))
    btn4.grid(row=3, column=1)
    
    btn5 = Button(window, text = "5", command = lambda: add_value(5), width=4, font=("Arial", 14))
    btn5.grid(row=3, column=2)
    
    btn6 = Button(window, text = "6", command = lambda: add_value(6), width=4, font=("Arial", 14))
    btn6.grid(row=3, column=3)

    btn_sub = Button(window, text = "-", command = lambda: add_value("-"), width=4, font=("Arial", 14))
    btn_sub.grid(row=3, column=4)
    
    btn7 = Button(window, text = "7", command = lambda: add_value(7), width=4, font=("Arial", 14))
    btn7.grid(row=4, column=1)
    
    btn8 = Button(window, text = "8", command = lambda: add_value(8), width=4, font=("Arial", 14))
    btn8.grid(row=4, column=2)
    
    btn9 = Button(window, text = "9", command = lambda: add_value(9), width=4, font=("Arial", 14))
    btn9.grid(row=4, column=3)
    
    btn_mult = Button(window, text = "x", command = lambda: add_value("*"), width=4, font=("Arial", 14))
    btn_mult.grid(row=4, column=4)
    
    btn_p1 = Button(window, text = "(", command = lambda: add_value("("), width=4, font=("Arial", 14))
    btn_p1.grid(row=5, column=1)
    
    btn0 = Button(window, text = "0", command = lambda: add_value(0), width=4, font=("Arial", 14))
    btn0.grid(row=5, column=2)
    
    btn_p2 = Button(window, text = ")", command = lambda: add_value(")"), width=4, font=("Arial", 14))
    btn_p2.grid(row=5, column=3)
    
    btn_div = Button(window, text = "/", command = lambda: add_value("/"), width=4, font=("Arial", 14))
    btn_div.grid(row=5, column=4)
    
    btn_clear = Button(window, text = "C", command = lambda: add_value("C"), width=10, font=("Arial", 14)) 
    btn_clear.grid(row=6, column=1, columnspan=2)
    
    btn_equal = Button(window, text = "=", command = lambda: add_value("="), width=10, font=("Arial", 14))
    btn_equal.grid(row=6, column=3, columnspan=2)
    


window = Tk()
window.title("Calculator")
window.geometry("300x215")

field = Text(window, height = 2, width = 21, font=("Arial", 24))
field.grid(columnspan=5)


buttons()

window.mainloop()