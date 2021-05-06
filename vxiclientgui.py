import tkinter as tk
import tkinter.font as font
import vxi11

result="Tour IP address"
root=tk.Tk()

time_instr = vxi11.Instrument("TCPIP::"+result+"::inst1::INSTR")

backGround='#FFFFFF'
BackGround_img="backgrond.png"
logo="logo-atem.png"
fcolor="#565656"
fbg='#FFFFFF'

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        #master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


u = tk.IntVar()
v = tk.IntVar()
#REPERTOIRE DE BOUTON__________________________
sw1 = [
      ("E1", 1),
      ("E2", 2),
      ("E3", 3),
      ("E4", 4),
      ("E5", 5),
      ("E6", 6)
      ]

sw2 = [
      ("E7", 7),
      ("E8", 8),
      ("E9", 9),
      ("E10", 10),
      ("E11", 11),
      ("E12", 12)
      ]

#RECUPERE LE TEXTE______________________________ 
def returnEntry(arg=None):
    result = str(myEntry.get())
    return result

radio = tk.IntVar()

#COMMENCE SUR L'IP DE BASE SI IL Y PAS DE TEXTE_
def command1():
	send1=str(v.get())

	if returnEntry() == "":
		time_instr = vxi11.Instrument("TCPIP::"+result+"::inst1::INSTR")
		time_instr.write('set:pin.E'+send1+':on')
	else:
		time_instr = vxi11.Instrument("TCPIP::"+returnEntry()+"::inst1::INSTR")
		time_instr.write('set:pin.E'+send1+':on')


def command2():
	send2=str(u.get())

	if returnEntry() == "":
		time_instr = vxi11.Instrument("TCPIP::"+result+"::inst1::INSTR")
		time_instr.write('set:pin.E'+send2+':on')
	else:
		time_instr = vxi11.Instrument("TCPIP::"+returnEntry()+"::inst1::INSTR")
		time_instr.write('set:pin.E'+send2+':on')


def name1():
      text = tk.Label(root, text="commutateur 1", borderwidth=0)
      text.place(relx=0.01, rely=0.38)
      text.config(background=fbg, foreground=fcolor, font=("Helvetica", 14, "bold"))

def name2():
      text = tk.Label(root, text="commutateur 2", borderwidth=0)
      text.place(relx=0.01, rely=0.58)
      text.config(background=fbg, foreground=fcolor, font=("Helvetica", 14, "bold"))      

#AFFICHAGE DES RADIO BOUTONS____________________
def sw6():
    for sw, val in sw1:
        tk.Radiobutton(
            root,
            text=sw,
            font=("Helvetica", 15),
            bg="red",
            selectcolor="#b8de37",
            activebackground="#ff9f21",
            indicatoron=0,
            width=5,
            height=5,
            padx=40,
            variable=v,
            command=command1,
            value=val,
            borderwidth=10,
        ).place(relx=(0.13 * val) - 0.01, rely=0.35)
        name1()

#AFFICHAGE DES RADIO BOUTONS____________________
def sw12():
    for sw, val in sw2:
        tk.Radiobutton(
            root,
            text=sw,
            font=("Helvetica", 15),
            bg="red",
            selectcolor="#b8de37",
            activebackground="#ff9f21",
            indicatoron=0,
            width=5,
            height=5,
            padx=40,
            variable=u,
            command=command2,
            value=val,
            borderwidth=10,
        ).place(relx=(0.13 * (val - 6)) - 0.01, rely=0.55)
        name2()

##\\##__##\\__##
app = FullScreenApp(root)
v = tk.IntVar()
# NOM DE L'APP___________________________________
root.title("VXI GUI")

# COULEUR DE FOND________________________________
root.configure(background=backGround)

# BANDO VERT AU DESSUS___________________________
cnv = tk.Canvas(root, width=2557, height=40, bg="#b8de37")
cnv.place(relx=0, rely=0)

# TITRE__________________________________________
text = tk.Label(root, text="GPIOs control", borderwidth=0)
text.place(relx=0.01, rely=0.07)
text.config(background=fbg, foreground=fcolor, font=("Helvetica", 40, "bold"))

# TEXTE__________________________________________
text = tk.Label(root, text="IP:", borderwidth=0)
text.grid(row=0, column=0, pady=10)
text.config(background="#b8de37", font=("Helvetica", 15, "bold"))

# BARRE DE TEXRE_________________________________
myEntry = tk.Entry(root, width=20, bd=2)
myEntry.bind("<Return>", returnEntry)
myEntry.grid(row=0, column=1)

# SAUTER UNE COLONE______________________________
space2 = text = tk.Label(root, text="  ", borderwidth=0)
space2.config(bg="#b8de37", height=1)
space2.grid(row=0, column=2)

# BOUTON POUR VALIDER____________________________
enterEntry = tk.Button(
    root,
    text="Enter",
    borderwidth=2,
    command=returnEntry,
    font=font.Font(family="Helvetica", size=13),
)
enterEntry.config(bg="white", height=1)
enterEntry.grid(row=0, column=3)

# BOUTONS POUR CHANGER LE NOMBRE DE BOUTONS______
space = text = tk.Label(root, text="                     ", borderwidth=0)
space.config(bg="#b8de37", height=1)
space.grid(row=0, column=4)
# BOUTON_________________________________________
commutateur1 = tk.Button(
    root,
    text="commutateur 1",
    borderwidth=2,
    command=sw6,
    font=font.Font(family="Helvetica", size=13, weight="bold"),
)
commutateur1.config(bg="white", height=1)
commutateur1.grid(row=0, column=5)

# SAUTER UNE COLONE______________________________
space2 = text = tk.Label(root, text="      ", borderwidth=0)
space2.config(bg="#b8de37", height=1)
space2.grid(row=0, column=6)

# BOUTON_________________________________________
commutateur2 = tk.Button(
    root,
    text="commutateur 2",
    borderwidth=2,
    command=sw12,
    font=font.Font(family="Helvetica", size=13, weight="bold"),
)
commutateur2.config(bg="white", height=1)
commutateur2.grid(row=0, column=7)

root.mainloop() 



