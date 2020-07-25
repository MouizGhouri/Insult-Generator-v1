import requests as request
import tkinter
import pyperclip

INSULT_API_GET = 'https://insult.mattbas.org/api/insult'

def getInsult () :

	NAME = input_box_entry.get ()

	if (len (NAME) > 0) :

		if ' ' in NAME :

			NAME_PARTS = NAME.split ()

			NAME = NAME_PARTS [0]

		NAME = '?who=' + NAME

	pyperclip.copy (request.get (INSULT_API_GET + NAME).text)

window = tkinter.Tk ()
window.geometry ('320x100')
window.title ('Insult Generator')

input_box_label = tkinter.Label (window, text="Name (Leave Empty for 'You'):").grid(row=0, column=0, padx=5, pady=10)

input_box_entry = tkinter.Entry (window)
input_box_entry.grid (row=0, column=2, padx=5, pady=10)

get_button = tkinter.Button (window, text='Copy New Insult', command = getInsult).grid (row=3, column=2, padx=10, pady=0)

window.mainloop ()
