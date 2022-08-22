import PySimpleGUI as sg
from time import time

def createWindow():
    sg.theme("black")

    layout = [
        [sg.VPush()],
        [sg.Text("0.0", font = "Young 50", key = "-OUTPUT-")],
        [sg.Button("Start", button_color = ("#FFFFFF", "#FF0000"), border_width = 0, key = "-START-"),
         sg.Button("Lap", button_color = ("#FFFFFF","#FF0000"), border_width = 0, key = "-LAP-", visible = False)],
        [sg.Column([[]], key = "-LAPS-")],
        [sg.VPush()]
    ]

    return sg.Window("Stopwatch",
                    layout,
                    size = (300, 350),
                    element_justification = "center")

window = createWindow()

startTime = 0
active = False
lapAmt = 1

while True:
    event, valeus = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, "Close"):
        break

    if event == "-START-":
        if active:
            #from active to stop
            active = False
            window["-START-"].update("Reset")
            window["-LAP-"].update(visible = False)
        else:
            #from sto to reset
            if startTime > 0:
                window.close()
                window = createWindow()
                startTime = 0
                lapAmt = 1
            else:
                #from start to active
                startTime = time()
                active = True
                window["-START-"].update("Stop")
                window["-LAP-"].update(visible = True)

    if active:
        elapsedTime = round(time() - startTime, 1)
        window["-OUTPUT-"].update(elapsedTime)

    if event == "-LAP-":
        window.extend_layout(window["-LAPS-"], [[sg.Text(lapAmt), sg.VSeparator(), sg.Text(elapsedTime)]])
        lapAmt += 1

window.close()