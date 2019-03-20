
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
from tkinter import scrolledtext ,Canvas, Frame, BOTH



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
    #time.sleep(10)
    w.itemconfig(app_rect, fill='white')
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

def clear_all():
    boot_text.delete(1.0,END)
    iap_text.delete(1.0,END)
    app_text.delete(1.0,END)



if __name__ == "__main__":

    """
    The main loop consists of all the GUI objects and its placement.

    The Main loop handles all the widget placements.

    """
    #frames
    frame_view_iap = Frame(height = 430, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 5)
    frame_view_boot = Frame(height = 430, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 438, y = 5)
    frame_view_app = Frame(height = 430, width = 440, bd = 3, relief = 'groove',bg="#808e95").place(x = 869, y = 5)
    frame_2 = Frame(height = 150, width = 860, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 558)

    #frame_4 = Frame(height = 150, width = 440, bd = 3, relief = 'groove').place(x = 869, y = 558)
    w = Canvas(gui, width=437.5, height=270,bg="#29434e")  # 808e95
    w.pack()
    w.create_text(260, 85,font=("freemono ", 11, "bold"),text = "BANK-2", anchor="nw", angle=90)
    w.create_text(260, 215,font=("freemono ", 11, "bold"),text = "BANK-1", anchor="nw", angle=90)

    #These will automatically be drawn on the already packed canvas
    w.place(x = 869, y = 436)
    bootPart1_rect = w.create_rectangle(280,240, 437.5, 270, fill='white')

    iap_rect = w.create_rectangle(280,200, 437.5, 240, fill='white')

    app_rect = w.create_rectangle(280,135, 437.5, 200, fill='white')



    bootPart2_rect = w.create_rectangle(280,115, 437.5, 135, fill='white')

    emul_rect = w.create_rectangle(280,113, 437.5, 115, fill='black')

    swap_rect = w.create_rectangle(280,50, 437.5, 113, fill='white')

    xfactory_rect = w.create_rectangle(280,2, 437.5, 50, fill='white')

    #label_bootPart1 = Label(text = "BootloaderP1",bg="#eeeeee").place(x =1192, y= 685)
    #label_iap = Label(text = "IAP",bg="#eeeeee").place(x =1220, y= 650)
    #data_app = Label(text = "Application",bg="#eeeeee").place(x =1193, y= 600)
    #data_bootPart2 = Label(text = "BootloaderP2",bg="#eeeeee").place(x =1192, y= 553.5)
    #data_swap = Label(text = "SWAP",bg="#eeeeee").place(x =1215, y= 510)
    #data_XFACTORY= Label(text = "XFactory",bg="#eeeeee").place(x =1200, y= 458)

    w.create_text(308, 249.5,font=("freemono ", 11, "bold"), text = "BootloaderP1", anchor="nw", angle=0)
    w.create_text(347, 215,font=("freemono ", 11, "bold"), text = "IAP", anchor="nw", angle=0)
    w.create_text(312, 157,font=("freemono ", 11, "bold"), text = "Application", anchor="nw", angle=0)
    w.create_text(308, 118,font=("freemono bold", 11, "bold"), text = "BootloaderP2", anchor="nw", angle=0)
    w.create_text(340, 73,font=("freemono ", 11, "bold"), text = "SWAP", anchor="nw", angle=0)
    w.create_text(320, 17,font=("freemono ", 11, "bold"), text = "XFactory", anchor="nw", angle=0)

    # 30, 10, 120, 80  Helvetica  'freemono bold'
    # 280, 350, 50, 150
    # text = Text(width = 65, height = 15)
    # text2 = Text(width = 65, height = 15)




    iap_text = scrolledtext.ScrolledText(gui,width=58,height=35)
    iap_text.grid(column=0,row=0)
    iap_text.place(x = 877, y = 10)

    app_text = scrolledtext.ScrolledText(gui,width=57,height=35)
    app_text.grid(column=0,row=0)
    app_text.place(x = 15, y = 10)

    boot_text = scrolledtext.ScrolledText(gui,width=57,height=35)
    boot_text.grid(column=0,row=0)
    boot_text.place(x = 446, y = 10)
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
    boot_indic = Label(text = "BOOTLOADER DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 555, y= 405)
    boot_indic = Label(text = "IAP DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 1035, y= 405)
    boot_indic = Label(text = "APPLICATION DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 100, y= 405)

    #contact = Label(text = "mastouri.rida@gmail.com").place(x = 250, y = 437)


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

    # clear_iap = Button(text = "Clear", command = clearIAP, width = 2,relief = 'ridge').place(x = 15, y = 405)
    # clear_app = Button(text = "Clear", command = clearAPP, width = 2,relief = 'ridge').place(x = 446, y = 405)
    # clear_boot = Button(text = "Clear", command = clearBOOT, width = 2,relief = 'ridge').place(x = 877, y = 405)

    # btn = Button(gui,text = "Clear", command =  lambda: iap_text.delete(1.0,END), width = 2,relief = 'ridge').place(x = 15, y = 405)
    # btn.pack()
    clear_app = Button(gui, text='Clear',width = 2,relief = 'ridge', command=lambda: app_text.delete(1.0,END))
    clear_app.pack()
    clear_app.place(x = 15, y = 405)

    clear_boot = Button(gui, text='Clear',width = 2,relief = 'ridge', command=lambda: boot_text.delete(1.0,END))
    clear_boot.pack()
    clear_boot.place(x = 446, y = 405)

    clear_iap = Button(gui, text='Clear',width = 2,relief = 'ridge', command=lambda: iap_text.delete(1.0,END))
    clear_iap.pack()
    clear_iap.place(x = 877, y = 405)

    clear_all = Button(gui, text='Clear All Window',width = 14,relief = 'ridge', command= clear_all)
    clear_all.pack()
    clear_all.place(x = 733, y = 565)
    #mainloop
    # master = Tk()
    # w = Spinbox(master, from_ = 0, to = 10)
    # w.pack()


    gui.geometry('1366x768')

    # canvas = Canvas(gui, width = 100, height = 100)
    # canvas.pack()
    # myrectangle = canvas.create_rectangle(100, 200, 400, 400, fill='black')
    # canvas.place(x = 15, y = 510)
    # canvas.itemconfig(myrectangle, fill='red')
    # gui.update()

    gui.mainloop()
