from tkinter import *

def btnCLick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

root = Tk()

root.title("Calculator with TK")
operator=""
text_Input =StringVar()

txtDisplay = Entry(root, font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify="right").grid(columnspan=4)

btn7=Button(root, padx=16, bd=8, command=lambda:btnCLick(7), fg="black", font=('arial', 20,'bold'), text="7").grid(row=1, column=0)
btn8=Button(root, padx=16, bd=8, command=lambda:btnCLick(8),fg="black", font=('arial', 20,'bold'), text="8").grid(row=1, column=1)
btn9=Button(root, padx=16, bd=8, command=lambda:btnCLick(9), fg="black", font=('arial', 20,'bold'), text="9").grid(row=1, column=2)
Addition=Button(root, padx=16, bd=8, command=lambda:btnCLick("+"), fg="black", font=('arial', 20,'bold'), text="+").grid(row=1, column=3)
# 1st line

btn4=Button(root, padx=16, bd=8, command=lambda:btnCLick(4), fg="black", font=('arial', 20,'bold'), text="4").grid(row=2, column=0)
btn5=Button(root, padx=16, bd=8, command=lambda:btnCLick(5), fg="black", font=('arial', 20,'bold'), text="5").grid(row=2, column=1)
btn6=Button(root, padx=16, bd=8, command=lambda:btnCLick(6), fg="black", font=('arial', 20,'bold'), text="6").grid(row=2, column=2)
Substraction=Button(root, padx=16, bd=8, fg="black", command=lambda:btnCLick("-"), font=('arial', 20,'bold'), text="-").grid(row=2, column=3)
# 2nd line

btn1=Button(root, padx=16, bd=8, command=lambda:btnCLick(1), fg="black", font=('arial', 20,'bold'), text="1").grid(row=3, column=0)
btn2=Button(root, padx=16, bd=8, command=lambda:btnCLick(2), fg="black", font=('arial', 20,'bold'), text="2").grid(row=3, column=1)
btn3=Button(root, padx=16, bd=8, command=lambda:btnCLick(3), fg="black", font=('arial', 20,'bold'), text="3").grid(row=3, column=2)
Multiply=Button(root, padx=16, bd=8, fg="black", command=lambda:btnCLick("*"), font=('arial', 20,'bold'), text="*").grid(row=3, column=4)
# 3rd line

btn0=Button(root, padx=16, pady=16, command=lambda:btnCLick(0), bd=8, fg="black", font=('arial', 20,'bold'), text="0").grid(row=4, column=0)
btnClear=Button(root, padx=16, pady=16, bd=8, fg="black", command=lambda:btnCLick("C"), font=('arial', 20,'bold'), text="C").grid(row=4, column=1)
btn11=Button(root, padx=16, pady=16, bd=8, fg="black", command=lambda:btnCLick("="), font=('arial', 20,'bold'), text="=").grid(row=4, column=2)
Division=Button(root, padx=16, pady=16, bd=8, fg="black", command=lambda:btnCLick("/"), font=('arial', 20,'bold'), text="/").grid(row=4, column=4)
# 4th line

root.mainloop()