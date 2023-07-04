import time
from tkinter import *
import tkinter.messagebox
Screen=Tk()
Screen.title("The Event")
Screen.geometry("600x600")
def option_rock():
    l2=Label(text="""\nYou quickly run inside the nearest building and decided to witness the ongoing events. You see some people are already there.
A few of them decided to film the ongoing events on their mobile. Will you: """)
    l2.pack()
    lp=Label(Screen)
    lp.pack()
    time.sleep(1)
    def D():
      l=Label(text="""You sat down with the rest and decided to just witness the entire event.
Soon, the gangsters started approaching you because one the "Film Makers" forgot to put his phone on silent. Congratulation!!! You died""") 
      l.pack()
    def E():
      l=Label(text="""You decided to film the event like the rest. A few people decided to be more daring
 and starting moving in the direction of the Battle, seeing them, you also moved a little. The phone of one of those person's rang.
 All of you were spotted and blazed. Congratulation!!! You are Dead.""")
      l.pack()
    def F():
      option_cave()

    C4=Button(text="A. Do Nothing and Just Watch", command=D)
    C4.pack()
    C5=Button(text="B. Decide to Film it", command=E)
    C5.pack()
    C6=Button(text="C. Figure out ways to escape the mess", command=F)
    C6.pack()

def intro():
    l1=Label(text="""While going home, you decided to take the Bleaker Street, on your way, you hear a gunfire. You turn  and see 4 SUV's coming from opposite directions and 4 from your side.It seems like a crossfire is about to happen. You will:""")
    l1.pack()
    time.sleep(1)
    def A():
        l=Label(text="""\nThere's a difference between Heroic and Stupid, you chose the rahter. Turns out, it was a Gangwar, They Shot you  then and there.
Congratulations!!! You are dead. """)
        l.pack()
    def B():
        option_rock()
    def C():
        l=Label(text=""" Just like the most of them you panicked and started running. Not long after,
You spot two tanks heading in your direction. Congratulation!!! The tanks opened fire and You died with the rest of them""")
        l.pack()
    C1=Button(text="A. Be a hero and s in the middle of the road so that the two groups halt", command=A)
    C1.pack()
    C2=Button(text="B. Hide inside a building", command=B)
    C2.pack()
    C3=Button(text="C. Run", command=C)
    C3.pack()


def option_cave():
  def G():
    l=Label(text="""You go back and hilde with the rest. Soon, the gangsters come in blazing with their guns
 since one of the filming "Directors" was so stupid , he who forgot to put his phone on silent. Congratulations!! You are dead.""")
    l.pack()
  def H():
    l4=Label(text="""With some force, you were able to open the door
On the other side, you saw a staircase leading to the basement and the roof
Will you: """)
    l4.pack()
    def I():
      l=Label(text="""You rush towards the basement. On your way, you come accros another door with a window out of which
you can see the outside road. You decide to open that door and make a run for it. Luckily, the mob was focused on
themselves and no one bothered to even scan the area. So, you were able to escape. Congratulations!! You Survived""")
      l.pack()
    def J():
      l=Label(text="""You decided to rush towards the roof. You waited for a while. Then Spotted some of them coming inside the buiding,thankfully,
they didn't come on the roof and went out back to their fight. After a while, the whole scene goes quite. You decide to take a look out of the roof
to make sure the area was clear. Oops, Turns out, it wasn't so, they had just stopped to reload. You were spotted and shot.
Congratulation!!! You Died""")
      l.pack()
    time.sleep(1)
    C9=Button(text="A. Walk/Rush towards the basment", command=I)
    C9.pack()
    C10=Button(text="B. Walk/Rush towards the roof", command=J)
    C10.pack()
          
  l3=Label(text="""You look around and find a door at the very end of the corridor. You decide to approach it.
 You think to  yourself that you don't know what might be behind that door. You could either go back and wait with the others
 or Move forward and open the door.""")
  l3.pack()
  time.sleep(1)
  C7=Button(text="A. Go back", command=G)
  C7.pack()
  C8=Button(text="B. Move Forward", command=H)
  C8.pack()

intro()
def MB():
    tkinter.messagebox.showinfo("About", "Project Version 1.0 B, Made by KnightHood_VK")
def Erase():
    Ans=tkinter.messagebox.askquestion("","Are You Sure?")
    if Ans=='yes':
        Screen.destroy()
def New():
    Screen.destroy()
    intro()

menubar = Menu(Screen)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=New)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Erase)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=MB)
menubar.add_cascade(label="Help", menu=helpmenu)
Screen.config(menu=menubar)
Screen.mainloop()
