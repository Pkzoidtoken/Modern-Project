from tkinter import *
import time

root = Tk()
root.geometry('916x692')
root.title("NFT")

background_photo = PhotoImage(file='Main.png')

MINE_COIN = 0.0000000
PET_SPEED = 2000
SPEED = 0.0000000

def background_task(e):
	mine_earn()

def mine_earn():
    global MINE_COIN
    MINE_COIN += 0.0000001  # Increment amount
    mycanvas.itemconfig(earn_btc, text=' '.join(f"{MINE_COIN:.7f}"))  # Update text
    root.after(2000, mine_earn)  # Call this function again after 2000ms (2 seconds)

#buy pet change pet
def buy_duck(e):
	PET_SPEED = 2000
	mycanvas.itemconfig(default_pet,image=duck_pet)

def buy_rabit(e):
	PET_SPEED = 1500
	mycanvas.itemconfig(default_pet,image=rabit_pet)

def buy_recon(e):
	PET_SPEED = 1000
	mycanvas.itemconfig(default_pet,image=recon_pet)

def buy_mole(e):
	PET_SPEED = 100
	mycanvas.itemconfig(default_pet,image=mole_pet)

def buy_fox(e):
	PET_SPEED = 2500
	mycanvas.itemconfig(default_pet,image=fox_pet)

#mining button
mine = PhotoImage(file='mine.png')
withdraw = PhotoImage(file='withdraw.png')

#earning show
earn = PhotoImage(file='earn.png')
speed = PhotoImage(file='speed.png')

#card photo
fox_card = PhotoImage(file='fox.png')
duck_card = PhotoImage(file='duck.png')
rabit_card = PhotoImage(file='rabit.png')
recon_card = PhotoImage(file='recon.png')
mole_card = PhotoImage(file='mole.png')

#stage pet default
fox_pet = PhotoImage(file='default.png')
duck_pet = PhotoImage(file='duck_pet.png')
rabit_pet = PhotoImage(file='rabit_pet.png')
recon_pet = PhotoImage(file='recon_pet.png')
mole_pet = PhotoImage(file='mole_pet.png')

mycanvas = Canvas(root,width=916,height=692)
mycanvas.pack(fill='both',expand=True)

mycanvas.create_image(0,0,image=background_photo,anchor='nw')
fox = mycanvas.create_image(90,136,image=fox_card)
duck = mycanvas.create_image(220,136,image=duck_card)
rabit = mycanvas.create_image(350,136,image=rabit_card)
recon =	mycanvas.create_image(480,136,image=recon_card)
mole = mycanvas.create_image(590,115,image=mole_card)
rabit1 = mycanvas.create_image(740,136,image=rabit_card)
duck1 = mycanvas.create_image(865,136,image=duck_card)

mycanvas.create_image(450,235,image=earn)
mycanvas.create_image(450,310,image=speed)

#earning show text
mycanvas.create_text(370,290,text=' '.join('0.0000000'),font=("Arial",25),anchor='nw',fill='white')
earn_btc = mycanvas.create_text(370,215,text=' '.join('0.0000000'),font=("Arial",25),anchor='nw',fill='white')

#place button
mine_btn = mycanvas.create_image(310,620,image=mine)
mycanvas.create_image(550,620,image=withdraw)

default_pet = mycanvas.create_image(440,450,image=fox_pet)

#bind all cards for clickable
mycanvas.tag_bind(duck,"<Button-1>",buy_duck)
mycanvas.tag_bind(rabit,"<Button-1>",buy_rabit)
mycanvas.tag_bind(recon,"<Button-1>",buy_recon)
mycanvas.tag_bind(mole,"<Button-1>",buy_mole)
mycanvas.tag_bind(fox,"<Button-1>",buy_fox)
mycanvas.tag_bind(duck1,"<Button-1>",buy_duck)
mycanvas.tag_bind(rabit1,"<Button-1>",buy_rabit)
mycanvas.tag_bind(mine_btn,"<Button-1>",background_task)

root.mainloop()
