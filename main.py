from tkinter import *
import random as r


# GLOBAL VARIABLES
length = 16  # password length
is_hidden = False
length_error = False
password = ""
colors = {
    "bg": "#F6EFFF",
    "title": "#4A148C",
    "insert": "#E3FFF1",
    "buttons_green": "#B9F6CA",
    "buttons_red": "#82B1FF",
    "error": "#E57373"
}


# MAIN WINDOW
root = Tk()  # the "Object"
root.title("Password Generator")  # window title
root.geometry("700x500")  # window size (width x height)
root.configure(bg=colors["bg"])  # sets the bg colour to light blue


# FRAMES
top_frame = Frame(root, bg=colors["bg"])  # title frame
top_frame.grid(row=0, column=0, columnspan=2, pady=20)
entry_frame = Frame(root, bg=colors["insert"])  # input frame
entry_frame.grid(row=1, column=0, columnspan=2, pady=20)
mid_frame = Frame(root, bg=colors["bg"])  # output frame
mid_frame.grid(row=2, column=0, columnspan=2, pady=20)
bottom_frame = Frame(root, bg=colors["bg"])  # buttons frame
bottom_frame.grid(row=3, column=0, columnspan=2, pady=10)
error_frame = Frame(root, bg=colors["bg"])  # error frame
error_frame.grid(row=4, column=0, columnspan=2, pady=20)


# FUNCTIONS
def generate(value=0, start=None):  # generates a random password
    global password, is_hidden, length_error
    password = ""
    length_error = False

    # length checking
    if value != 0 and 12 <= int(user_input.get()) <= 30:
        value = int(user_input.get())
    elif int(user_input.get()) < 12:
        value = 12
        length_error = True
    elif int(user_input.get()) > 30:
        value = 30
        length_error = True
    else:
        value = r.randint(12, 24)

    # show error if needed
    if length_error:
        error.grid(row=0, column=0, padx=50, pady=10)
    else:
        error.grid_forget()

    # generate password
    for i in range(value):
        password += chr(r.randint(33, 126))

    output.set(password)
    is_hidden = False
    show_hide()
    show_hide_button.grid(row=0, column=1, padx=20)


def show_hide():
    global is_hidden
    if is_hidden:
        output.set(password)
        button_text = "HIDE"
        is_hidden = False
    else:
        output.set("*"*len(password))
        button_text = "SHOW"
        is_hidden = True
    show_hide_button.config(text=button_text)


# WIDGETS
output = StringVar()
user_input = StringVar()
user_input.set(str(length))
output.set("*" * length)  # we use this to show ******* at the beginning

# title
title = Label(
    top_frame, text="PASSWORD GENERATOR", font=("Courier New", 30, "bold"),
    fg=colors["title"], bg=colors["bg"], justify="center"
)
title.grid(row=0, column=0, pady=20, padx=130)

# instruction label + entry input
instruction = Label(
    entry_frame, text="Length Needed:", bg=colors["insert"], fg=colors["title"], font=("Courier New", 15)
)
instruction.grid(row=0, column=0)
entry = Entry(entry_frame, textvariable=user_input, show="", bg=colors["insert"], font=("Courier New", 15))
entry.grid(row=0, column=1, pady=20, padx=10)

# password output
output_label = Entry(
    mid_frame, textvariable=output, font=("Courier New", 25, "bold"), fg=colors["title"], bg=colors["bg"],
    state="readonly", justify="center"
)
output_label.grid(row=0, column=0, pady=20)

# generate button
generate_button = Button(
    bottom_frame, text="GENERATE", font=("Courier New", 20), fg=colors["title"], bg=colors["buttons_green"],
    command=lambda: generate(value=length)
)
generate_button.grid(row=0, column=0, padx=20)

# show/hide button
show_hide_button = Button(
        bottom_frame, text="HIDE", font=("Courier New", 20), fg=colors["title"], bg=colors["buttons_red"],
        command=lambda: show_hide()
)

# in case of invalid length
error = Label(
    error_frame, text="Error: length value must be between 12 and 30 characters.", fg=colors["error"], bg=colors["bg"]
)


root.mainloop()
