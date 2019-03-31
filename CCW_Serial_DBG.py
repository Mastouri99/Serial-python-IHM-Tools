
"""
@file  :  CCW_Serial_DBG.py
@brief :  Serial IHM Tools for test and validation.
 ###### myLinux <mastouri.rida@gmail.com> ######
@AUTHOR :    Ridha MASTOURI       START DATE :    19 Mar 2019
@version : 1.0.0
@Control Version : Linux Local Git
"""


import time
import threading
import Queue
import Tkinter
import ttk
from Tkinter import *
import serial
from tkinter import scrolledtext ,Canvas, Frame, BOTH
import datetime
import os
import tkinter.messagebox
import os
repeat = 0
senario = 0
myrepeat_2 = 0
path = os.getcwd()+'/Cardio Device History Log/'+'CCW-'+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#path = os.getcwd()
Enable_dgb = 'NO'
__all_dbg = 'NO'
__error_dbg = 'NO'
__iap_dbg = 'NO'
__app_dbg = 'NO'
__boot_dbg = 'NO'
__scner_dbg = 'NO'
__error_display = 'NO'
serial_check='no'
# define the access rights
access_rights = 0o755
BaudRates = [110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200,28800, 38400,56000, 57600, 115200, 128000,153600,230400,256000 ,460800,921600]

serial_data = ''
serial_object = None
gui = Tk()
gui.title("CARDIO DEVICE TEST TOOLS")
gui.configure(bg='#102027')
dead = 'true'


