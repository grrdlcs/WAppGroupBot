from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk

def enviar_wasap(grupos,mensaje):
    global mensa
    URL='https://web.whatsapp.com/'
    #texto=" ".join(mensaje)
    #texto=" ".join(mensa)
    texto=mensa
    grupo=list(grupos)
    driver=webdriver.Chrome()
    driver.get(URL)
    time.sleep(22)
    for i in grupo:
        time.sleep(3)
        print("Buscando {} ...".format(i))
        mBox=driver.find_element("xpath",'/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
        mBox.send_keys(i[:9])
        time.sleep(4)
        elements=driver.find_elements(By.TAG_NAME,"span")
        for element in elements:
            if element.text==i:
                element.click()
                tBox=driver.find_element("xpath",'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]')
                tBox.send_keys(texto)
                time.sleep(1)
                #Apreto enviar
                #driver.find_element("xpath",'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
                print("Grupo {} Mensaje enviado".format(i))
                mBox.clear()
                break
    exit()
grupos=[]
mensaje=[]
mensa=''
with open("grupos.txt") as archivo:
    for linea in archivo:
        grupos.append(linea.rstrip())
 
with open("mensaje.txt") as archivo:
    for linea in archivo:
        mensaje.append(linea.rstrip())

def envia():
    enviar_wasap(grupos,mensa)

window = tk.Tk()
window.title('Envio de Whatsapp')
window.geometry('800x500')
l = tk.Label(window, bg='grey', width=90, text='Listado de Grupos')
l.pack()
for a in grupos:
    l = tk.Label(window, bg='white', width=90, text=a)
    l.pack()

l = tk.Label(window, bg='grey', width=90, text='Mensaje')
l.pack()
for b in mensaje:
    l = tk.Label(window, bg='white', width=90, text=b)
    l.pack()

def getTextInput():
    global mensa
    result=textExample.get("1.0","end")
    print(result)
    mensa=result

textExample=tk.Text(window, height=10)
textExample.insert('1.0', mensaje)
textExample.pack()
btnRead=tk.Button(window, height=1, width=10, text="Read", command=getTextInput)

btnRead.pack()

checkme = tk.Button(window, text='Enviar Whatsapp',command=envia)
checkme.pack()
window.mainloop()