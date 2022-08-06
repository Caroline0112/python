import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy 

#Zaczynamy od dwóch funkcji; pierwsza dodaje wzór funkcji, druga czyści okienka, użyjemy ich przy guzikach 
def add_func(text):
    equation = str(equation_tk.get())
    equation = equation + str(text)
    equation_tk.set(equation)

def clearing():
    equation = ""
    equation_tk.set("")
    x_min.set("0")
    x_max.set("1")
    y_min.set("0")
    y_max.set("1")
    plot_name.set("")
#tworzymy okno, określamy składowe okienka, warunki domyślne i wstępny wygląd
root = tk.Tk()
root.geometry("1200x600")
root.configure(bg='green')
root.columnconfigure(0, weight=10)
root.columnconfigure(1, weight=10)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=10)
root.columnconfigure(4, weight=15)


equation = ""
equation_tk = tk.StringVar(root)
x_min = tk.StringVar(root)
x_max = tk.StringVar(root)
y_min = tk.StringVar(root)
y_max = tk.StringVar(root)
x_name = tk.StringVar(root)
y_name = tk.StringVar(root)
plot_name = tk.StringVar(root)
legend = tk.IntVar()
equation_tk.set("")
x_min.set("0")    
x_max.set("1")
y_min.set("0")
y_max.set("1")
x_min_ = tk.Entry(root, textvariable=x_min, width=15)
x_max_ = tk.Entry(root, textvariable=x_max, width=15)
y_min_ = tk.Entry(root, textvariable=y_min, width=15)
y_max_ = tk.Entry(root, textvariable=y_max, width=15)
x_name_ = tk.Entry(root, textvariable=x_name, width=15)
y_name_ = tk.Entry(root, textvariable=y_name, width=15)
plot_name_ = tk.Entry(root, textvariable=plot_name, width=15)
equation_entry = tk.Entry(root, textvariable=equation_tk, width=25)
x_min_.grid(column=1, row=8)
x_max_.grid(column=1, row=9)
y_min_.grid(column=1, row=10)
y_max_.grid(column=1, row=11)
x_name_.grid(column=1, row =12)
y_name_.grid(column=1, row =13)
plot_name_.grid(column=1, row =14)
equation_entry.grid(column=4, row=12)
x_min_label = tk.Label(root, text= "Min X:", width=15).grid(column=0, row=8)
x_max_label = tk.Label(root, text= "Max X:", width=15).grid(column=0, row=9)
y_min_label = tk.Label(root, text= "Min Y:", width=15).grid(column=0, row=10)
y_max_label = tk.Label(root, text= "Max Y:", width=15).grid(column=0, row=11)
x_name_label = tk.Label(root, text= "x name: ", width=15).grid(column=0,row=12)
y_name_label = tk.Label(root, text= "y name: ", width=15).grid(column=0,row=13)
plot_name_label = tk.Label(root, text= "plot name: ", width=15).grid(column=0,row=14)


#zapisujemy słownik, a w drugiej linijce, biorąc klucze, dostajemy się do oczekiwanych funkcji numpy'a i operacji arytmetycznych
math_func = {"Sin": "numpy.sin", "Cos": "numpy.cos", "Ln": "numpy.log", "Exp":"numpy.exp", "+":"+", "-":"-", "*":"*","/":"/"}
math_func_keys = list(math_func.keys())

def plot_button():
    Plot_matplot = plt.figure(figsize=(6,6))
    Plot_tkinter = tk.Frame(root, width=350)
    Plot_tkinter.grid(column=3, row=2, rowspan=13)


    xmin = int(x_min.get())
    xmax = int(x_max.get())
    ymin = int(y_min.get())
    ymax = int(y_max.get())
    
    

    equation = str(equation_tk.get())
    equation1 = str(equation_tk.get())
    if equation == "": 
        equation = "0"
        equation1 = "0"
    for key, value in math_func.items(): 
        equation = equation.replace(key, value) 

    functions = equation.split(';') 
    functions1 = equation1.split(';')

    arguments_list = numpy.linspace(xmin, xmax)

    
    for i in range(len(functions)):
        value_list = [eval(functions[i]) for x in arguments_list] #dostajemy funkcje
        plt.plot(arguments_list, value_list, label=str(functions1[i]))
        plt.xlabel(x_name.get())    
        plt.ylabel(y_name.get())
        plt.title(plot_name.get())
        plt.axis([xmin,xmax,ymin,ymax])
  
    if legend.get():
        plt.legend()
    plt.grid()

    Canvas = FigureCanvasTkAgg(Plot_matplot, Plot_tkinter)
    Canvas.get_tk_widget().pack(side=tk.RIGHT)

plot_button()

#nadanie funkcjonalności głównym przyciskom i legendzie (check)
plotting_button = tk.Button(root, text = "DRAW", command=plot_button, width=15).grid(column=0, row=3)
clearing_button = tk.Button(root, text = "CLEAR", width=15, command=clearing).grid(column=1, row=3)
legend_button = tk.Checkbutton(root, text="Legend", variable=legend, onvalue=True, offvalue=False, width=15).grid(column=4, row=14)
#przyciski-nadajemy im opisy i funkcje
button1 = tk.Button(root, text="sin", width=15, command=lambda: [add_func("Sin()")]).grid(column=0, row=4)
button2 = tk.Button(root, text="cos", width=15, command=lambda: [add_func("Cos()")]).grid(column=1, row=4)
button5 = tk.Button(root, text="ln", width=15, command=lambda: [add_func("Ln()")]).grid(column=0, row=5)
button6 = tk.Button(root, text="exp", width=15, command=lambda: [add_func("Exp()")]).grid(column=1, row=5)
button7 = tk.Button(root, text="+", width=15, command=lambda: [add_func("+")]).grid(column=0, row=6)
button8 = tk.Button(root, text="*", width=15, command=lambda: [add_func("*")]).grid(column=1, row=6)
button9 = tk.Button(root, text="-", width=15, command=lambda: [add_func("-")]).grid(column=0, row=7)
button8 = tk.Button(root, text="/", width=15, command=lambda: [add_func("/")]).grid(column=1, row=7)
root.mainloop ()








