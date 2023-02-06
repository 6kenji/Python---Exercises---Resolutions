from tkinter import*
window = Tk()
window.title('My Application')

# A text entry box with a label:
Label(window, text = 'Name: ').grid(row = 0, column = 0)
my_text_box = Entry(window, width = 15)
my_text_box.grid(row = 0, column = 1)

# Two frames:
frame1 = Frame(window, height = 20, width = 100, bg = 'green')
frame1.grid(row = 0, column = 0)

frame2 = Frame(window, height = 20, width = 100, bg = 'red')
frame2.grid(row = 1, column = 1)

#A drop-down menu:
options = (1, 2, 3)
my_variable_object = IntVar() # Access the value with .get()
my_variable_object.set('Choose:')
my_dropdown = OptionMenu(window, my_variable_object, *options)
my_dropdown.grid()

window.mainloop()