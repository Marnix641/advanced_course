from tkinter import *

formula = ""


def press(num):
    global formula

    formula = formula + str(num)

    equation.set(formula)


def equalpress():
    try:

        global formula

        total = str(eval(formula))

        equation.set(total)

        formula = ""

    except:

        equation.set(" error ")
        formula = ""


def clear():
    global formula
    formula = ""
    equation.set("")


def back():
    global formula
    formula = equation.get()[:-1]
    equation.set(formula)


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="lightcyan2")

    gui.title("Calculator")

    gui.geometry("350x360")

    equation = StringVar()

    formula_field = Entry(gui, textvariable=equation, justify="right")

    formula_field.grid(columnspan=4, ipadx=110, pady=5)

    equation.set("0")

    button1 = Button(gui, text=' 1 ', fg='black', bg='dodger blue', command=lambda: press(1), height=2, width=10)
    button1.grid(row=2, column=0, pady=5)

    button2 = Button(gui, text=' 2 ', fg='black', bg='dodger blue', command=lambda: press(2), height=2, width=10)
    button2.grid(row=2, column=1, pady=5)

    button3 = Button(gui, text=' 3 ', fg='black', bg='dodger blue', command=lambda: press(3), height=2, width=10)
    button3.grid(row=2, column=2, pady=5)

    button4 = Button(gui, text=' 4 ', fg='black', bg='dodger blue', command=lambda: press(4), height=2, width=10)
    button4.grid(row=3, column=0, pady=5)

    button5 = Button(gui, text=' 5 ', fg='black', bg='dodger blue', command=lambda: press(5), height=2, width=10)
    button5.grid(row=3, column=1, pady=5)

    button6 = Button(gui, text=' 6 ', fg='black', bg='dodger blue', command=lambda: press(6), height=2, width=10)
    button6.grid(row=3, column=2, pady=5)

    button7 = Button(gui, text=' 7 ', fg='black', bg='dodger blue', command=lambda: press(7), height=2, width=10)
    button7.grid(row=4, column=0, pady=5)

    button8 = Button(gui, text=' 8 ', fg='black', bg='dodger blue', command=lambda: press(8), height=2, width=10)
    button8.grid(row=4, column=1, pady=5)

    button9 = Button(gui, text=' 9 ', fg='black', bg='dodger blue', command=lambda: press(9), height=2, width=10)
    button9.grid(row=4, column=2, pady=5)

    button0 = Button(gui, text=' 0 ', fg='black', bg='dodger blue', command=lambda: press(0), height=2, width=10)
    button0.grid(row=5, column=0, pady=5)

    plus = Button(gui, text=' + ', fg='black', bg='dodger blue', command=lambda: press("+"), height=2, width=10)
    plus.grid(row=2, column=3, pady=5)

    minus = Button(gui, text=' - ', fg='black', bg='dodger blue', command=lambda: press("-"), height=2, width=10)
    minus.grid(row=3, column=3, pady=5)

    multiply = Button(gui, text=' * ', fg='black', bg='dodger blue', command=lambda: press("*"), height=2, width=10)
    multiply.grid(row=4, column=3, pady=5)

    divide = Button(gui, text=' / ', fg='black', bg='dodger blue', command=lambda: press("/"), height=2, width=10)
    divide.grid(row=5, column=3, pady=5)

    equal = Button(gui, text=' = ', fg='black', bg='dodger blue', command=equalpress, height=2, width=10)
    equal.grid(row=5, column=2, pady=5)

    clear = Button(gui, text='Clear', fg='black', bg='dodger blue', command=clear, height=2, width=10)
    clear.grid(row=6, column=0, pady=5)

    Decimal = Button(gui, text='.', fg='black', bg='dodger blue', command=lambda: press('.'), height=2, width=10)
    Decimal.grid(row=5, column=1, pady=5)

    back = Button(gui, text='Back', fg='black', bg='dodger blue', command=back, height=2, width=10)
    back.grid(row=6, column=1, pady=5)

    square = Button(gui, text=' ^ ', fg='black', bg='dodger blue', command=lambda: press("**"), height=2, width=10)
    square.grid(row=6, column=2, pady=5)

    sqroot = Button(gui, text=' Root ', fg='black', bg='dodger blue', command=lambda: press("**(1/2)"), height=2, width=10)
    sqroot.grid(row=6, column=3, pady=5)

    openhekje = Button(gui, text=' ( ', fg='black', bg='dodger blue', command=lambda: press("("), height=2, width=10)
    openhekje.grid(row=7, column=0, pady=5)

    sluithekje = Button(gui, text=' ) ', fg='black', bg='dodger blue', command=lambda: press(")"), height=2, width=10)
    sluithekje.grid(row=7, column=1, pady=5)

    # start the GUI
    gui.mainloop()
