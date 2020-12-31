from tkinter import *
from tkinter.messagebox import *
import subprocess
import random

vpns = {
    "US" : [("us1.vpnbook.com", "vpnbook", "z9KY2tN"), ("us2.vpnbook.com", "vpnbook", "z9KY2tN")],
    "UK" : [("uk.justfreevpn.com", "justfreevpn", "1881")],
    "CA" : [("ca222.vpnbook.com", "vpnbook", "z9KY2tN"), ("ca198.vpnbook.com", "vpnbook", "z9KY2tN")],
    "FR" : [("fr1.vpnbook.com", "vpnbook", "z9KY2tN"), ("fr8.vpnbook.com", "vpnbook", "z9KY2tN")],
    "DE" : [("DE4.vpnbook.com", "vpnbook", "z9KY2tN")],
    "PL" : [("PL226.vpnbook.com", "vpnbook", "z9KY2tN")],
}

subprocess.run('powershell Remove-VpnConnection -Name "VPN" -Force -PassThru', shell=True, capture_output=True)


def connect_to_vpn(ServerAddress, Username, Password):
    subprocess.run(f'powershell Add-VpnConnection -Name "VPN" -ServerAddress "{ServerAddress}" -Force -RememberCredential -PassThru', shell=True, capture_output=True)
    subprocess.run(f'rasdial.exe "VPN" "{Username}" "{Password}"', shell=True, capture_output=True)

def disconnect_from_vpn():
    subprocess.run('rasdial.exe "VPN" /disconnect', shell=True, capture_output=True)
    subprocess.run('powershell Remove-VpnConnection -Name "VPN" -Force -PassThru', shell=True, capture_output=True)



def Connect_Button_Code(value):
    US = 1
    CA = 2
    UK = 3
    FR = 4
    DE = 5
    PL = 6

    if value == US:
        vpn = random.choice(vpns["US"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to an American Server")

    if value == CA:
        vpn = random.choice(vpns["CA"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to a Canadian Server")
    
    if value == UK:
        vpn = random.choice(vpns["UK"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to a British Server")
    
    if value == FR:
        vpn = random.choice(vpns["FR"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to a French Server")
    
    if value == DE:
        vpn = random.choice(vpns["DE"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to a German Server")
    
    if value == PL:
        vpn = random.choice(vpns["PL"])
        connect_to_vpn(vpn[0], vpn[1], vpn[2])
        showinfo("Connected", "Connected to a Polish Server")

def Disconnect_Button_Code():
    disconnect_from_vpn()
    showinfo("Disconnected", "Successfully Disconnected from VPN")


root = Tk()
root.title("VPN")
# root.iconbitmap("icon.iso")

r = IntVar()

Radiobutton(root, text="USA", variable=r, value=1).pack()
Radiobutton(root, text="Canada ", variable=r, value=2).pack()
Radiobutton(root, text="England", variable=r, value=3).pack()
Radiobutton(root, text="France ", variable=r, value=4).pack()
Radiobutton(root, text="Germany", variable=r, value=5).pack()
Radiobutton(root, text="Poland ", variable=r, value=6).pack()

Connect_Button = Button(root, text="Connect", command=lambda: Connect_Button_Code(r.get()))
Disconnect_Button = Button(root, text="Disconnect", command=Disconnect_Button_Code)
Connect_Button.pack()
Disconnect_Button.pack()

mainloop()