from tkinter import *

#constants
DISPLAY_HEIGHT = 75
CALCULATOR_HEIGHT = 350
WIDTH = 400
SCREEN_COLOR = "#D3D3D3"
CALC_COLOR = "#B2BEB5"

screen_text  = ""

def buttons():
    
    pass
    
#helllp meeeee

def add_value(value):
    global screen_text
    
    screen_text = screen_text + str(value)
    
    #screen.delete("1,0", END) #END or 'end'
  #  screen.insert("1.0", screen_text)
    pass


def calculations():
    pass


def clear():
    pass



window = Tk()
window.title("Calculator")
window.resizable(False, False)





window.mainloop()