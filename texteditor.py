import PySimpleGUI as sg
from pathlib import Path

smileys = [
    "happy", [":)", "xD", ":D", "•◡•"],
    "sad", [":(", ":-|", ":-(", "T_T"],
    "other", [";P", ":-/", ":O", "^_^"]
]

smileyEvents = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count", "Character Count"]],
    ["Add", smileys]
]

sg.theme("GrayGrayGray")

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text("Untitled", key = "-DOCNAME-")],
    [sg.Multiline(no_scrollbar = True, size = (50, 30), key = "-TEXTBOX-")]
]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Open":
        filePath = sg.popup_get_file("Open", no_window = True)
        if filePath:
            file = Path(filePath)
            print(file.read_text())
            window["-TEXTBOX-"].update(file.read_text())
            window["-DOCNAME-"].update(filePath.split("/")[-1])

    if event == "Save":
        filePath = sg.popup_get_file("Save as", no_window = True, save_as = True) + ".txt"
        file = Path(filePath)
        file.write_text(values["-TEXTBOX-"])
        window["-DOCNAME-"].update(filePath.split("/")[-1])

    fullText = values["-TEXTBOX-"]
    cleanText = fullText.replace("\n", " ").split(" ")

    if event == "Word Count":
        wordCount = len(cleanText)
        sg.popup(f"{wordCount} words")

    if event == "Character Count":
        wordCount = len(cleanText)
        charCount = len("".join(cleanText))
        sg.popup(f"{charCount} characters")

    if event in smileyEvents:
        currentText = values["-TEXTBOX-"]
        newText = currentText + " " + event
        window["-TEXTBOX-"].update(newText)

    if event == "Exit":
            window.close()


window.close()