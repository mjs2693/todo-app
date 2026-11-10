import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
coose_button1 = sg.FileBrowse("Chose")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
coose_button2 = sg.FolderBrowse("Chose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1,input1,coose_button1],
                           [label2,input2,coose_button2],
                           [compress_button]])

window.read()
window.close()
