import PySimpleGUI as sg

def createWindow(theme):

    sg.theme(theme)
    sg.set_options(font= "Calibri  14", button_element_size= (6, 3))
    button_size = (6, 3)

    layout = [
        [sg.Text("", font = "Franklin 26",
                 justification = "center",
                 expand_x = True,
                 pad = (0, 30) ,
                 key = "-OUTPUT-",
                 right_click_menu = themeMenu)],

        [sg.Button("Clear", expand_x = True),
         sg.Button("Enter", expand_x = True)],

        [sg.Button("7", size = button_size),
         sg.Button("8", size = button_size),
         sg.Button("9", size = button_size),
         sg.Button("%", size = button_size, key = "/")],

        [sg.Button("4", size = button_size),
         sg.Button("5", size = button_size),
         sg.Button("6", size = button_size),
         sg.Button("x", size = button_size, key = "*")],

        [sg.Button("1", size = button_size),
         sg.Button("2", size = button_size),
         sg.Button("3", size = button_size),
         sg.Button("-", size = button_size)],

        [sg.Button("0", expand_x = True),
         sg.Button(".", size = button_size),
         sg.Button("+", size = button_size)]
    ]

    return sg.Window("Calculator", layout)

themeMenu = ["menu", ["BlueMono", "LightBlue1", "dark", "BrightColors", "random"]]

window = createWindow("LightBlue1")

curretNum = []
operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in themeMenu[1]:
        window.close()
        window = createWindow(event)

    if event in["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        curretNum.append(event)
        numStr = "".join(curretNum)
        window["-OUTPUT-"].update(numStr)

    if event in["+", "-", "/", "*"]:
        operation.append("".join(curretNum))
        curretNum = []
        operation.append(event)
        window["-OUTPUT-"].update("")

    if event == "Enter":
        operation.append("".join(curretNum))
        result = eval(" ".join(operation))
        window["-OUTPUT-"].update(round(result, 2))
        operation = []

    if event == "Clear":
        curretNum = []
        operation = []
        window["-OUTPUT-"].update("")

window.close()