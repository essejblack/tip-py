from tkinter import Button,Label,DoubleVar,Entry,Tk

window = Tk()
window.title("tip")
window.geometry("500x500")
window.configure(bg="#d9d9d9")

def calculate_tip():
    bill = bl_value.get()
    tip=(bill/100)*5
    tp_value.set(tip)
    total = bill + tip
    total_value.set(total)

def clear():
    bl_value.set("")
    tp_value.set("")
    total_value.set("")

bl_label = Label(window, text="Bill Amount",bg="black",fg="white")
bl_label.grid(column=1, row=1, padx=10, pady=10)

bl_value = DoubleVar()
bl_entry = Entry(window, textvariable=bl_value,width=10)
bl_entry.grid(column=2, row=1, padx=10, pady=10)
bl_entry.delete(0, "end")

tp_label = Label(window, text="Tip",bg="black",fg="white")
tp_label.grid(column=1, row=2, padx=10, pady=10)

tp_value = DoubleVar()
tp_entry = Entry(window, textvariable=tp_value,width=10)
tp_entry.grid(column=2, row=2, padx=10, pady=10)
tp_entry.delete(0, "end")

total_label = Label(window, text="Total",bg="black",fg="white")
total_label.grid(column=1, row=3, padx=10, pady=10)

total_value = DoubleVar()
total_entry = Entry(window, textvariable=total_value,width=10)
total_entry.grid(column=2, row=3, padx=10, pady=10)
total_entry.delete(0, "end")

calculate_btn = Button(bg="green",fg="white",command=calculate_tip,width=15,text="calculate")
calculate_btn.grid(column=1, row=4, padx=50, pady=50)

clear_btn = Button(bg="black",fg="white",command=clear,width=15,text="clear")
clear_btn.grid(column=2, row=4, padx=50, pady=50)




window.mainloop()