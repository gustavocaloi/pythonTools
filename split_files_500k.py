import tkinter as tk
import time
import os
import sys
import csv
import ctypes
import sys
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
        _split = 1

        _end = time.time()
        _elapsed = (_end-_start)/60
        _eta = (_elapsed / _files) * (len(filenames) - _files)

        outfile = open("output_file_"+str(_files)+"_split_"+str(_split)+".txt","a")
        
        with open(files_directory + "/" + f,"r") as infile:
            for line in infile:
                
                _lines += 1

                if _lines/_split == 500000:
                    _split += 1
                    outfile.close
                    outfile = open("output_file_"+str(_files)+"_split_"+str(_split)+".txt","a")

                try:
                    outfile.write(line)
                except:
                    e = sys.exc_info()[0]
                    err_file = open("error_file_"+str(_files)+"_split_"+str(_split)+".txt","a")
                    err_file.close
                    pass

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
                #sys.stdout.write(_message)
                #sys.stdout.flush()




        
