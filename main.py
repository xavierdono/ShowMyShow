#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tk import
from tkinter import *
from tkinter.messagebox import *

# Class import
from Show import Show
from SQLManager import SQLManager
from APIShow import APIShow
from Helper import Helper

###############################
# DB
###############################
sql = SQLManager()
sql.create_db()

###############################
# Callback
###############################
def search(event):
    searchShow()


def searchShow():
    # Supprime les précédentes recherches
    for w in fraShow.winfo_children():
        w.destroy()
    
    api = APIShow()
    lstShow = api.search(nameShow.get())
    
    if lstShow == None:
        showwarning('Attention', 'Une erreur est survenue.')
        return
    
    for show in lstShow:
        global photo # Indispensable pour garder la référence à la photo
        photo = Helper.getImage(show)
       
        if photo != None:        
            canvas = Canvas(fraShow, width=150, height=150, bg='ivory')
            canvas.create_image(0, 0, anchor=NW, image=photo)
            canvas.pack()
        
        Label(fraShow,text=show.name).pack(side=LEFT,padx=10,pady=10)

###############################
# IHM
###############################
root = Tk()
root.title("Show my show!")
root.geometry("520x320+80+100")

groupSearch = LabelFrame(root, text="Search", padx=5, pady=5)
groupSearch.pack(padx=10, pady=10)

lblShow = Label(groupSearch, text = 'Show: ')
lblShow.pack(side = LEFT, padx = 5, pady = 5)

nameShow = StringVar()
txtShow = Entry(groupSearch, textvariable=nameShow, bg ='bisque', fg='maroon')
txtShow.bind('<Return>', search)
txtShow.focus_set()
txtShow.pack(side = LEFT, padx = 5, pady = 5)

btnSearch = Button(groupSearch, text='Search', command = searchShow)
btnSearch.pack(side = LEFT, padx = 5, pady = 5)

fraShow = Frame(root,borderwidth=2,relief=GROOVE)
fraShow.pack(side=LEFT,padx=10,pady=10)

root.mainloop()

sql.close_db()
