from tkinter import *
import tkinter as tk
import requests
import json

 # ta funkcja głównie do uzyskiwania walut z listy
def sl(str):
    for i in str:
        if i=="(":
            x1 = str.index(i)+1    #bierzemy wnętrze nawiasu
        if i==")":
            x2 = str.index(i)
    return str[x1:x2] 

currencies = ["(USD)","(PLN)","(EUR)", "(CNY)","(CAD)","(MXN)","(GBP)","(JPY)","(CHF)"]


def currency_converter(): # funkcja przeliczająca waluty
    api_key = "UYUAAK43NQJFTKIU"
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    variable1 = sl(var1.get())
    variable2 = sl(var2.get())
    main_url = url+"&from_currency="+variable1+"&to_currency="+variable2+"&apikey="+api_key
    req_ob = requests.get(main_url)
    result = req_ob.json()
    print(result)
    rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    amount = float(amount1.get())
    new_amount = round(amount*rate,2)
    final_amount.insert(0, str(new_amount))


def create_GUI(): # ta funkcja tworzy warstwę graficzną
    
    amount_label = Label(root,width=20, text = "Podaj kwotę : ", bg="#cc99cc") 
    amount_label.grid(row=2, column=0, padx=20,pady=10)
    global starting_amount
    starting_amount = Entry(root, width = 28, textvariable =amount1)
    starting_amount.grid(row=2, column = 1, padx=20,pady=10)

    
    from_currency = Label(root,width=20, text = "Waluta wyjściowa: ", bg="#cc99cc")
    from_currency.grid(row=3,column=0,padx=20,pady=10)
    from_currency_menu = OptionMenu(root, var1, *currencies)
    from_currency_menu.grid(row=3, column=1,padx=20,pady=10)

    to_currency = Label(root,width=20, text = "Waluta przeliczona: ", bg="#cc99cc")
    to_currency.grid(row=4,column=0,padx=20,pady=10)
    to_currency_menu = OptionMenu(root, var2, *currencies)
    to_currency_menu.grid(row=4, column=1,padx=20,pady=10)

    new_amount_label = Label(root, width=20, text = "Przeliczona kwota: ", bg="#cc99cc")
    new_amount_label.grid(row=5, column=0,padx=20,pady= 10 )
    global final_amount
    final_amount= Entry(root, width=28)
    final_amount.grid(row=5, column= 1,padx=20,pady=10)

    #przyciski, nadaję im oczekiwany wygląd i funkcje
    starting_button = Button(root, width = 15, text = "Przelicz", command= currency_converter,bg="#663366")
    starting_button.grid(row = 6, column =0, padx=20,pady=10)
    clearing_button = Button(root, width = 15, text="Wyczyść", command= clearing, bg="#663366")
    clearing_button.grid(row=6, column=1,padx= 20, pady =10)



def clearing():  # Funkcja "czyszcząca" do clearing
    starting_amount.delete(0, END)
    final_amount.delete(0, END)


root = tk.Tk()
var1 = tk.StringVar()
var1.set("Wybierz walutę :")
var2 = tk.StringVar()
var2.set("Wybierz walutę :")
amount1= tk.StringVar()
root.geometry("400x250")
root.title("Przelicznik walut")
root.config(background = "#996699")


create_GUI()
root.mainloop()