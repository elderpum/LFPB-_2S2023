# Libreria Graphviz
# https://graphviz.org/download/
# pip install graphviz

# Libreria Reportlab
# https://www.reportlab.com/dev/install/installation/
# pip install reportlab

# Libreria Tkinter
# https://docs.python.org/3/library/tkinter.html
# pip install tk

# Importamos las librerias
import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4   

def generarDOT():
    dot = Digraph('AFD', filename='AFDPrueba', format='png')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('B')
    dot.attr('node', shape='circle')
    dot.node('A')
    dot.edge('A', 'B', label='1') # A,1;B
    dot.render('AFDPrueba', view=False)

def mostrarDOT():
    webbrowser.open_new_tab('AFDPrueba.png')

def generarPDF():
    w, h = A4
    pdf = canvas.Canvas("Reporte.pdf", pagesize=A4)
    pdf.setTitle("Reporte de AFD")
    text = pdf.beginText(50, h - 50)
    text.setFont("Times-Roman", 12)
    text.textLine("AFD")
    text.textLine("Alfabeto: 1")
    text.textLine("Estados: A, B")
    text.textLine("Estado inicial: A")
    text.textLine("Estado final: B")
    text.textLine("Transiciones:")
    text.textLine("A,1;B")
    text.textLine()
    text.textLine("AFD generado con Graphviz")
    pdf.drawText(text)
    pdf.drawInlineImage("AFDPrueba.png", 100, 0, width=200, height=200, preserveAspectRatio=True)
    pdf.save()
    webbrowser.open_new_tab('Reporte.pdf')

def mostrarVentanaPrincipal():
    ventanaPrincipal.deiconify()
    ventanaSecundaria.withdraw()

def mostrarVentanaSecundaria():
    ventanaSecundaria.deiconify()
    ventanaPrincipal.withdraw() 

# Creamos las ventanas
ventanaPrincipal = tk.Tk()
ventanaSecundaria = tk.Toplevel(ventanaPrincipal)

# Definir ventana principal
ventanaPrincipal.title("Ventana Principal")
btnImprimir = tk.Button(ventanaPrincipal, text="Imprimir Grafo", command=mostrarDOT)
btnImprimir.pack()

btnMostrarDatos = tk.Button(ventanaPrincipal, text="Mostrar Datos", command=mostrarVentanaSecundaria)
btnMostrarDatos.pack()

btnGenerarPDF = tk.Button(ventanaPrincipal, text="Generar PDF", command=generarPDF)
btnGenerarPDF.pack()

generarDOT()

# Definir ventana secundaria
ventanaSecundaria.title("Ventana Secundaria")

btnRegresar = tk.Button(ventanaSecundaria, text="Regresar", command=mostrarVentanaPrincipal)
btnRegresar.pack()

txtValores = tk.Text(ventanaSecundaria, width=40, height=10)
txtValores.pack()

txtValores.insert(tk.END, "ElderPum\n201700761")
txtValores.configure(state="disabled")

ventanaSecundaria.withdraw()

ventanaPrincipal.mainloop()