from tkinter import *
from PIL import ImageGrab
from Predict import predict
import Input
import time
import webbrowser
import os
import subprocess

current_x,current_y = 0,0
mouse=False

def locate_xy(event):
    global current_x,current_y
    current_x,current_y = event.x,event.y
    
def addLine(event):
    global mouse
    mouse=True
    global current_x,current_y
    canvas.create_line((current_x+1,current_y+1,event.x+1,event.y+1),width=50,smooth=True)
    canvas.create_line((current_x+3,current_y+3,event.x+3,event.y+3),width=50,smooth=True)
    canvas.create_line((current_x+2,current_y+2,event.x+2,event.y+2),width=50,smooth=True)
    canvas.create_line((current_x+4,current_y+4,event.x+4,event.y+4),width=50,smooth=True)
    canvas.create_line((current_x+5,current_y+5,event.x+5,event.y+5),width=50,smooth=True)
    canvas.create_line((current_x+6,current_y+6,event.x+6,event.y+6),width=50,smooth=True)
    canvas.create_line((current_x+7,current_y+7,event.x+7,event.y+7),width=50,smooth=True)
    canvas.create_line((current_x+8,current_y+8,event.x+8,event.y+8),width=50,smooth=True)
    canvas.create_line((current_x+9,current_y+9,event.x+9,event.y+9),width=50,smooth=True)
    current_x=event.x
    current_y=event.y
    
def imported_drawing():
    global drawing,mouse
    mouse=False
    prev_x,prev_y = drawing[0][0],drawing[0][1]
    for i in drawing:
        new_x = i[0]
        new_y = i[1]
        canvas.create_line((prev_x+1,prev_y+51,new_x+1,new_y+51),width=50,smooth=True)
        canvas.create_line((prev_x+3,prev_y+53,new_x+3,new_y+53),width=50,smooth=True)
        canvas.create_line((prev_x+2,prev_y+52,new_x+2,new_y+52),width=50,smooth=True)
        canvas.create_line((prev_x+4,prev_y+54,new_x+4,new_y+54),width=50,smooth=True)
        canvas.create_line((prev_x+5,prev_y+55,new_x+5,new_y+55),width=50,smooth=True)
        canvas.create_line((prev_x+6,prev_y+56,new_x+6,new_y+56),width=50,smooth=True)
        canvas.create_line((prev_x+7,prev_y+57,new_x+7,new_y+57),width=50,smooth=True)
        canvas.create_line((prev_x+8,prev_y+58,new_x+8,new_y+58),width=50,smooth=True)
        canvas.create_line((prev_x+9,prev_y+59,new_x+9,new_y+59),width=50,smooth=True)
        prev_x = new_x
        prev_y = new_y
        
        
    
    
def clear(event):
    canvas.delete('all')



def save_and_predict(event):
    global mouse
    ImageGrab.grab().crop((50,50,900,900)).save("pred.jpg")
    prediction = brain.driver(mouse)
    print("The prediction is : ",prediction)
    if prediction=='G':
        webbrowser.open_new_tab('http://www.google.co.in')
    if prediction=='C':
        os.startfile('C:\Windows\System32\cmd.exe')
    if prediction=='S':
        subprocess.Popen(r'explorer /select,"C:\Studies"')
    if prediction=='P':
        os.startfile('C:\Windows\system32\mspaint.exe')
    if prediction=='W':
        webbrowser.open_new_tab('http://www.wikipedia.com')
    if prediction=='Y':
        webbrowser.open_new_tab('http://www.Youtube.com')
    if prediction=='E':
        webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
    
    
    
        
    
def openCamera(event):
    global drawing
    drawing = Input.main()
    imported_drawing()



drawing = Input.main()
brain = predict()



window = Tk()
window.title("Digit Recognition")
window.state("zoomed")

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)


canvas = Canvas(window,bg='White')
canvas.grid(row=0,column=0,sticky='nsew')



canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)

window.bind('<BackSpace>',clear)
window.bind('<Return>',save_and_predict)
window.bind('<space>',openCamera)
imported_drawing()

window.mainloop()





