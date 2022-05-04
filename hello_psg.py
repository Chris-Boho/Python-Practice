import PySimpleGUI as sg

layout = [
    [sg.Text('Hello from Pysimple GUI')],
    [sg.Button('OK')]
]

# Create the window

window = sg.Window('Demo', layout)

# Create an event LookupError

while True:
    event, values = window.read()
    # End program if user closes window or presses OK button
    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()
