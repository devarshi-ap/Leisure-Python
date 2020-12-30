# import py gui and os modules
import PySimpleGUI as psg
import os.path


# Window layout; 2 columns.
# Left column takes input and Right column shows picture

left_file_column = [
    [
        psg.Text("Image Folder"),
        psg.In(size=(25, 1), enable_events=True, key="folder"),
        psg.FolderBrowse(button_color='white on navy'),
    ],
    [
        psg.Listbox(values=[], size=(44, 20), enable_events=True, key="file list")
    ],
]


# Right column will show a message until the user chooses the image file. Then displays the file

right_image_column = [
    [psg.Text("* Click on 'browse' and select a folder."
              "\n* Then you'll be shown a list of contents."
              "\n* Select image to view"
              "\n\n ...or copy paste the folder path into the text box")],
    [psg.Text(size=(40,1), key="message")],
    [psg.Image(key="image")],
]


# -------- Overall Layout --------

full_layout = [
    [
        psg.Column(left_file_column),
        psg.VSeparator(),
        psg.Column(right_image_column),
    ]
]


# create window when program is run
window = psg.Window("Image Viewer Program", full_layout)

# Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == psg.WIN_CLOSED:
        break

    if event == "folder":
        folder = values["folder"]
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        file_names = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".png", ".gif"))
        ]

        # displays the list of files in the folder provided
        window["file list"].update(file_names)

    # when the user selects a file from the list of files from chosen folder
    elif event == "file list":
        fname = os.path.join(values["folder"], values["file list"][0])

        # displays the image (replaces the message)
        window["message"].update(fname)
        window["image"].update(filename=fname)


# close window object
window.close()
