#!/usr/bin/env python3
""" 
Camera viewer
"""
import tkinter as tk
from tkinter import ttk
import vlc

ip = '192.168.1.42:554'
user = 'rtspuser'
upass = 'video554'
vpreview = "/ch%d/1"
vfullview = "/ch%d/0"
previewWidth=432
previewHeight=320
sepWidth = 2

baseurl = 'rtsp://' + user + ':' + upass + '@' + ip
class viewer :
    def __init__ (self,frame,streamURL) :
        args = ['--no-audio', '--no-osd', '--no-xlib']
        self.instance = vlc.Instance(args)
        self.player = self.instance.media_player_new()
        m = self.instance.media_new(streamURL)
        self.player.set_media(m)
        self.player.set_xwindow(frame.winfo_id())
        self.player.play()

def guiExit() :
    exit()

def genWindow(rootWindow,width,height,place_x,place_y) :
    win = tk.Canvas(rootWindow,bg='black',height=height,width=width)
    win.place(x=place_x,y=place_y,height=height,width=width)
    #win.pack()
    return(win)

if __name__ == '__main__'  :
    rootCanvas = tk.Tk()
    screenWidth = rootCanvas.winfo_screenwidth()
    screenHeight = rootCanvas.winfo_screenheight()
    print ("width = %d height = %d" % (screenWidth,screenHeight))
    rootCanvas.title =" Camera View"
    rootCanvas.geometry("%dx%d" %(screenWidth, screenHeight))
    exitButton = tk.Button(rootCanvas,text="Exit",command=guiExit, bg='orange',fg='black')
    exitButton.place(x=screenWidth-60,y=screenHeight-150)
    w3 = (screenWidth - (sepWidth*2))/3
    h3 = (screenHeight - (sepWidth*2))/3
    if((h3 > previewHeight) and (w3 > previewWidth)) :
        ww = w3
        wh = h3
        chNum = vfullview
    else:
        ww=previewWidth
        wh=previewH
        chNum = vpreview
    ox = 0 #sepWidth
    oy = 0 #sepWidth
    r = 0
    c = 0
    for ch in range(8) :
        x = ox + c * (ox +  ww)
        y = oy + r * (oy +  wh)
        c += 1 
        print("ch = %d:: x+ww =%d  screen Width = %d x = %d, y = %d  ww = %d" %((ch+1) ,(x+ww), screenWidth, x, y, ww)) 
        if ((x + ww) > screenWidth) :
            c = 0
            r += 1
            y = oy + r * (oy +  wh)
            x = ox + c * (ox +  ww)
            print("move to: ch = %d:: x+ww =%d  screen Width = %d x = %d y = %d ww = %d" %((ch+1) ,(x+ww), screenWidth, x, y, ww)) 
            c += 1 
        pane = genWindow(rootCanvas,ww,wh,x,y)
        url = baseurl + chNum % (ch+1)
        print(url)
        view = viewer(pane,url)
        
    rootCanvas.mainloop()
    
