# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 21:12:20 2021

@author: user
"""

import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter as tk
import pandas as pd
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases

# importing modules
from clean_text import *
from testing import *


window = tk.Tk()
width = int(window.winfo_screenwidth()*0.75)
height = int(window.winfo_screenheight()*0.95)
dimension = str(width)+"x"+str(height)

models = {
    "SGNS + CleanTrainSet + th=0.3":1,
    "SGNS + CleanTrainSet + th=0.5":2,
    "SGNS + CleanTrainSet + th=1":3,
    "SGNS + UnCleanTrainSet + th=0.3":4,
    "SGNS + UnCleanTrainSet + th=0.5":5,
    "SGNS + UnCleanTrainSet + th=1":6
    }
data = ()

def openFile():
    filepath = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    pathText.set(filepath)
    
def testPhraseDet():
    global data
    print(test_set_input.get(), configs.get())
    df = pd.read_csv(test_set_input.get())
    queries = df['pertanyaan'].values
    expected_phrase = df['label'].values
    
    # clean the data
    for record in output_table.get_children():
        output_table.delete(record)
        
    for record in summary_table.get_children():
        summary_table.delete(record)
        
        
    if models[configs.get()] == 1:
        data = model1(queries, expected_phrase)
    elif models[configs.get()] == 2:
        data = model2(queries, expected_phrase)
    elif models[configs.get()] == 3:
        data = model3(queries, expected_phrase)
    elif models[configs.get()] == 4:
        data = model4(queries, expected_phrase)
    elif models[configs.get()] == 5:
        data = model5(queries, expected_phrase)
    elif models[configs.get()] == 6:
        data = model6(queries, expected_phrase)
    exp_ph = det_ph = det_t = det_f = not_det = 0
    for i in range(0, len(data)):
        # ("Query", "Expected Phrase", "Detected Phrase", "N Expected", "Detected True", "Detected False", "Not Detected")
        exp_ph+=len(data[i][1])
        det_ph+=len(data[i][2])
        det_t+=data[i][4]
        det_f+=data[i][5]
        not_det+=data[i][6]
        output_table.insert(parent='', index='end', iid=i, text="", values=data[i])
    
    # ("Total Queries","N Expected", "Phrase Detected",  "Detected True", "Detected False", "Not Detected")
    summ = ((len(queries)), exp_ph, det_ph, det_t, det_f, not_det)
    summary_table.insert(parent='', index='end', iid=i, text="", values=summ)
    # df.to_csv('output.csv')
    # print("exported")

# def exportToCSV(data):
    # target = open('results.csv', 'w')
    # for line in data:
    #     for attr in data:
    #         target.write("\""+attr+"\""+",")
    
    
# set window label and main frame
window.title("PBA Final Assignment - Indonesian Phrase Detector using GENSIM [Group 3]")
input_frame = tk.Frame(master=window, width=(width*0.8))
config_frame = tk.Frame(master=window, width=(width*0.8))
output_frame = tk.Frame(master=window, width=(width*0.8))


# set label Path file
test_set_label = tk.Label(master=window, text="Dataset Test Path")
test_set_label.pack(anchor=W, padx=20, pady=5)

# set entry field (a line only)
pathText = tk.StringVar()
test_set_input = tk.Entry(master=input_frame, width=150, textvariable=pathText)
test_set_input.pack(side=LEFT, fill=BOTH, padx=20)

# set button open file
openfile_btn = tk.Button(master=input_frame, text="Open CSV File", width=15, command=openFile)
openfile_btn.pack(fill=BOTH)

input_frame.pack(anchor=W, pady=5)

# set label configurations selection
configs_label = tk.Label(master=config_frame, text="Choose Configuration")
configs_label.pack(anchor=W)

# set dropdown to choose model+its configuration
OPTIONS=[
    "SGNS + CleanTrainSet + th=0.3",
    "SGNS + CleanTrainSet + th=0.5",
    "SGNS + CleanTrainSet + th=1",
    "SGNS + UnCleanTrainSet + th=0.3",
    "SGNS + UnCleanTrainSet + th=0.5",
    "SGNS + UnCleanTrainSet + th=1"
    ]
configs = tk.StringVar(config_frame)
configs.set("Choose Configuration Here")

chosen_config = tk.OptionMenu(config_frame, configs,*OPTIONS, )
chosen_config.config(width=145)
chosen_config.pack(side=LEFT, fill=BOTH)

# set button run test
test_btn = tk.Button(master=config_frame, text="Run the Test", width=15, command=testPhraseDet)
test_btn.pack(fill=BOTH, padx=20)

config_frame.pack(anchor=W, padx=20, pady=5)

# output site
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', pady=10)

# set label output phrase detector
output_label = tk.Label(master=output_frame, text="Results")
output_label.pack(anchor=W, pady=5)

# scrollbar for table
vsb = ttk.Scrollbar(output_frame, orient="vertical")
hsb = ttk.Scrollbar(output_frame, orient="horizontal")
vsb.pack(side=RIGHT, fill=Y)
hsb.pack(side=BOTTOM, fill=X)

# set tree view widgets
output_table = ttk.Treeview(master=output_frame, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
style = ttk.Style()
style.configure("Treeview",
                rowheight=30
                )

vsb.config(command=output_table.yview)
hsb.config(command=output_table.xview)
# define column
output_table['columns'] = ("Query", "Expected Phrase", "Detected Phrase", "N Expected", "Detected True", "Detected False", "Not Detected")

# formate the columns
output_table.column("#0", anchor=W, width=0, stretch=NO)
output_table.column("Query", anchor=W, width=700)
output_table.column("Expected Phrase", anchor=W, width=300)
output_table.column("Detected Phrase", anchor=W, width=300)
output_table.column("N Expected", anchor=CENTER, width=125)
output_table.column("Detected True", anchor=CENTER, width=125)
output_table.column("Detected False", anchor=CENTER, width=125)
output_table.column("Not Detected", anchor=CENTER, width=115)

# create headings
output_table.heading("#0", anchor=W, text="")
output_table.heading("Query", anchor=W, text="Query")
output_table.heading("Expected Phrase", anchor=W, text="Expected Phrase")
output_table.heading("Detected Phrase", anchor=W, text="Detected Phrase")
output_table.heading("N Expected", anchor=CENTER, text="N Expected")
output_table.heading("Detected True", anchor=CENTER, text="Detected True")
output_table.heading("Detected False", anchor=CENTER, text="Detected False")
output_table.heading("Not Detected", anchor=CENTER, text="Not Detected")

# data = ("Apakah frasa itu?", "frasa", "frasa", 1, 1, 0, 0)
#insert data
# for i in range (0,24):
#     output_table.insert(parent='', index='end', iid=i, text="", values=data)

output_table.pack()
output_frame.pack(anchor=W, padx=20, pady=5)

# table summary
summary_table = ttk.Treeview(master=window)
summary_table['columns'] = ("Total Queries","N Expected", "Phrase Detected",  "Detected True", "Detected False", "Not Detected")

summary_table.column("#0", anchor=W, width=0, stretch=NO)
summary_table.column("Total Queries", anchor=CENTER, width=125)
summary_table.column("N Expected", anchor=CENTER, width=125)
summary_table.column("Phrase Detected", anchor=CENTER, width=125)
summary_table.column("Detected True", anchor=CENTER, width=125)
summary_table.column("Detected False", anchor=CENTER, width=125)
summary_table.column("Not Detected", anchor=CENTER, width=115)

summary_table.heading("#0", anchor=W, text="")
summary_table.heading("Total Queries", anchor=CENTER, text="Total Queries")
summary_table.heading("N Expected", anchor=CENTER, text="N Expected")
summary_table.heading("Phrase Detected", anchor=CENTER, text="Phrase Detected")
summary_table.heading("Detected True", anchor=CENTER, text="Detected True")
summary_table.heading("Detected False", anchor=CENTER, text="Detected False")
summary_table.heading("Not Detected", anchor=CENTER, text="Not Detected")

summary_table.pack(pady=10)
# export and close button
export_btn = tk.Button(master=window, text="Export Result to CSV", command=lambda: exportToCSV())
export_btn.pack(ipadx=10, pady=5)

# button exit right
exit_btn = tk.Button(master=window, text="Exit", command=window.destroy, width=15)
exit_btn.pack(pady=5)


window.geometry(dimension)
window.mainloop()