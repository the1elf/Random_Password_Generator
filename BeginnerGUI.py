import random
import string
# module allows us to copy and paste text to and from the clipboard to your computer
import pyperclip
import PySimpleGUI as sg


QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

sg.theme("DarkPurple7")


# Defining the window's contents
layout = [[sg.Text("Random Password Generator", font=("Helvetica", 15, "bold"))],
          [sg.Text("Select Password Length:", key='-OUTPUT1-', font=("Helvetica", 10, "bold")),
          sg.Spin([i for i in range(8, 21)], initial_value=8, size=(4, 4), key='-INPUT-')],
          [sg.Text(size=(30, 1), key='-OUTPUT-', font=("Helvetica", 20, "bold"))],
          [sg.Button('Generate', key='-1-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")),
          sg.Button('Copy', key='-2-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")), 
          sg.Button('Quit', key='-3-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold"))]]

window = sg.Window('Random Password Generator', layout, use_default_focus=False, return_keyboard_events=True, keep_on_top=False, size=(375, 200))

# Display and interact with the Window using an Event Loop
while True: 
    event, values = window.read()

    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):         # Check for ENTER key
        elem = window.find_element_with_focus()
        if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
            elem.Click()


    elif event == '-1-':
        useript = values['-INPUT-']
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all, useript)
        password = "".join(temp)
        print(password)
        window['-OUTPUT-'].update(password)

        
    elif event == '-2-':
        op = window['-OUTPUT-'].get()
        pyperclip.copy(op)
        # Output a message to the window
        #sg.popup("Password is copied to your clipboard")
        sg.popup_auto_close("Password Copied", button_type=5, auto_close_duration=.5)
               

    # See if user wants to quit or window was closed
    elif event == sg.WINDOW_CLOSED or event == '-3-':
        break

# Finish up by removing from the screen
window.close()
