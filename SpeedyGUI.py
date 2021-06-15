'''
    Program: GAS : Internet Speed Tester
    Author: Shashi Kumar
    GitHub: sbkshashi

	Read Me Before running
		1. All module should come with Python basic installation except speedtest.
		2. To install speedtest run 
			a. pip install speedtest_cli
		3. I have used Python3.9.2 64-bit

'''
##Required Imports
from tkinter import *
from speedtest import Speedtest

##Internet speed check function
def speed_check():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    ping = speed_test.results.ping
    isp = speed_test.results.client['isp']
    country = speed_test.results.client['country']
    ip = speed_test.results.client['ip']
    server = speed_test.results.server['sponsor']
    sever_location = speed_test.results.server['name']
    downlabel.config(text="Download Speed :- "+ str(download_speed) + "Mbps")
    uplabel.config(text="Upload Speed :- "+ str(upload_speed) + "Mbps")
    pinglabel.config(text="Ping Time :- "+ str(round(ping,0)) + "ms")
    isplabel.config(text="Network :- "+ str(isp))
    countrylabel.config(text="Country :- "+str(country))
    iplabel.config(text="IP Address :- "+ip)
    serverlabel.config(text="Test Server :- "+str(server))
    serverloclabel.config(text="Region :- "+ str(sever_location))

##Initialization of empty windows.
root = Tk()
root.title("GAS SPEED CHECKER")
root.geometry('305x385')
root.config(bg='blue')
root.resizable(False,False)

##Creating Canvas for Results
canvas = Canvas(root, width = 300, height = 385, bg = "black")
canvas.pack()
#img = PhotoImage(file='pic.png')
img = PhotoImage(file="C:\Temp\Python\InternetSpeed\pic.png")
canvas.create_image(0,0,anchor=NW,image=img)

##Button and label config 

Button = Button(root,text="GET YOUR SPEED", width=15,command=speed_check, bg="green")
Button.place(x=90,y=345)
downlabel = Label(root,text="shows Download Speed",width=25)
downlabel.place(x=60,y=275)
uplabel = Label(root,text="Shows Upload Speed",width=25)
uplabel.place(x=60,y=307)
iplabel = Label(root,text="IP Address",width=25)
iplabel.place(x=60,y=250)
pinglabel = Label(root,text="Ping time",width=25)
pinglabel.place(x=60,y=225)
isplabel = Label(root,text="Network",width=25)
isplabel.place(x=60,y=100)
serverlabel = Label(root,text="Test Server",width=25)
serverlabel.place(x=60,y=125)
countrylabel = Label(root,text="Country",width=25)
countrylabel.place(x=60,y=125)
serverloclabel = Label(root,text="Region",width=25)
serverloclabel.place(x=60,y=150)

root.mainloop()
