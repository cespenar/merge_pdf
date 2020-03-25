#!/usr/bin/env python3

import argparse
import glob
import os
import sys
import PySimpleGUI as sg
from PyPDF2 import PdfFileMerger, PdfFileReader


def get_arguments(options=sys.argv[1:]):

    parser = argparse.ArgumentParser(conflict_handler="resolve", \
        description="Merge pdf files in a directory.")
    parser.add_argument("-i", "--input_dir", type=str, required=True, \
        help="The directory containing the files.")
    parser.add_argument("-o", "--output", type=str, required=True, \
        help="Output file.")
    parser.add_argument("-p", "--pattern", type=str, default="*.pdf", \
        help="The pattern for glob to select the files Default: \".pdf\".")
    args = parser.parse_args(options)
    return args


def merge_files(input_dir, pattern):

    merged_pdf = PdfFileMerger()
    for f_name in glob.glob(os.path.join(input_dir, pattern)):
        merged_pdf.append(PdfFileReader(f_name, "rb"))
    
    return merged_pdf
    

if __name__ == "__main__":

    # args = get_arguments()

    sg.theme("DarkAmber")	# Add a touch of color
    # All the stuff inside your window.
    layout = [ 
            # [sg.Text("Folder with PDF files to merge")],
            # [sg.FolderBrowse()],
            # [sg.Text("Output file")],
            # [sg.popup_get_file("Choose the output file", default_extension="pdf", save_as=True)],
            [sg.Text("Input folder", size=(12, 1)), sg.Input(), sg.FolderBrowse()],
            [sg.Text("Output file", size=(12, 1)), sg.Input(), sg.FileBrowse()],
            [sg.Button("Merge files"), sg.Button("Cancel")],
            ]

    # Create the Window
    window = sg.Window("Merge PDFs", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):	# if user closes window or clicks cancel
            break
        print('Values ', values[0], values[1])

    window.close()

    merged_pdf = merge_files(args.input_dir, args.pattern)
    # merged_pdf.write(args.output)
