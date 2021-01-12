from tkinter import *
from tkinter.messagebox import *
import subprocess
import random
import threading
import queue as Queue
from tkinter.ttk import Progressbar



OPTIONS = [
"Select Server",
"US Server",
"Canada Server",
"United Kingdom Server (down)",
"France Server",
"Germany Server",
"Poland Server"
]

TCP_VPNS = {
    "US" : [("us1.vpnbook.com", "vpnbook", "k8VBRa6"), ("us2.vpnbook.com", "vpnbook", "k8VBRa6")],
    "UK" : [("uk.justfreevpn.com", "justfreevpn", "1881")],
    "CA" : [("ca222.vpnbook.com", "vpnbook", "k8VBRa6"), ("ca198.vpnbook.com", "vpnbook", "k8VBRa6")],
    "FR" : [("fr1.vpnbook.com", "vpnbook", "k8VBRa6"), ("fr8.vpnbook.com", "vpnbook", "k8VBRa6")],
    "DE" : [("DE4.vpnbook.com", "vpnbook", "k8VBRa6")],
    "PL" : [("PL226.vpnbook.com", "vpnbook", "k8VBRa6")],
}

UDP_VPNS = {
    "US" : [("us1.vpnbook.com", "vpnbook", "k8VBRa6"), ("us2.vpnbook.com", "vpnbook", "k8VBRa6")],
    "UK" : [("uk.justfreevpn.com", "justfreevpn", "1881")],
    "CA" : [("ca222.vpnbook.com", "vpnbook", "k8VBRa6"), ("ca198.vpnbook.com", "vpnbook", "k8VBRa6")],
    "FR" : [("fr1.vpnbook.com", "vpnbook", "k8VBRa6"), ("fr8.vpnbook.com", "vpnbook", "k8VBRa6")],
    "DE" : [("DE4.vpnbook.com", "vpnbook", "k8VBRa6")],
    "PL" : [("PL226.vpnbook.com", "vpnbook", "k8VBRa6")],
}


subprocess.run('powershell Remove-VpnConnection -Name "VPN" -Force -PassThru', shell=True, capture_output=True)


def connect_to_vpn(ServerAddress, Username, Password):
    subprocess.run(f'powershell Add-VpnConnection -Name "VPN" -ServerAddress "{ServerAddress}" -Force -RememberCredential -PassThru', shell=True, capture_output=True)
    subprocess.run(f'rasdial.exe "VPN" "{Username}" "{Password}"', shell=True, capture_output=True)

def disconnect_from_vpn():
    subprocess.run('rasdial.exe "VPN" /disconnect', shell=True, capture_output=True)
    subprocess.run('powershell Remove-VpnConnection -Name "VPN" -Force -PassThru', shell=True, capture_output=True)


def progressbar_connect():

    p = Progressbar(root,orient=HORIZONTAL,length=150,mode="determinate",takefocus=True,maximum=10000)
    p.pack()            
    for i in range(10000):                
        p.step()            
        root.update()

def Connect_Button_Code_full(value, conn_type):
    while threading.Thread(target=Connect_Button_Code, args=(value, conn_type)).start():
        threading.Thread(target=progressbar_connect).start()


def Connect_Button_Code(value, conn_type):
    if conn_type == 1:
        conn_type = "TCP"
    else:
        conn_type = "UDP"

    US = "US Server"
    CA = "Canada Server"
    UK = "United Kingdom Server"
    FR = "France Server"
    DE = "Germany Server"
    PL = "Poland Server"

    if value == US:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["US"])
        else:
            vpn = random.choice(UDP_VPNS["US"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to an American {conn_type} Server")

    if value == CA:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["CA"])
        else:
            vpn = random.choice(UDP_VPNS["CA"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to a Canadian {conn_type} Server")
    
    if value == UK:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["UK"])
        else:
            vpn = random.choice(UDP_VPNS["UK"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to a British {conn_type} Server")
    
    if value == FR:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["FR"])
        else:
            vpn = random.choice(UDP_VPNS["FR"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to a French {conn_type} Server")
    
    if value == DE:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["DE"])
        else:
            vpn = random.choice(UDP_VPNS["DE"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to a German {conn_type} Server")
    
    if value == PL:
        if conn_type == "TCP":
            vpn = random.choice(TCP_VPNS["PL"])
        else:
            vpn = random.choice(UDP_VPNS["PL"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", f"Connected to a Polish {conn_type} Server")

def Disconnect_Button_Code():
    disconnect_from_vpn()
    showinfo("Disconnected", "Successfully Disconnected from VPN")


root = Tk()
root.title("VPN")
# root.iconbitmap("icon.iso")

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value
r = IntVar()


Radiobutton(root, text="TCP", variable=r, value=1).pack()
Radiobutton(root, text="UDP", variable=r, value=2).pack()

OptionMenu(root, variable, *OPTIONS).pack()


Connect_Button = Button(root, text="Connect", command=lambda: Connect_Button_Code_full(variable.get(), r.get()))
Disconnect_Button = Button(root, text="Disconnect", command=Disconnect_Button_Code)
Connect_Button.pack()
Disconnect_Button.pack()

mainloop()