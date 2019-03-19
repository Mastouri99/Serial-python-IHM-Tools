
"""Serial IHM Tools for test and validation.
@author: myLinux <mastouri.rida@gmail.com>
"""

import time
import threading
import Queue
import Tkinter
import ttk
from Tkinter import *
import serial

from tkinter import scrolledtext



serial_data = ''
filter_data = ''
update_period = 5000
serial_object = None
gui = Tk()
gui.title("CARDIO DEVICE TEST")

gui.configure(bg='#102027')



def connect():

    version_ = button_var.get()
    print version_
    global serial_object
    port = port_entry.get()
    baud = baud_entry.get()



    try:
        if (version_ == 2)or(version_ == 3):
            try:
                serial_object = serial.Serial('/dev/tty' + str(port), baud,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=400)

            except:
                print "Cant Open Specified Port"
        elif version_ == 1:
            serial_object = serial.Serial('COM' + str(port), baud,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=100)

    except ValueError:
        print "Enter Baud and Port"
        return

    t1 = threading.Thread(target = get_data)
    t1.daemon = True
    t1.start()



def get_data():

    global serial_object
    global filter_data
    # text.place(x = 15, y = 10)
    # #text2.place(x = 505, y = 10)
    # progress_1.place(x = 60, y = 680)
    global file
    file = open("logiap1.txt", "w")
    while(1):
        try:
            filter_data = ''
            filter_data = serial_object.readline()
            print filter_data
            if filter_data:
                q.put(filter_data)
                #q.join()
                if '[IAP]' in filter_data :
                    iap_text.insert(END, filter_data)
                    iap_text.insert(END,"\n")
                    iap_text.yview_pickplace("end")


        except TypeError:
            pass




def update_gui():

    global filter_data
    global update_period
    global file

    file = open("logiap1.txt", "w")
    while(1):
        try:
            item = q.get()
            if item :
                file.write(item)

                file.flush()


        except :
            pass

def send():

    send_data = data_entry.get()

    if not send_data:
        print "Sent Nothing"

    serial_object.write(send_data)



def disconnect():
    global file
    try:
        serial_object.close()

    except AttributeError:
        print "Closed without Using it -_-"
    file.close()
    gui.quit()
def clear():
    iap_text.insert(END,"\n")


def grnCircle():

    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green')

    LEDLog.insert(0.0, "On\n")



def whtCircle():

    circleCanvas.create_oval(19, 19, 81, 81, width=0, fill='white')

    LEDLog.insert(0.0, "Off\n")


if __name__ == "__main__":

    """
    The main loop consists of all the GUI objects and its placement.

    The Main loop handles all the widget placements.

    """
    #frames
    frame_view_iap = Frame(height = 553, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 5)
    frame_view_boot = Frame(height = 553, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 438, y = 5)
    frame_view_app = Frame(height = 553, width = 440, bd = 3, relief = 'groove',bg="#808e95").place(x = 869, y = 5)
    frame_2 = Frame(height = 150, width = 860, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 558)
    #frame_3 = Frame(height = 150, width = 400, bd = 3, relief = 'groove',bg="#808e95").place(x = 410, y = 560)
    frame_4 = Frame(height = 150, width = 440, bd = 3, relief = 'groove').place(x = 869, y = 558)
    # text = Text(width = 65, height = 15)
    # text2 = Text(width = 65, height = 15)
    iap_text = scrolledtext.ScrolledText(gui,width=57,height=44)
    iap_text.grid(column=0,row=0)
    iap_text.place(x = 15, y = 10)

    boot_text = scrolledtext.ScrolledText(gui,width=57,height=44)
    boot_text.grid(column=0,row=0)
    boot_text.place(x = 446, y = 10)

    app_text = scrolledtext.ScrolledText(gui,width=58,height=44)
    app_text.grid(column=0,row=0)
    app_text.place(x = 877, y = 10)
    #threads
    q = Queue.Queue()
    t2 = threading.Thread(target = update_gui)
    t2.daemon = True
    t2.start()


    #Labels
    data1_ = Label(text = "Command:",bg="#808e95").place(x = 15, y= 660)
    osdata_ = Label(text ="OS :",bg="#808e95").place (x = 10, y = 570)
    setting = Label(text ="Advanced Setting",bg="#808e95").place (x = 420, y = 620)
    baud   = Label(text = "Baud",bg="#808e95").place(x = 100, y = 600)
    port   = Label(text = "Port",bg="#808e95").place(x = 200, y = 600)
    boot_indic = Label(text = "BOOTLOADER DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 80, y= 500)
    boot_indic = Label(text = "IAP DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 580, y= 500)
    boot_indic = Label(text = "APPLICATION DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 980, y= 500)
     # fg = "light green",
		#  bg = "dark green",
		#  font = "Helvetica 16 bold italic").pack()
    #contact = Label(text = "mastouri.rida@gmail.com").place(x = 250, y = 437)

    #progress_bars
    #progress_1 = ttk.Progressbar(orient = HORIZONTAL, mode = 'determinate', length = 200, max = 255)



    iap_text.place(x = 15, y = 10)
    #progress_1.place(x = 60, y = 680)
    #Entry
    data_entry = Entry(width = 41)
    data_entry.place(x = 100, y = 684)

    baud_entry = Entry(width = 10)
    baud_entry.place(x = 100, y = 624)

    port_entry = Entry(width = 10)
    port_entry.place(x = 200, y = 624)



    #radio button
    button_var = IntVar()
    radio_1 = Radiobutton(text = "Linux  ", variable = button_var, value = 2,bg="#808e95",relief = 'raised').place(x = 60, y = 570)
    radio_2 = Radiobutton(text = "Windows", variable = button_var, value = 1,bg="#808e95",relief = 'raised').place(x = 150, y = 570)
    radio_3 = Radiobutton(text = "Mac    ", variable = button_var, value = 3,bg="#808e95",relief = 'raised').place(x = 250, y = 570)

    radio_4 = Radiobutton(text = "Enable Logging ", variable = button_var, value = 4,bg="#808e95",relief = 'raised').place(x = 420, y = 570)
    all_debug = IntVar()
    Checkbutton(gui, text="All Debug", variable=all_debug,bg="#808e95",relief = 'raised').place(x = 420, y = 595)
    only_errors = IntVar()
    Checkbutton(gui, text="Only Errors", variable=only_errors,bg="#808e95",relief = 'raised').place(x = 550, y = 595)
    boot_logging = IntVar()
    Checkbutton(gui, text="Boot Logging", variable=boot_logging,bg="#808e95",relief = 'raised').place(x = 420, y = 650)
    iap_logging = IntVar()
    Checkbutton(gui, text="IAP Logging", variable=iap_logging,bg="#808e95",relief = 'raised').place(x = 550, y = 650)
    app_logging = IntVar()
    Checkbutton(gui, text="Application Logging", variable=app_logging,bg="#808e95",relief = 'raised').place(x = 675, y = 650)

    #button

    connect = Button(text = "Connect", command = connect,relief = 'ridge').place(x = 15, y = 620)
    disconnect = Button(text = "Disconnect", command = disconnect,relief = 'ridge').place(x =300, y = 620)
    button1 = Button(text = "Send", command = send, width = 6,relief = 'ridge').place(x = 15, y = 680)

    clear = Button(text = "Clear", command = clear, width = 4,relief = 'ridge').place(x = 15, y = 510)
    #mainloop
    # master = Tk()
    # w = Spinbox(master, from_ = 0, to = 10)
    # w.pack()

    gui.geometry('1366x768')


    gui.mainloop()
