"""
@Luis Alejandro Vejarano Gutierrez
@Johan Sebastián Miranda
@Manuel Torres

PROYECTO COVID 19 COLOMBIA
"""
import matplotlib.pyplot as pt #Uso de Gráficas
from numpy.linalg import inv #Calculo de la matriz inversa
import numpy as ny #Manejo de grandes arreglos

def prediCol(meses,cant,hoy):
    mes=[3,4,5,6,7,8,9,10,11]
    X = ny.array([ny.ones(len(mes)), mes]).T #Arreglo numpy
    a = inv(X.T @ X) @ X.T @ cant #Formula para minimizar cuadrados

    fig8, ax = pt.subplots(figsize=(20, 10))
    ax.set_title('REGRESIÓN LINEAL DATOS DE COVID EN COLOMBIA')
    x_predict = ny.linspace(3, 11, num=100)
    subs_predict = a[0] + a[1] * x_predict #Realiza la predicción con la fórmula
    pt.scatter(mes, cant) #Grafica
    pt.xlabel('Meses');
    pt.ylabel('Cantidad de Infectados');
    pt.plot(x_predict, subs_predict, 'c')
    fig8.tight_layout()
    fname="RegresionLineal_Covid_Colombia_"+hoy+".png"
    pt.savefig(fname, bbox_inches='tight')
    arY=[]
    arY1=[]
    for i in range(12,19): #Ciclo para las predicciones en diciembre y el siguiente semestre
        y = a[1] * (i) + a[0] #Fórmula de la recta
        y1 = f"{y:.1f}"
        arY1.append(y1)

    fig9, ax = pt.subplots(figsize=(20, 10))
    ax.set_title('PROYECCIÓN DE CONTAGIOS POR MES EN COLOMBIA')
    mesP=['Diciembre',"21Enero","21Febrero","21Marzo","21Abril","21Mayo","21Junio"] #Arreglo de Meses donde 21 es por el otro año
    pt.xlabel('Meses Siguientes')
    pt.ylabel('Cantidad')
    pt.plot(mesP, arY1,marker="o", color="red") #Grafica
    fig9.tight_layout()
    fname="Proyeccion_Covid_Colombia_"+hoy+".png"
    pt.savefig(fname, bbox_inches='tight')
    pt.show()