def playing_protection():
    w.itemconfig(bootPart1_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(bootPart1_rect, fill='white')
    w.itemconfig(iap_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(iap_rect, fill='white')
    w.itemconfig(app_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(app_rect, fill='white')
    w.itemconfig(bootPart2_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(bootPart2_rect, fill='white')
    w.itemconfig(swap_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(swap_rect, fill='white')
    w.itemconfig(xfactory_rect, fill='#4f83cc')
    gui.update()
    time.sleep(0.05)
    w.itemconfig(bootPart1_rect, fill='white')
    w.itemconfig(iap_rect, fill='white')
    w.itemconfig(app_rect, fill='white')
    w.itemconfig(bootPart2_rect, fill='white')
    w.itemconfig(swap_rect, fill='white')
    w.itemconfig(xfactory_rect, fill='white')
    gui.update()

def rervers_txt():
    w.itemconfig(txt1, fill='white')
    w.itemconfig(txt2, fill='white')
    w.itemconfig(txt3, fill='white')
    w.itemconfig(txt4, fill='white')
    w.itemconfig(txt5, fill='white')
    w.itemconfig(txt6, fill='white')

def protection_modeA():
    w.itemconfig(bootPart1_rect, fill='red')
    w.itemconfig(iap_rect, fill='red')
    w.itemconfig(app_rect, fill='red')
    w.itemconfig(bootPart2_rect, fill='red')
    w.itemconfig(swap_rect, fill='#00BF32')
    w.itemconfig(xfactory_rect, fill='#00BF32')
    rervers_txt()
    gui.update()


def protection_modeB():
    w.itemconfig(bootPart1_rect, fill='red')
    w.itemconfig(iap_rect, fill='red')
    w.itemconfig(app_rect, fill='#00BF32')
    w.itemconfig(bootPart2_rect, fill='red')
    w.itemconfig(swap_rect, fill='#00BF32')
    w.itemconfig(xfactory_rect, fill='red')
    rervers_txt()
    gui.update()

def shwo_connect():
    i = 0
    while i<4 :
        i +=1
        playing_protection()
    S4.itemconfig(s4_rect, fill='#00BF32')
    show_id()

def show_id():
    Label(text = "       INFO  ",bg="#29434e",foreground="white").place(x = 875, y= 445)
    Label(text = "Product    : STM32L4A6RG",bg="#29434e",foreground="white").place(x = 875, y= 460)
    Label(text = "Flash size : 1MB",bg="#29434e",foreground="white").place(x = 875, y= 475)
    Label(text = "RAM size   : 320 KB",bg="#29434e",foreground="white").place(x = 875, y= 490)
    Label(text = "NB Bank    : 2",bg="#29434e",foreground="white").place(x = 875, y= 505)
    Label(text = "NB Page    : 256 per Bank",bg="#29434e",foreground="white").place(x = 875, y= 520)
    Label(text = "Size Page  : 2 KB",bg="#29434e",foreground="white").place(x = 875, y= 535)
    Label(text = "CORE       : Cortex M4",bg="#29434e",foreground="white").place(x = 875, y= 550)
    Label(text = "Over Clock : 80 MHZ",bg="#29434e",foreground="white").place(x = 875, y= 565)

    Label(text = "       NOTE",bg="#29434e",foreground="white").place(x = 875, y= 590)
    Label(text = "This is the code color of the WRP ",bg="#29434e",foreground="white").place(x = 875, y= 605)
    Label(text = "memory protection visualisation>> ",bg="#29434e",foreground="white").place(x = 875, y= 620)
    Label(text = "WHITE  : Device is not connected ",bg="#29434e",foreground="white").place(x = 875, y= 635)
    Label(text = "GREEN  : WRP config Disabled",bg="#29434e",foreground="white").place(x = 875, y= 650)
    Label(text = "RED    : WRP config Enabled",bg="#29434e",foreground="white").place(x = 875, y= 665)


def App_status_connected():
    S1.itemconfig(s1_rect, fill='#00BF32')
    S2.itemconfig(s2_rect, fill='#FF0000')
    S3.itemconfig(s3_rect, fill='#FF0000')
    gui.update()

def IAP_status_connected():
    S1.itemconfig(s1_rect, fill='#FF0000')
    S2.itemconfig(s2_rect, fill='#FF0000')
    S3.itemconfig(s3_rect, fill='#00BF32')
    gui.update()

def Boot_status_connected():
    S1.itemconfig(s1_rect, fill='#FF0000')
    S2.itemconfig(s2_rect, fill='#00BF32')
    S3.itemconfig(s3_rect, fill='#FF0000')
    gui.update()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def connect():

    global dead
    global BaudRates
    global serial_object
    global serial_check
    version_ = button_var.get()
    port = port_entry.get()
    baud = baud_entry.get()

    if (serial_check == 'yes'):
        tkinter.messagebox.showinfo("INFORMATION", "The Device is connected !!")
        return

    if ((baud == '') and (port =='') and (version_ == 0)):
        tkinter.messagebox.showwarning("WARNING", "Please select your OS and Connection info !!")
        return


    if (version_ == 0):
        tkinter.messagebox.showwarning("WARNING", "Please Select your OS !!")
        return

    if ((baud == '') and (port =='')):
        tkinter.messagebox.showwarning("WARNING", "Please enter your connection info !!")
        return

    if (baud == ''):
        tkinter.messagebox.showwarning("WARNING", "Please enter your Baud Rates !!")
        return

    if (int(baud)not in BaudRates):
        tkinter.messagebox.showerror("ERROR", "Invalid Baud Rates !!")
        return

    if (port == ''):
	tkinter.messagebox.showwarning("WARNING", "Please enter your Port !!")
	return

    try:
        if (version_ == 2)or(version_ == 3):
            try:
                serial_object = serial.Serial('/dev/tty' + str(port), baud,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=400)
                serial_check ='yes'
                shwo_connect()

            except:
                serial_check ='no'
                tkinter.messagebox.showerror("ERROR", "Can't Open Specified Port")

        elif version_ == 1:
            try:
                serial_object = serial.Serial('COM' + str(port), baud,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=100)
                serial_check ='yes'
                shwo_connect()
            except:
                serial_check ='no'
                tkinter.messagebox.showerror("ERROR", "Can't Open Specified Port")
    except ValueError:
        print "Enter Baud and Port"
        return

def Start_debug():

    global repeat
    global myrepeat_2
    global dead
    global serial_object
    global serial_check
    global Enable_dgb
    global __all_dbg
    global __error_dbg
    global __iap_dbg
    global __app_dbg
    global __boot_dbg
    global __scner_dbg
    global __error_display
    global senario
    ALL_DBG  = all_debug.get()
    ERR_DBG  = only_errors.get()
    BOOT_DBG = boot_logging.get()
    IAP_DBG = iap_logging.get()
    SCEN_DBG =Scenario_logging.get()
    APP_DBG = app_logging.get()
    senario = select_mode.get()
    check_log = button_enable_debug.get()
    if (serial_check == 'yes'):
        if((check_log!=4) and((SCEN_DBG==1)or(ALL_DBG==1)or(ERR_DBG==1)or(BOOT_DBG==1)or(IAP_DBG==1)or(APP_DBG==1))):
            tkinter.messagebox.showwarning("WARNING", "You must Enable the Debug Logging")
            return
        if((senario!=3) and (SCEN_DBG==1)):
            tkinter.messagebox.showwarning("WARNING", "You must set the Scenario Display")
            return
        myrepeat_2 = myrepeat_2 + 1
        if ((senario == 0) and (myrepeat_2 < 2)):
            tkinter.messagebox.showinfo("INFORMATION", "For more options you can select the mode of the little screen Display ")
            return

    if (serial_check == 'yes'):
        repeat = repeat + 1

    if ((repeat > 1) and (serial_check == 'yes')) :
        if (repeat>3):
            tkinter.messagebox.showinfo("INFORMATION", "You must Restart to load the new configuration")
            return

        tkinter.messagebox.showinfo("INFORMATION", "Debug is ON !!!")
        return

    dead = 'true'
    if (senario != 0):
        if ((senario == 3)or(SCEN_DBG==1)):
            tkinter.messagebox.showinfo("INFORMATION", "You should Learn the use case of The Scenario Test to Succeed The VR")
            __scner_dbg = 'YES'
        elif ((senario == 2)or(SCEN_DBG==1)):
            tkinter.messagebox.showinfo("INFORMATION", "The little Screen is reserver for Displaying software Error")
            __error_display = 'YES'
        t3 = threading.Thread(target = scenario_thread)
        t3.daemon = True
        dead = 'false'
        t3.start()
    try:
        if(check_log == 4 ):
            Enable_dgb = 'YES'
            if (ALL_DBG == 1):
                __all_dbg = 'YES'
            if (ERR_DBG == 1):
                __error_dbg = 'YES'
            if (BOOT_DBG == 1):
                __boot_dbg = 'YES'
            if (IAP_DBG == 1):
                __iap_dbg = 'YES'
            if (APP_DBG == 1):
                __app_dbg = 'YES'
            if (SCEN_DBG == 1):
                __scner_dbg = 'YES'
            if (serial_check == 'yes') :

                t2 = threading.Thread(target = logging_thread)
                t2.daemon = True
                dead = 'false'
                t2.start()
            else :
                tkinter.messagebox.showerror("ERROR", "You should connect to cardio device first  !!")
                return
        if (serial_check == 'yes') :
            S5.itemconfig(s5_rect,fill="#00BF32")
            gui.update()
            t1 = threading.Thread(target = get_data)
            t1.daemon = True
            dead = 'false'
            t1.start()
        else :
            tkinter.messagebox.showerror("ERROR", "You should connect to cardio device first  !!")
            return
    except ValueError:
        tkinter.messagebox.showerror("ERROR", "You should connect to cardio device first!!")
        return



def get_data():
    global dead
    global serial_object
    global serial_data
    global Enable_dgb
    while(1):
        try:
            serial_data = ''
            serial_data = serial_object.readline()
            print serial_data
            if serial_data:
                queu_2.put(serial_data)
                if (Enable_dgb == 'YES'):
                    q.put(serial_data)
                if '[IAP]>' in serial_data :
                    IAP_status_connected()
                    protection_modeB()
                    serial_data = serial_data.replace('[IAP]>', '')
                    #serial_data.lstrip('[IAP]>')
                    if ('Error' in serial_data)or('error' in serial_data)or('Erreur' in serial_data)or('erreur' in serial_data)or('ERROR' in serial_data)or('ERREUR' in serial_data):
                        iap_text.insert(END, serial_data,'warning')

                    else :
                        iap_text.insert(END, serial_data)
                    #iap_text.insert(END,"\n")
                    iap_text.yview_pickplace("end")

                if '[APP]>' in serial_data :
                    App_status_connected()
                    protection_modeA()
                    serial_data = serial_data.replace('[APP]>', '')
                    #serial_data.lstrip('[APP]>')
                    if ('Error' in serial_data)or('error' in serial_data)or('Erreur' in serial_data)or('erreur' in serial_data)or('ERROR' in serial_data)or('ERREUR' in serial_data):
                        app_text.insert(END, serial_data,'warning')
                    else :
                        app_text.insert(END, serial_data)
                    #app_text.insert(END,"\n")
                    app_text.yview_pickplace("end")

                if '[BOOT]>' in serial_data :
                    Boot_status_connected()
                    serial_data = serial_data.replace('[BOOT]>', '')
                    #serial_data.lstrip('[BOOT]>')
                    if ('Error' in serial_data)or('error' in serial_data)or('Erreur' in serial_data)or('erreur' in serial_data)or('ERROR' in serial_data)or('ERREUR' in serial_data):
                        boot_text.insert(END, serial_data,'warning')
                    else :
                        boot_text.insert(END, serial_data)
                    #boot_text.insert(END,"\n")
                    boot_text.yview_pickplace("end")
                if dead == 'true':
                    return
        except TypeError:
            pass

def logging_thread():

    global serial_data
    global file_full_debug
    global file_error_only
    global file_iap_only
    global file_boot_only
    global file_app_only
    global file_Scenario_only
    global __all_dbg
    global __error_dbg
    global __iap_dbg
    global __app_dbg
    global __boot_dbg
    global __scner_dbg
    global dead
    path_to_log = path
    os.makedirs(path, access_rights)

    if (__all_dbg == 'YES'):
        file_full_debug = open(path_to_log +'/'+'CCW Full Log.txt', "w")
    if (__error_dbg == 'YES'):
        file_error_only = open(path_to_log +'/'+'CCW ERROR Log.txt', "w")
    if (__iap_dbg == 'YES'):
        file_iap_only = open(path_to_log +'/'+'CCW IAP Log.txt', "w")
    if (__boot_dbg == 'YES'):
        file_boot_only = open(path_to_log +'/'+'CCW BOOT Log.txt', "w")
    if (__app_dbg == 'YES'):
        file_app_only = open(path_to_log +'/'+'CCW APP Log.txt', "w")
    if (__scner_dbg == 'YES'):
        file_Scenario_only = open(path_to_log +'/'+'CCW SCENARIO VR Log.txt', "w")

    while(1):
        try:
            item = ''
            item = q.get()
            if item :
                if (__all_dbg == 'YES'):
                    file_full_debug.write(item)
                    file_full_debug.flush()

                if (__error_dbg == 'YES'):
                    if ('Error' in item)or('error' in item)or('Erreur' in item)or('erreur' in item)or('ERROR' in item)or('ERREUR' in item):
                        file_error_only.write(item)
                        file_error_only.flush()

                if (__iap_dbg == 'YES'):
                    if '[IAP]>' in item :
                        item = item.replace('[IAP]>', '')
                        file_iap_only.write(item)
                        file_iap_only.flush()


                if (__app_dbg == 'YES'):
                    if '[APP]>' in item :
                        item = item.replace('[APP]>', '')
                        file_app_only.write(item)
                        file_app_only.flush()

                if (__boot_dbg == 'YES'):
                    if '[BOOT]>' in item :
                        item = item.replace('[BOOT]>', '')
                        file_boot_only.write(item)
                        file_boot_only.flush()
                if (__scner_dbg == 'YES'):
                    if '[SCENARIO]>' in item :
                        item = item.replace('[SCENARIO]>', '')
                        file_Scenario_only.write(item)
                        file_Scenario_only.flush()
            if dead == 'true':
                return

        except :
            pass


def scenario_thread():

    global __scner_dbg
    global __error_display
    global dead
    while(1):
        try:
            item_2 = ''
            item_2 = queu_2.get()
            if item_2 :
                if (__scner_dbg == 'YES'):
                    if '[SCENARIO]>' in item_2 :
                        item_2 = item_2.replace('[SCENARIO]>', '')
                        Senario_text.insert(END, item_2)
                        Senario_text.yview_pickplace("end")
                if (__error_display == 'YES'):
                    if ('Error' in serial_data)or('error' in item_2)or('Erreur' in item_2)or('erreur' in item_2)or('ERROR' in item_2)or('ERREUR' in item_2):
                        Senario_text.insert(END, item_2)
                        Senario_text.yview_pickplace("end")
            if dead == 'true':
                return
        except :
            pass


def send():
    if (serial_check == 'no'):
        tkinter.messagebox.showerror("ERROR", "You should connect to cardio device first  !!")
        return

    send_data = data_entry.get()

    if not send_data:
        print "Sent Nothing"

    serial_object.write(send_data)

def disconnect():
    global file_full_debug
    global file_error_only
    global file_iap_only
    global file_boot_only
    global file_app_only
    global file_Scenario_only
    global Enable_dgb
    global __all_dbg
    global __error_dbg
    global __iap_dbg
    global __app_dbg
    global __boot_dbg
    global __scner_dbg

    try:
        serial_object.close()

    except AttributeError:
        print "Closed without Using it -_-"
    if (Enable_dgb == 'YES'):
        if (__all_dbg == 'YES'):
            file_full_debug.close()
        if (__error_dbg == 'YES'):
            file_error_only.close()
        if (__app_dbg == 'YES'):
            file_app_only.close()
        if (__iap_dbg == 'YES'):
            file_iap_only.close()
        if (__boot_dbg == 'YES'):
            file_boot_only.close()
        if (__scner_dbg == 'YES'):
            file_Scenario_only.close()
    gui.quit()

def clear_all():
    boot_text.delete(1.0,END)
    iap_text.delete(1.0,END)
    app_text.delete(1.0,END)
    Senario_text.delete(1.0,END)

def toggleLowDeer():
    if DeerLowButton.config('relief')[-1] == 'sunken':
        DeerLowButton.config(relief="raised")
    else:
        DeerLowButton.config(relief="sunken")


if __name__ == "__main__":

    """
    The Main loop handles all the widget placements for the cardio Debug view.
    """

    #frames
    frame_view_iap = Frame(height = 430, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 5)
    frame_view_boot = Frame(height = 430, width = 430, bd = 3, relief = 'groove',bg="#808e95").place(x = 438, y = 5)
    frame_view_app = Frame(height = 430, width = 440, bd = 3, relief = 'groove',bg="#808e95").place(x = 869, y = 5)
    frame_2 = Frame(height = 156, width = 861, bd = 3, relief = 'groove',bg="#808e95").place(x = 7, y = 552)

    w = Canvas(gui, width=437.5, height=270,bg="#29434e")  # 808e95
    w.pack()
    w.create_text(260, 85,font=("freemono ", 11, "bold"),text = "BANK-2", fill='white', anchor="nw", angle=90)
    w.create_text(260, 215,font=("freemono ", 11, "bold"),text = "BANK-1",  fill='white',anchor="nw", angle=90)
    w.place(x = 869, y = 436)

    bootPart1_rect = w.create_rectangle(280,240, 437.5, 270, fill='white')
    iap_rect = w.create_rectangle(280,200, 437.5, 240, fill='white')
    app_rect = w.create_rectangle(280,135, 437.5, 200, fill='white')
    bootPart2_rect = w.create_rectangle(280,115, 437.5, 135, fill='white')
    emul_rect = w.create_rectangle(280,113, 437.5, 115, fill='black')
    swap_rect = w.create_rectangle(280,50, 437.5, 113, fill='white')
    xfactory_rect = w.create_rectangle(280,2, 437.5, 50, fill='white')

    txt1 = w.create_text(308, 249.5,font=("freemono ", 11, "bold"), text = "BootloaderP1", anchor="nw", angle=0)
    txt2 =w.create_text(347, 215,font=("freemono ", 11, "bold"), text = "IAP", anchor="nw", angle=0)
    txt3 =w.create_text(312, 157,font=("freemono ", 11, "bold"), text = "Application", anchor="nw", angle=0)
    txt4 =w.create_text(308, 118,font=("freemono bold", 11, "bold"), text = "BootloaderP2", anchor="nw", angle=0)
    txt5 =w.create_text(340, 73,font=("freemono ", 11, "bold"), text = "SWAP", anchor="nw", angle=0)
    txt6 =w.create_text(320, 17,font=("freemono ", 11, "bold"), text = "XFactory", anchor="nw", angle=0)

    iap_text = scrolledtext.ScrolledText(gui,width=58,height=35)
    iap_text.grid(column=0,row=0)
    iap_text.place(x = 877, y = 10)

    app_text = scrolledtext.ScrolledText(gui,width=57,height=35)
    app_text.grid(column=0,row=0)
    app_text.place(x = 15, y = 10)

    boot_text = scrolledtext.ScrolledText(gui,width=57,height=35)
    boot_text.grid(column=0,row=0)
    boot_text.place(x = 446, y = 10)

    Senario_text = scrolledtext.ScrolledText(gui,width=59,height=10.48,bg="#102027", foreground="yellow")
    Senario_text.grid(column=0,row=0)
    Senario_text.place(x = 438, y = 436)

    iap_text.tag_config('warning', background="yellow", foreground="red")
    app_text.tag_config('warning', background="yellow", foreground="red")
    boot_text.tag_config('warning', background="yellow", foreground="red")
    #queu for the transmission data between threads
    q = Queue.Queue()
    queu_2 = Queue.Queue()

    #Labels
    osdata_ = Label(text ="OS :",bg="#808e95").place (x = 10, y = 570)
    setting = Label(text ="Advanced Setting",bg="#808e95").place (x = 420, y = 620)
    baud   = Label(text = "Baud",bg="#808e95").place(x = 100, y = 600)
    port   = Label(text = "Port",bg="#808e95").place(x = 200, y = 600)
    boot_indic = Label(text = "BOOTLOADER DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 555, y= 405)
    boot_indic = Label(text = "IAP DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 1035, y= 405)
    boot_indic = Label(text = "APPLICATION DEBUG VIEW",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 100, y= 405)
    project_indic = Label(text = " CARDIO DEVICE CCW V1.0.0",fg = "#eeeeee",font = "Helvetica 16 bold italic",bg="#808e95").place(x = 55, y= 665)

    #contact = Label(text = "mastouri.rida@gmail.com").place(x = 250, y = 437)
    baud_entry = Entry(width = 10)
    baud_entry.place(x = 100, y = 624)
    port_entry = Entry(width = 10)
    port_entry.place(x = 200, y = 624)

    #radio button
    button_var = IntVar()
    radio_1 = Radiobutton(text = "Linux  ", variable = button_var, value = 2,bg="#808e95",relief = 'raised').place(x = 50, y = 570)
    radio_2 = Radiobutton(text = "Windows", variable = button_var, value = 1,bg="#808e95",relief = 'raised').place(x = 140, y = 570)
    radio_3 = Radiobutton(text = "Mac    ", variable = button_var, value = 3,bg="#808e95",relief = 'raised').place(x = 233, y = 570)

    button_enable_debug = IntVar()
    radio_4 = Radiobutton(text = "Enable Logging ", variable = button_enable_debug, value = 4,bg="#808e95",relief = 'raised').place(x = 420, y = 570)

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
    Scenario_logging = IntVar()
    Checkbutton(gui, text="Scenario VR Logging", variable=Scenario_logging,bg="#808e95",relief = 'raised').place(x = 420, y = 675)

    #button
    connect = Button(text = "Connect", command = connect,relief = 'ridge').place(x = 15, y = 620)
    start = Button(text = "Start Debug", command = Start_debug,relief = 'ridge').place(x =625, y = 565)
    disconnect = Button(text = "Disconnect", command = disconnect,relief = 'ridge').place(x =300, y = 620)
    Restart_prog = Button(text = "Restart", command =restart_program,relief = 'ridge').place(x =321, y = 565)
    data1_ = Label(text = "Command:",bg="#102027",foreground="white").place(x = 15, y= 492)
    button1 = Button(text = "Send", command = send, width = 6,relief = 'ridge').place(x = 15, y = 510)
    data_entry = Entry(width = 44)
    data_entry.place(x = 100, y = 513)
    data5_ = Label(text = " Little Screen  ",bg="#102027",foreground="white").place(x = 170, y= 450)
    data6_ = Label(text = " Display Mode>>",bg="#102027",foreground="white").place(x = 170, y= 470)
    select_mode = IntVar()
    nothink    = Radiobutton(text = "  None Display  ", variable = select_mode, value = 1,bg="#808e95",relief = 'raised').place(x = 280, y = 440)
    error_view = Radiobutton(text = " Error Display  ", variable = select_mode, value = 2,bg="#808e95",relief = 'raised').place(x = 280, y = 463)
    test_view  = Radiobutton(text = "Scenario Display", variable = select_mode, value = 3,bg="#808e95",relief = 'raised').place(x = 280, y = 485)

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

    S1 = Canvas(gui, width = 8, height = 8,bg="#29434e")
    S1.pack()
    S1.place(x = 330 , y = 412.5)

    s1_rect = S1.create_rectangle(0,0, 20, 20, fill='#29434e')

    S2 = Canvas(gui, width = 8, height = 8,bg="#29434e")
    S2.pack()
    S2.place(x = 775 , y = 412.5)
    s2_rect = S2.create_rectangle(0,0, 20, 20, fill='#29434e')

    S3 = Canvas(gui, width = 8, height = 8,bg="#29434e")
    S3.pack()
    S3.place(x = 1185 , y = 412.5)
    s3_rect = S3.create_rectangle(0,0, 20, 20, fill='#29434e')

    S4 = Canvas(gui, width = 5, height = 5,bg="#29434e")
    S4.pack()
    S4.place(x = 81, y = 630.5)
    s4_rect = S4.create_rectangle(0,0, 20, 20, fill='#ff0000')

    S5 = Canvas(gui, width = 5, height = 5,bg="#29434e")
    S5.pack()
    S5.place(x = 720, y = 576)
    s5_rect = S5.create_rectangle(0,0, 20, 20, fill='#ff0000')

    gui.geometry('1366x768')
    gui.mainloop()
