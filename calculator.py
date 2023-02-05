from tkinter import *

expression = ""

def press_button(button):
    if button == "=":
        compute()
        return 
    
    global expression
    expression += str(button)
    equation.set(expression)

def compute():
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def erase():
    global expression
    expression = ""
    equation.set("")


# Noir : #101419
# Bleu : #476C9B
# Rouge : #984447

gui = Tk()

gui.title("Calculatrice")
gui.geometry("235x285")
gui.configure(background="#101419")

    # Get current application data
equation = StringVar()

    # Result box
result = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height="2")
result.grid(columnspan=4)

buttons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
calculator_row = 1
calculator_column = 0

for button in buttons:
        newButton = Label(gui, text=str(button), bg="#476C9B", fg="#FFF", height=4, width=6)

        newButton.bind("<Button-1>", lambda e, button=button: press_button(button))
        newButton.grid(row=calculator_row, column=calculator_column)

        calculator_column += 1
        if calculator_column == 4:
            calculator_column = 0
            calculator_row += 1

newButton = Label(gui, text="Effacer", bg="#984447", fg="#FFF", height=4, width=26)
newButton.bind("<Button-1>", lambda e: erase())
newButton.grid(columnspan=4)

gui.mainloop()