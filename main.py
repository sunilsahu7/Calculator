from tkinter import *

root = Tk()

root.title("Calculator with TK")
operator=""
text_Input =StringVar()

txtDisplay = Entry(root, font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify="right").grid(columnspan=4)

btn7=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="7").grid(row=1, column=0)
btn8=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="8").grid(row=1, column=1)
btn9=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="9").grid(row=1, column=2)
Addition=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="+").grid(row=1, column=3)

btn4=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="4").grid(row=2, column=0)
btn5=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="5").grid(row=2, column=1)
btn6=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="6").grid(row=2, column=2)
Substraction=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="-").grid(row=2, column=3)

btn1=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="4").grid(row=3, column=0)
btn2=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="5").grid(row=3, column=1)
btn3=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="6").grid(row=3, column=2)
Substraction=Button(root, padx=16, bd=8, fg="black", font=('arial', 20,'bold'), text="X").grid(row=3, column=3)

Radiobutton(text = "test")

root.mainloop()