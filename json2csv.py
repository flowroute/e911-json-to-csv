#!/usr/bin/env python

import json
import os
import requests
from Tkinter import Tk, Label, Button, Entry, StringVar
import tkMessageBox


class FR_GUI:
    def __init__(self, master):

        if os.getenv('FR_ACCESS_KEY') != '':
            userdefault = StringVar(master, value=os.getenv('FR_ACCESS_KEY'))

        if os.getenv('FR_SECRET_KEY') != '':
            passdefault = StringVar(master, value=os.getenv('FR_SECRET_KEY'))

        if os.getenv('FR_CSV_OUTPUT') != '':
            filedefault = StringVar(master, value=os.getenv('FR_CSV_OUTPUT'))

        self.master = master
        master.title("E911 CSV Output")

        self.label = Label(master, text="E911 CSV Output")
        self.label.grid(row=1, column=1, columnspan=2, pady=(0,20))

        usertext=Label(master, text="Username: ")
        usertext.grid(row=2, column=1, padx=(40,10))

        self.user_entry = Entry(master, textvariable=userdefault)
        self.user_entry.grid(row=2, column=2, padx=10, pady=5)

        passtext=Label(master, text="Password: ")
        passtext.grid(row=3, column=1, padx=(40,10))

        self.user_pass = Entry(master, textvariable=passdefault, show="*")
        self.user_pass.grid(row=3, column=2, padx=10, pady=5)

        filetext=Label(master, text="Output File: ")
        filetext.grid(row=4, column=1, padx=(40,10))

        self.output_file = Entry(master, textvariable=filedefault)
        self.output_file.grid(row=4, column=2, padx=10, pady=5)

        self.greet_button = Button(master, text="Write CSV", command=self.produce_csv)
        self.greet_button.grid(row=5, column=1, padx=(40,10), pady=20)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=5, column=2, pady=20)

    def produce_csv(self):
        data = json.loads(self.get_data())
        self.write_file(data)

    def get_data(self):

        user = self.user_entry.get()
        passwd = self.user_pass.get()
        uri = 'https://api.flowroute.com/v2/e911s'

        r = requests.get(uri, auth=(user,passwd))

        return r.content

    def write_file(self, data):

        fields = ['label','last_name','first_name','street_number','street_name','address_type','address_type_number','city','state','country','zip']

        f = open(self.output_file.get(), 'w')
        f.write("'ID'" + ',')
        for field in fields:
            f.write(field.replace("_", " ").title() + ',')
        f.write('\n')

        for line in data['data']:
            f.write("'" + line['id'] + "',")
            for field in fields:
                f.write("'" + line['attributes'][field] + "',")
            f.write('\n')
        f.close()

        tkMessageBox.showinfo("Information", "CSV file written.")

root = Tk()
fr_gui = FR_GUI(root)
root.wm_geometry("400x200")
root.mainloop()
