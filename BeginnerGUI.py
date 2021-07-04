import random
import string
# module allows us to copy and paste text to and from the clipboard to your computer
import pyperclip
import PySimpleGUI as sg


QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'
#QT_ENTER_KEY3 = 'special 16777222'

sg.theme("DarkPurple7")


# Defining the window's contents
layout = [[sg.Text("Random Password Generator", font=("Helvetica", 15, "bold"))],
          [sg.Text("Select Password Length:", key='-OUTPUT1-', font=("Helvetica", 10, "bold")),
          sg.Spin([i for i in range(8, 21)], initial_value=8, size=(3, 4), key='-INPUT-')],
          #[sg.Spin([i for i in range(8, 21)], initial_value=8,
                   #size=(3, 4), key='-INPUT-')],
          #   [sg.Input(key='-INPUT-' "sd")],
          [sg.Text(size=(30, 1), key='-OUTPUT-', font=("Helvetica", 20, "bold"))],
          [sg.Button('Generate', key='-1-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")),
          #bind_return_key=True
           sg.Button('Copy', key='-2-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")), 
           sg.Button('Quit', key='-3-', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold"))]]
#use_default_focus=False, return_keyboard_events=True
window = sg.Window('Random Password Generator', layout, use_default_focus=False, return_keyboard_events=True, keep_on_top=False, size=(375, 200))

# Display and interact with the Window using an Event Loop
while True: 
    event, values = window.read()

    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):         # Check for ENTER key
        # go find element with Focus
        elem = window.find_element_with_focus()
        if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
            elem.Click()


    elif event == '-1-':
        #bind(bind_string, key_modifier)
        useript = values['-INPUT-']
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all, useript)
        password = "".join(temp)
        print(password)
        #sg.popup(password)
        window['-OUTPUT-'].update(password)

        #window["-INPUT-"].update("8")

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