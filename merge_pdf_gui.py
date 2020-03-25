#!/usr/bin/env python3

import glob
import os
import PySimpleGUI as sg
from PyPDF2 import PdfFileMerger, PdfFileReader


def merge_files(input_dir):

    merged_pdf = PdfFileMerger()
    for f_name in glob.glob(os.path.join(input_dir, "*.pdf")):
        merged_pdf.append(PdfFileReader(f_name, "rb"))
    
    return merged_pdf
    

if __name__ == "__main__":

 
    sg.theme("System Default 1")
    
    layout = [ 
            [sg.Text("Input folder", size=(12, 1)), sg.Input(),
                sg.FolderBrowse(initial_folder=os.getcwd(), key="input", tooltip="Select folder containing pdf files for merging.")],
            [sg.Text("Output file", size=(12, 1)), sg.Input(),
                sg.FileSaveAs(file_types=(("PDF", "*.pdf"),), initial_folder=os.getcwd(), key="output", tooltip="Select the output file.")],
            [sg.Button("Merge files", key="button_merge", tooltip="Merge selected files"), sg.Cancel(tooltip="Cancel")],
            ]

    window = sg.Window("Merge PDFs", layout)
    
    while True:
        event, values = window.read()
        print(values)
        if event == "button_merge":
            if not values["input"] or not values["output"]:
                sg.popup("You need to choose both input folder and output file!", title="Warning!")
            else:
                merged_pdf = merge_files(values["input"])
                merged_pdf.write(values["output"])
                sg.popup("Files have been merged!", title="Success!")
                break
        if event in (None, "Cancel"):
            break

    window.close()
