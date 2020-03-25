#!/usr/bin/env python3

import argparse
import glob
import os
import sys
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

    args = get_arguments()

    merged_pdf = merge_files(args.input_dir, args.pattern)
    merged_pdf.write(args.output)
