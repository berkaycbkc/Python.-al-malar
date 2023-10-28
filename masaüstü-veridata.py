import tkinter
pencere = tkinter.Tk()
tabloAdi = ""
def vtolustur():
    # veritabanıda tablo oluşturma
    import mysql.connector

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="445566",
    database="pythondersleri"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE obs (ad VARCHAR(255), telefon VARCHAR(255))")

def kaydet():
    import mysql.connector

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="445566",
    database="pythondersleri"
    )

    mycursor = mydb.cursor()

    a= "INSERT INTO obs (ad, telefon) VALUES (%s, %s)"
    b= (adE.get(), telefonE.get())
    mycursor.execute(a, b) 

    mydb.commit()

adL = tkinter.Label(text="Adı:").grid(row=1,column=1)
telL = tkinter.Label(text="Telefonu:").grid(row=1,column=2)
adE = tkinter.Entry()
adE.grid(row=2,column=1)
telefonE = tkinter.Entry()
telefonE.grid(row=2,column=2)
kaydet = tkinter.Button(text="Kaydet",command=kaydet).grid(row=3,column=2)

tabloaL = tkinter.Label(text="Tablo adı:").grid(row=4,column=2)
tabloaE = tkinter.Entry().grid(row=5,column=2)
olustur = tkinter.Button(text="Olustur",command=vtolustur).grid(row=5,column=3)

pencere.mainloop()
