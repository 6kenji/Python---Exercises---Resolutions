# Gender UI, using Drop-down menu instead of Radio Buttons

from tkinter import*

# Functions go here:
def change_text():
    my_label.config(text = options)

# GUI code go here:
# Create the main tkinter window

window = Tk()
window.title('My Application')

# Add an empty tkinter label widget and place it in a grid layout
my_label = Label(window, width = 25, height = 1, text = '')
my_label.grid(row = 0, column = 0)

# Add an empty tkinter button widget, place it in a grid layout
# and attach the change_text() function

my_button = Button(window, text = 'Submit', width = 25, command = change_text)
my_button.grid(row = 1, column = 0)

# Add drop-down menu:

options = (1, 2, 3)
my_variable_object = IntVar() # Access the value with .get()
my_variable_object.set('Choose:')
my_dropdown = OptionMenu(window,  my_variable_object, *options)
my_dropdown.grid()

# Enter the main loop event
window.mainloop()