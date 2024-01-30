import hashlib
import PySimpleGUI as sg
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_message(private_key, message):
    key = RSA.import_key(private_key)
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    return signature

def verify_signature(public_key, message, signature):
    key = RSA.import_key(public_key)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

sg.theme('LightGrey1')

layout = [
    [sg.Text('Enter your message:', size=(15, 1)), sg.InputText(key='-MESSAGE-')], #, password_char='*')],
    [sg.Button('Sign'), sg.Button('Verify')],
    [sg.Text('Hashed Signature:', size=(15, 1)), sg.Text('', size=(70, 1), key='-OUTPUT-')]
]


window = sg.Window('RSA Digital Signature', layout, resizable=True, finalize=True, element_justification='center')

private_key, public_key = generate_key_pair()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Sign":
        message = values['-MESSAGE-'].encode("utf-8")
        signature = sign_message(private_key, message)
        window['-OUTPUT-'].update(f"{signature.hex()}")

    elif event == "Verify":
        message = values['-MESSAGE-'].encode("utf-8")
        signature_str = window['-OUTPUT-'].DisplayText
        signature = bytes.fromhex(signature_str)
        is_valid = verify_signature(public_key, message, signature)
        if is_valid:
            window['-OUTPUT-'].update("Signature is valid")
        else:
            window['-OUTPUT-'].update("Signature is NOT valid")

window.close()

