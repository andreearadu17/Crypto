import argparse
import hashlib
import PySimpleGUI as sg

def hash_password(password, hashtype="sha256"):
    x = getattr(hashlib, hashtype)()
    x.update(password.encode())
    return x.hexdigest()

sg.theme('LightGrey1')

layout = [
    [sg.Text('Password:', size=(10, 1)), sg.InputText(key='-PASSWORD-')], #, password_char='*')],
    [sg.Button('Hash'), sg.Button('Exit')],
    [sg.Text('Hashed Password:', size=(15, 1)), sg.Text('', size=(50, 1), key='-OUTPUT-')]
]

window = sg.Window('Password Hasher', layout, resizable=True, finalize=True, element_justification='center')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Hash':
        password = values['-PASSWORD-']
        hashed_password = hash_password(password)
        window['-OUTPUT-'].update(hashed_password)

window.close()
