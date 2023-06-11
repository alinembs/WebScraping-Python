import PySimpleGUI as sg
import random, time
sg.theme("LightBlue")


layout=[[sg.ProgressBar(50, orientation='h', size=(100, 20), border_width=4, key='-PROGRESS_BAR-')],
        [sg.Button('Execute Process'), sg.Button('Stop Process'), sg.Exit()]]

window =sg.Window("Progress Bar",layout)


while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
                break
    if event == "Execute Process":
        for i in range(50):
            # Pause for 1 second each iteration (Can be replaced by time.sleep(.01))
            event, values = window.read(1000)
            if event == 'Stop Process':
                break
            window['-PROGRESS_BAR-'].update(i+1)

window.close()
    

