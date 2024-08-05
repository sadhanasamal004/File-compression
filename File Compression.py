                        # PROJECT 3: FILE COMPRESSION

import tkinter as tk 
from compressmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title='Select a file')
    return filename

def compression(i,o):
    compress(i,o)

window=tk.Tk()
window.title('Compression engine')
window.geometry('400x400')

compress_button=tk.Button(window,text='Compress',command=lambda:compression(open_file(),'out2.txt'))
compress_button.grid(row=2,column=1,padx=5,pady=5)

window.mainloop()