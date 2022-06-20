import tkinter as tk
import time
import os
import sys
import csv
import ctypes
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
files_directory = filedialog.askdirectory()

_start = time.time()
_files = 0
_lines = 0

for root, dirs, filenames in os.walk(files_directory):
        
    for f in filenames:
        
        _files += 1
        _files_perc = _files/len(filenames) * 100
        _lines = 0
        
        _end = time.time()
        _elapsed = (_end-_start)/60
        _eta = (_elapsed / _files) * (len(filenames) - _files)
        
        with open(files_directory + "/" + f,"r") as infile, open("join_files.txt","a") as outfile:

            for line in infile:
                
                _lines += 1               

                #write results to file
                outfile.write(text)

                _end = time.time()
                _elapsed = (_end-_start)/60

                _message = "\r%.2f%%" % _files_perc
                _message += " files, "
                _message += "%.0f" % _lines
                _message += " lines read, "
                _message += "%.2f" % _elapsed
                _message += " minutes passed, "
                _message += "%.2f" % _eta
                _message += " minutes estimated."
                sys.stdout.write(_message)
                sys.stdout.flush()
        
