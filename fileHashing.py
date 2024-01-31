import hashlib
import PySimpleGUI as sg

def calculate_sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def main():
    sg.theme('LightBlue2')

    layout = [
        [sg.Text('File 1:', size=(8, 1)), sg.InputText(key='file1', size=(30, 1)), sg.FileBrowse(), sg.Button('Load Content 1')],
        [sg.Multiline(size=(60, 10), key='content1', disabled=True, autoscroll=True)],
        [sg.Text('File 2:', size=(8, 1)), sg.InputText(key='file2', size=(30, 1)), sg.FileBrowse(), sg.Button('Load Content 2')],
        [sg.Multiline(size=(60, 10), key='content2', disabled=True, autoscroll=True)],
        [sg.Button('Calculate Hashes', size=(15, 1)), sg.Button('Exit', size=(15, 1))],
        [sg.Multiline(size=(60, 10), key='output', disabled=True, autoscroll=True)]
    ]

    window = sg.Window('File Hash Calculator', layout, resizable=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Load Content 1':
            file_path1 = values['file1']
            try:
                with open(file_path1, 'r') as file:
                    data1 = file.read().replace('\n', '')
                    window['content1'].update(data1)
            except Exception as e:
                sg.popup_error(f"Error: {str(e)}")

        elif event == 'Load Content 2':
            file_path2 = values['file2']
            try:
                with open(file_path2, 'r') as file:
                    data2 = file.read().replace('\n', '')
                    window['content2'].update(data2)
            except Exception as e:
                sg.popup_error(f"Error: {str(e)}")

        elif event == 'Calculate Hashes':
            file_path1 = values['file1']
            file_path2 = values['file2']

            try:
                with open(file_path1, 'r') as file:
                    data1 = file.read().replace('\n', '')
                    window['content1'].update(data1)

                with open(file_path2, 'r') as file:
                    data2 = file.read().replace('\n', '')
                    window['content2'].update(data2)

                hash_hexdigest1 = calculate_sha256_hash(data1)
                hash_hexdigest2 = calculate_sha256_hash(data2)

                output_text = f"File 1: {hash_hexdigest1}\n"
                output_text += f"File 2: {hash_hexdigest2}\n"

                if hash_hexdigest1 == hash_hexdigest2:
                    output_text += 'The hashes are equal.'
                else:
                    output_text += 'The hashes are different.'

                window['output'].update(output_text)

            except Exception as e:
                sg.popup_error(f"Error: {str(e)}")

    window.close()

if __name__ == '__main__':
    main()
