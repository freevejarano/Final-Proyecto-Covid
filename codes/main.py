"""
@Luis Alejandro Vejarano Gutierrez
@Johan Sebastián Miranda
@Manuel Torres

PROYECTO COVID 19 COLOMBIA
"""
# Importa las clases
import Colombia
import ColombiaRegiones
import MapaColombia
import Bogota
import BogotaLocalidades
import MapaBogota
import RegresionColombia as rC
import RegresionBogota as rB
# Se hace el llamado a cada clase
# Se ejecuta la siguiente clase una vez que se cierran todas las ventanas de la actual

ColombiaRegiones.ColReg() #Gráficas de Colombia por Departamentos

a,b,c=Colombia.Col() #Gráficas de Colombia

rC.prediCol(a,b,c) #Regresión y proyección Colombia

BogotaLocalidades.BogLoc() #Gráficas de Bogotá por Localidades

d,e,f=Bogota.Bog() #Gráficas de Bogotá

rB.prediBog(d,e,f) #Regresión y proyección Bogotá

MapaColombia.MapCol() #Mapa de Colombia Por Departamentos Con Los Casos de Covid

MapaBogota.MapBog() #Mapa de Calor de Bogotá Por Localidades Con Los Casos de Covid
