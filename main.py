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

root.mainloop()