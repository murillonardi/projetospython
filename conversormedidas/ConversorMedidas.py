from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#cores do app
color1 = "#2C3333"
color2 = "#FFFFFF"
color3 = "#2E4F4F"
janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg=color1)
janela.resizable(width=FALSE, height=FALSE)

#frames do app
frame_above = Frame(janela, width=450, height=100, bg=color1, pady=0, padx=3, relief="flat")
frame_above.place(x=2, y=2)

frame_left = Frame(janela, width=450, height=170, bg=color1, pady=0, padx=3, relief="flat")
frame_left.place(x=2, y=82)

frame_right = Frame(janela, width=198, height=260, bg=color1, pady=0, padx=0, relief="flat")
frame_right.place(x=454, y=2)

#estilo
style = ttk.Style(janela)
style.theme_use("clam")

calculator_app_name = Label(frame_above, text="Calculadora de Unidades de Medida", height=1, padx=0, relief="flat", anchor="center", font=('Arial 15 bold'), bg=color1, fg=color2)
calculator_app_name.place(x=50, y=10)

calculator_app_inst = Label(frame_above, text="Instruções - Selecione uma das medidas nos botões abaixo e preencha os \n valores solicitados no canto direito", height=10, padx=0, relief="flat", anchor="nw", font=('Arial 8 bold'), bg=color1, fg=color2)
calculator_app_inst.place(x=2, y=45)

unidades = {'Massa':[{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'mg': 0.001}] ,
            'Tempo':[{'segundo':31557600}, {'minuto':525960}, {'hora':8766}, {'dia':365.25}, {'semana':52.18}, {'mês':12}, {'ano':1}],
            'Comprimento':[{'km':1000}, {'hm':100}, {'dm':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}, {'milha':1609.34}, {'jarda':0.9144}, {'pé': 0.3048}, {'polegada':0.0254}, {'milha náutica':1852}] , 
            'Área':[{'km2':0.000001}, {'m2':1}, {'milha2':0.000000386}, {'pé2':10.7639}, {'polegada2':1550}, {'hectare':0.0001}, {'acre':0.000247105}] , 
            'Volume':[{'m3':1000}, {'litro':1}, {'mL':0.001}, {'galão imperial':4.55}, {'onça líq imperial':0.03}] , 
            'Velocidade':[{'km/h':3.6}, {'milha/h':2.24}, {'m/s':1}, {'nó':1.94}]}

def show_menu(i):
    unidade_de = []
    unidade_para = []
    unidade_de_values = []
    unidade_para_values = []
    entrada = {}

    for j in unidades[i]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            entrada[k] = v
    
    combo_de['values'] = unidade_de
    combo_para['values'] = unidade_para

    unidade_nome['text'] = i

    def calcular():

        a = combo_de.get()
        b = combo_para.get()
        result = 0

        num_convert = float(entry_numero.get())

        try:
            if unidade_nome['text'] in ('Massa', 'Comprimento', 'Volume'):
                result = round((entrada[a] / entrada[b] * num_convert), 6)

            if unidade_nome['text'] in ('Tempo', 'Área', 'Velocidade'):
                result = round((entrada[b] / entrada[a] * num_convert), 6)
        except ValueError:
            result = 'Valor não aceito!'
        except KeyError:
            result = 'Escolha as medidas!'

        label_result['text'] = result

    label_info = Label(frame_right, text="Digite o valor", width=0, height=0, padx=5, pady=3, bg=color1, fg=color2, relief="flat", anchor="center", font=('Arial 10 bold'))
    label_info.place(x=5, y=100)

    entry_numero = Entry(frame_right, width=11, font=('Arial 10 bold'), justify="center", relief=SOLID)
    entry_numero.place(x=105,y=104)

    b_calculate = Button(frame_right, command=calcular, text="Calcular", width=22, height=1, relief="raised", bg=color3, fg=color2, overrelief="ridge", font=('Arial 10 bold'))
    b_calculate.place(x=5, y=156)

    label_result = Label(frame_right, text="00000000", width=17, height=0, padx=5, pady=3, relief="groove", anchor="center", font=('Arial 12 bold'))
    label_result.place(x=5, y=205)

img_0 = Image.open('images/balanca.png')
img_0 = img_0.resize((40, 40), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_left, command=lambda:show_menu('Massa'), text="Peso", width=205, height=40, image=img_0, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_0.grid(row=0, column=0, sticky=NSEW, pady=5, padx=5)

img_1 = Image.open('images/clock.png')
img_1 = img_1.resize((40, 40), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_left, command=lambda:show_menu('Tempo'), text="Tempo", width=205, height=40, image=img_1, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_1.grid(row=0, column=1, sticky=NSEW, pady=5, padx=5)

img_2 = Image.open('images/ruler.png')
img_2 = img_2.resize((40, 40), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_left, command=lambda:show_menu('Comprimento'), text="Comprimento", width=205, height=40, image=img_2, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_2.grid(row=1, column=0, sticky=NSEW, pady=5, padx=5)

img_3 = Image.open('images/area.png')
img_3 = img_3.resize((40, 40), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_1 = Button(frame_left, command=lambda:show_menu('Área'), text="Área", width=205, height=40, image=img_3, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_1.grid(row=1, column=1, sticky=NSEW, pady=5, padx=5)

img_4 = Image.open('images/quantity.png')
img_4 = img_4.resize((40, 40), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_left, command=lambda:show_menu('Volume'), text="Volume", width=205, height=40, image=img_4, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_4.grid(row=2, column=0, sticky=NSEW, pady=5, padx=5)

img_5 = Image.open('images/speed.png')
img_5 = img_5.resize((40, 40), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_left, command=lambda:show_menu('Velocidade'), text="Velocidade", width=205, height=40, image=img_5, compound=LEFT, anchor="nw", relief=FLAT, overrelief=SOLID, bg=color3, fg=color2, font=('Arial 10 bold'))
b_5.grid(row=2, column=1, sticky=NSEW, pady=5, padx=5)

unidade_nome = Label(frame_right, text="Unidade", width=16, height=2, padx=0, relief="flat", bg=color1, fg=color2, anchor="center", font=('Arial 15 bold'))
unidade_nome.place(x=0, y=0)

unidade_de = Label(frame_right, text="De", height=1, padx=3, relief="flat",bg=color1, fg=color2, anchor="center", font=('Arial 10 bold'))
unidade_de.place(x=10, y=58)

combo_de = ttk.Combobox(frame_right, width=5, justify=("center"), font=('Arial 8 bold'))
combo_de.place(x=38, y=58)

unidade_para = Label(frame_right, text="Para", height=1, padx=3, relief="flat",bg=color1, fg=color2, anchor="center", font=('Arial 10 bold'))
unidade_para.place(x=95, y=58)

combo_para = ttk.Combobox(frame_right, width=5, justify=("center"), font=('Arial 8 bold'))
combo_para.place(x=135, y=58)

janela.mainloop()
