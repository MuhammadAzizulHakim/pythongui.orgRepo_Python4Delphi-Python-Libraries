import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

def main():
    layout = [
        [sg.Image(key='-IMAGE-')],
        [sg.FileBrowse('Open Image'), sg.Button('Exit')]
    ]

    window = sg.Window('Image Viewer', layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Open Image':
            file_path = values['FileBrowse']
            if file_path:
                image = open_and_resize_image(file_path)
                window['-IMAGE-'].update(data=image)

    window.close()

def open_and_resize_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((300, 300))
    image_data = ImageTk.PhotoImage(image)
    return image_data

if __name__ == '__main__':
    main()
