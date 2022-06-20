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

#For new tags insert in both arrays
tags = [["1",       #Account
        "11",       #ClOrdID
        "17",       #ExecId
        "19",       #ExecRefId
        "20",       #ExecTransType
        "21",       #HandInst
        "31",       #LastPx
        "32",       #LastQty
        "35",       #MsgType
        "37",       #OrderID
        "38",       #OrderQty
        "39",       #OrdStatus
        "40",       #OrdType        
        "41",       #OrigClOrdID
        "44",       #Price
        "49",       #SenderCompID
        "50",       #SenderSubID
        "52",       #SendingTime
        "54",       #Side
        "55",       #Symbol
        "56",       #TargetCompID
        "57",       #TargetSubID
        "58",       #Text
        "59",       #TimeInForce
        "60",       #TransactTime
        "75",       #TradeDate
        "128",      #DeliverToCompID
        "150",      #ExecType
        "151",      #LeavesQty
        "198",      #SecondaryOrderID
        "448",      #PartyID_1
        "448",      #PartyID_2
        "448",      #PartyID_3
        "448",      #PartyID_4
        "448",      #PartyID_5
        "452",      #PartyRole_1
        "452",      #PartyRole_2
        "452",      #PartyRole_3
        "452",      #PartyRole_4
        "452",      #PartyRole_5
        "5149",     #UserAPAMA
        "5205",     #Tool
        "5220",     #System
        "5231",     #User        
        "5233",     #IP_1
        "5239",     #IP_2
        "6032",     #TradeId
        "10072"],   #ClientUser
        ["Account",
         "ClOrdID",
         "ExecId",
         "ExecRefId",
         "ExecTransType",
         "HandInst",
         "LastPx",
         "LastQty",
         "MsgType",
         "OrderID",
         "OrderQty",
         "OrdStatus",
         "OrdType",
         "OrigClOrdID",
         "Price",
         "SenderCompID",
         "SenderSubID",
         "SendingTime",
         "Side",
         "Symbol",
         "TargetCompID",
         "TargetSubID",
         "Text",
         "TimeInForce",
         "TransactTime",
         "TradeDate",
         "DeliverToCompID",
         "ExecType",
         "LeavesQty",
         "SecondaryOrderID",
         "PartyID_1",
         "PartyID_2",
         "PartyID_3",
         "PartyID_4",
         "PartyID_5",
         "PartyRole_1",
         "PartyRole_2",
         "PartyRole_3",
         "PartyRole_4",
         "PartyRole_5",
         "UserAPAMA",
         "Tool",
         "System",
         "User",
         "IP_1",
         "IP_2",
         "TradeId",
         "ClientUser"]]

