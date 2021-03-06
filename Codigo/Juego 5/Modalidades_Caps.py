# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Caps.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
sys.path.append("..") #Necesario para poder importar basedatos
import bd #Importa el script bd.py
import numpy as np
import numpy.random as rnd


class Craps:
    def __init__(self):
        self.saldo = 0
        self.dinGanado = 0
        self.dado1 = 0
        self.dado2 = 0
        self.transaccion = 0
        self.ActualizarSaldo()
        print("JUEGO DE CRAPS INICIADO")
    def ActualizarSaldo(self):
        self.saldo = bd.traerValor()
        
    def getData(self):
        return [self.saldo,self.transaccion]

    def Mod1(self,apuesta,dado1,dado2):
        self.cuota = 1.2
        if (dado1 + dado2) != 7:
            return self.cuota * apuesta
        else:
            return 0
    def Mod2(self,apuesta,dado1,dado2):
        self.cuota = 1.5
        self.suma = dado1 + dado2
        if self.suma != 2 and self.suma != 3 and self.suma != 12:
            return self.cuota * apuesta
        else:
            return 0
    def Mod3(self,apuesta,dado1,dado2):
        self.cuota = 2
        if ((dado1 % 2) == 0 or (dado2 % 2) == 0):
            return self.cuota * apuesta
        else:
            return 0

    def Mod4(self,apuesta):
        self.repeat = True    
        self.cuota = 4.5
        while(self.repeat):
            self.dado1 = rnd.randint(1,7,1)
            self.dado2 = rnd.randint(1,7,1)
            if(self.dado1+self.dado2==7 or self.dado1+self.dado2==11):
                self.repeat = False
                return self.cuota * apuesta
            elif(self.dado1+self.dado2==2 or self.dado1+self.dado2==3 or self.dado1+self.dado2==12):
                self.repeat = False
                return 0

    def Mod5(self,apuesta,dado1,dado2,dado1P,dado2P):
        self.cuota = 36    
        if dado1 == dado1P and dado2 == dado2P or dado1 == dado2P and dado2 == dado1P:
            return self.cuota * apuesta
        else:
            return 0

    def Apostar(self, _mod,_apuesta,_dado1 = 0,_dado2 = 0):
        self.dado1 = rnd.randint(1,7,1)
        self.dado2 = rnd.randint(1,7,1)
        self.dinGanado = 0
        
        #Recibo parametros
        self.ActualizarSaldo()
        if self.saldo <= _apuesta:
            return False
        else:
            if _mod == 1:
                self.dinGanado = self.Mod1(_apuesta,self.dado1,self.dado2)
            elif _mod == 2:
                self.dinGanado = self.Mod2(_apuesta,self.dado1,self.dado2)
            elif _mod == 3:
                self.dinGanado = self.Mod3(_apuesta,self.dado1,self.dado2)
            elif _mod == 4:
                self.dinGanado = self.Mod4(_apuesta)
            elif _mod == 5:
                self.dinGanado = self.Mod5(_apuesta,self.dado1,self.dado2,_dado1,_dado2)
            else:
                print("MODALIDAD INCORRECTA")

            self.transaccion = self.dinGanado - _apuesta
            self.saldo += self.transaccion
            bd.insertarDatos(self.saldo,self.transaccion)
            return True
