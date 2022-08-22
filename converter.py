import PySimpleGUI as sg

layout = [
    [sg.Input(key = "-INPUT-"),
    sg.Spin(["km to mile", "kg to pound", "sec to min"], key = "-UNITS-"),
    sg.Button("Convert", key = "-CONVERTBUTTON-")],
    [sg.Text("Output", key = "-OUTPUT-")],
    [sg.Button("Close", key = "-CLOSEBUTTON-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CLOSEBUTTON-":
        window.close()

    if event == "-CONVERTBUTTON-":
        inputValue = values["-INPUT-"]

        if inputValue.isnumeric():
            if values["-UNITS-"] == "km to mile":
                output = float(inputValue) * 0.06214
                outputStr = f"{inputValue} km are {round(output, 2)} miles."

            elif values["-UNITS-"] == "kg to pound":
                output = float(inputValue) * 2.20462
                outputStr = f"{inputValue} kg are {round(output, 2)} pounds."

            elif values["-UNITS-"] == "sec to min":
                output = float(inputValue) / 60
                outputStr: str = f"{inputValue} sec are {round(output, 2)} mins."

            window["-OUTPUT-"].update(outputStr)

        else:
            window["-OUTPUT-"].update("Please enter an integer")