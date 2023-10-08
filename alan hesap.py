from tkinter import *
import math

pencere=Tk()

pencere.title("Alan-Hesap")
pencere.geometry("600x300")

def alanhesap():
    yaricap = xx.get()
    yaricap = int(yaricap)
    alan = math.pi * (pow(yaricap,2))
    yazı= "Dairenin Alanı = " + str(alan) + " cm^2."
    cbk6.config(text=yazı)
   

def çevrehesap():
    yarıcap= xx.get()
    yarıcap=int(yarıcap)
    cevre = 2*math.pi*yarıcap
    yazı ="Dairenin Çevresi ="+str(cevre)+"cm."
    cbk6.config(text=yazı)

bck=Label(text="Dairenin yarıçapı:",padx=45,pady=0)
bck.place(x=10,y=30)
xx = Entry()
xx.place(x=160,y=30)


cbk2=Button(text="ALAN HESAP",command = alanhesap)
cbk2.place(x=15,y=75)
cbk3=Button(text="ÇEVRE HESAP",command = çevrehesap)
cbk3.place(x=150,y=75)

cbk6=Label(text="cm.",padx=10,pady=2)
cbk6.place(x=300,y=29)

cbk4=Label()
cbk4.place(x=10,y=150)

cbk5=Button(pencere,text=("KAPAT"),command=pencere.destroy).place(x=400,y=200)
 


   
pencere.mainloop()   