for root, dirs, filenames in os.walk(files_directory):
    
    text_output = ""
    
    with open("fix_to_excel.tab","w") as outfile:
        for column in tags[1]:
            text_output += column + "\t"

        outfile.write(text_output + "\n")
    
    for f in filenames:
        
        _files += 1
        _files_perc = _files/len(filenames) * 100
        _lines = 0
        
        _end = time.time()
        _elapsed = (_end-_start)/60
        _eta = (_elapsed / _files) * (len(filenames) - _files)
        
        with open(files_directory + "/" + f,"r") as infile, open("fix_to_excel.tab","a") as outfile:

            for line in infile:
                
                _lines += 1

                text = line

                if "\x01" in text:
                    brk = "\x01"
                elif "|" in text:
                    brk = "|"
                elif "\x09" in text:
                    brk = "\x09"
                elif "~" in text:
                    brk = "~"
                elif "," in text:
                    brk = ","
                elif ";" in text:
                    brk = ";"
                else:
                    brk = ""

                text_output = ""
                tag_dupl_count = 0

                if (brk + "1" + "=") in text:

                    for tag in tags[0]:
                        
                        dlm = brk + tag + "="
                        if (dlm) in text:                            
                            text_ini = text.find("=",text.find(dlm)) + 1
                            text_end = text.find(brk,text_ini)
                            text_slice = text[text_ini:text_end]

                            if tag == "20":
                                if text_slice == "0":
                                    text_slice = "New"
                                elif text_slice == "1":
                                    text_slice = "Cancel"
                                elif text_slice == "2":
                                    text_slice = "Correct"
                                elif text_slice == "3":
                                    text_slice = "Status"

                            if tag == "21":
                                if text_slice == "1":
                                    text_slice = "Automated execution order, private, no broker intervention"
                                elif text_slice == "2":
                                    text_slice = "Automated execution order, public, broker intervention ok"
                                elif text_slice == "3":
                                    text_slice = "Manual order, best execution"

                            if tag == "31":
                                text_slice = float(text_slice)
                                text_slice = str(text_slice)
                                text_slice = text_slice.replace(".",",")

                            if tag == "32":
                                text_slice = float(text_slice)
                                text_slice = str(text_slice)
                                text_slice = text_slice.replace(".",",")

                            if tag == "38":
                                text_slice = float(text_slice)
                                text_slice = str(text_slice)
                                text_slice = text_slice.replace(".",",")

                            if tag == "39":
                                if text_slice == "0":
                                    text_slice = "New"
                                elif text_slice == "1":
                                    text_slice = "Partial fill"
                                elif text_slice == "2":
                                    text_slice = "Fill"
                                elif text_slice == "3":
                                    text_slice = "Done for day"
                                elif text_slice == "4":
                                    text_slice = "Canceled"
                                elif text_slice == "5":
                                    text_slice = "Replaced"
                                elif text_slice == "6":
                                    text_slice = "Pending Cancel"
                                elif text_slice == "7":
                                    text_slice = "Stopped"
                                elif text_slice == "8":
                                    text_slice = "Rejected"
                                elif text_slice == "9":
                                    text_slice = "Suspended"
                                elif text_slice == "A":
                                    text_slice = "Pending new"
                                elif text_slice == "B":
                                    text_slice = "Calculated"
                                elif text_slice == "C":
                                    text_slice = "Expired"
                                elif text_slice == "D":
                                    text_slice = "Accepted for bidding"
                                elif text_slice == "E":
                                    text_slice = "Pending Replace"

                            if tag == "40":
                                if text_slice == "1":
                                    text_slice = "Market"
                                elif text_slice == "2":
                                    text_slice = "Limit"
                                elif text_slice == "3":
                                    text_slice = "Stop"
                                elif text_slice == "4":
                                    text_slice = "Stop Limit"
                                elif text_slice == "K":
                                    text_slice = "Mkt Leftover"                               
                                    
                            if tag == "44":
                                text_slice = float(text_slice)
                                text_slice = str(text_slice)
                                text_slice = text_slice.replace(".",",")

                            if tag == "52":
                                text_slice = text_slice.replace(".",",")
                                text_slice = text_slice.replace("-"," ")
                                x1 = text_slice[0:4]
                                x2 = text_slice[4:6]
                                x3 = text_slice[6:8]
                                x4 = text_slice[9:]
                                text_slice = x1 + "/" + x2 + "/" + x3 + " " + x4

                            if tag == "54":
                                if text_slice == "1":
                                    text_slice = "Buy"
                                elif text_slice == "2":
                                    text_slice = "Sell"
                                elif text_slice == "3":
                                    text_slice = "Buy minus"
                                elif text_slice == "4":
                                    text_slice = "Sell plus"
                                elif text_slice == "5":
                                    text_slice = "Sell short"
                                elif text_slice == "6":
                                    text_slice = "Sell short exempt"
                                elif text_slice == "7":
                                    text_slice = "Undisclosed"
                                elif text_slice == "8":
                                    text_slice = "Cross"
                                elif text_slice == "9":
                                    text_slice = "Cross short"

                            if tag == "59":
                                if text_slice == "0":
                                    text_slice = "Day"
                                elif text_slice == "1":
                                    text_slice = "Good Till Cancel"
                                elif text_slice == "3":
                                    text_slice = "Immediate Or Cancel(IOC)/Fill And Kill (FAK)"
                                elif text_slice == "4":
                                    text_slice = "Fill Or Kill (FOK)/All Or Nothing (AON)"
                                elif text_slice == "6":
                                    text_slice = "Good Till Date (GTD)"
                                elif text_slice == "7":
                                    text_slice = "At the Close"
                                elif text_slice == "A":
                                    text_slice = "Good For Auction (GFA)"

                            if tag == "60":
                                text_slice = text_slice.replace(".",",")
                                text_slice = text_slice.replace("-"," ")
                                x1 = text_slice[0:4]
                                x2 = text_slice[4:6]
                                x3 = text_slice[6:8]
                                x4 = text_slice[9:]
                                text_slice = x1 + "/" + x2 + "/" + x3 + " " + x4

                            if tag == "150":
                                if text_slice == "0":
                                    text_slice = "New"
                                elif text_slice == "1":
                                    text_slice = "Partial fill"
                                elif text_slice == "2":
                                    text_slice = "Fill"
                                elif text_slice == "3":
                                    text_slice = "Done for day"
                                elif text_slice == "4":
                                    text_slice = "Canceled"
                                elif text_slice == "5":
                                    text_slice = "Replaced"
                                elif text_slice == "6":
                                    text_slice = "Pending Cancel"
                                elif text_slice == "7":
                                    text_slice = "Stopped"
                                elif text_slice == "8":
                                    text_slice = "Rejected"
                                elif text_slice == "9":
                                    text_slice = "Suspended"
                                elif text_slice == "A":
                                    text_slice = "Pending new"
                                elif text_slice == "B":
                                    text_slice = "Calculated"
                                elif text_slice == "C":
                                    text_slice = "Expired"
                                elif text_slice == "D":
                                    text_slice = "Restarted"
                                elif text_slice == "E":
                                    text_slice = "Pending Replace"
                                elif text_slice == "F":
                                    text_slice = "Trade"
                                elif text_slice == "H":
                                    text_slice = "Trade Cancel"

                            if tag == "151":
                                text_slice = float(text_slice)
                                text_slice = str(text_slice)
                                text_slice = text_slice.replace(".",",")

                            #Stores first two values. Third value is added at the end with default
                            if tag == "448" or tag == "452":                            
                                tag_dupl_count += 1

                                if tag_dupl_count > 5:
                                    tag_dupl_count = 1
                                
                                text_ini_first = text_ini                                
                                    
                                for x in range(1,tag_dupl_count):

                                    text_ini = text.find("=",text.find(dlm,text_end)) + 1
                                    text_end = text.find(brk,text_ini)
                                    
                                if text_ini >= text_ini_first:
                                    text_slice = text[text_ini:text_end]                                                               

                            #concatenate results
                            text_output += text_slice
                            
                        #add tab even if not found
                        text_output += "\t"

                    #write results to file
                    outfile.write(text_output + "\n")

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
