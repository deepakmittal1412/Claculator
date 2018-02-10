from tkinter import *
import parser

root = Tk()
root.resizable(0, 0)
root.propagate()
i = 0


def operation(op):
    global i
    l = len(op)
    ent.insert(i, op)
    i += l


def calculate():
    s = ent.get()
    if '!' in s:
        j = s.index('!')
        n = int(s[j - 1])
        f = 1
        for k in range(n, 1, -1):
            f *= k
        f = str(f)
        s = s[:j - 1] + f + s[j + 1:]
    try:
        a = parser.expr(s).compile()
        r = eval(a)
        clearall()
        ent.insert(0, r)
    except Exception:
        clearall()
        ent.insert(0, "Error")


def get_values(num):
    global i
    ent.insert(i, num)
    i += 1


def clearall():
    ent.delete(0, END)


def undo():
    s = ent.get()
    if (len(s)):
        clearall()
        ent.insert(0, s[:-1])
    else:
        clearall()
        ent.insert(0, "Error")


ent = Entry(root)
ent.grid(row=1, columnspan=10, sticky=W + E)

Button(root, text='1', command=lambda: get_values(1)).grid(row=2, column=0)
Button(root, text='2', command=lambda: get_values(2)).grid(row=2, column=1)
Button(root, text='3', command=lambda: get_values(3)).grid(row=2, column=2)

Button(root, text='4', command=lambda: get_values(4)).grid(row=3, column=0)
Button(root, text='5', command=lambda: get_values(5)).grid(row=3, column=1)
Button(root, text='6', command=lambda: get_values(6)).grid(row=3, column=2)

Button(root, text='7', command=lambda: get_values(7)).grid(row=4, column=0)
Button(root, text='8', command=lambda: get_values(8)).grid(row=4, column=1)
Button(root, text='9', command=lambda: get_values(9)).grid(row=4, column=2)

Button(root, text='AC', command=clearall).grid(row=5, column=0)
Button(root, text='0', command=lambda: get_values(0)).grid(row=5, column=1)
Button(root, text='=', command=calculate).grid(row=5, column=2)

Button(root, text='+', command=lambda: operation("+")).grid(row=2, column=3)
Button(root, text='-', command=lambda: operation("-")).grid(row=3, column=3)
Button(root, text='*', command=lambda: operation("*")).grid(row=4, column=3)
Button(root, text='/', command=lambda: operation("/")).grid(row=5, column=3)

Button(root, text='pi', command=lambda: operation("*3.14")).grid(row=2, column=4)
Button(root, text='%', command=lambda: operation("%")).grid(row=3, column=4)
Button(root, text='(', command=lambda: operation("(")).grid(row=4, column=4)
Button(root, text='exp', command=lambda: operation("**")).grid(row=5, column=4)

Button(root, text='<-', command=undo).grid(row=2, column=5)
Button(root, text='X!', command=lambda: operation("!")).grid(row=3, column=5)
Button(root, text=')', command=lambda: operation(")")).grid(row=4, column=5)
Button(root, text='X^2', command=lambda: operation("**2")).grid(row=5, column=5)

root.mainloop()
