import sys

class CamCampos:
        def __init__(self,tipoRegistro,nombre,long,tipo,Nulo,pos_inicial,pos_final):
                self.tipoRegistro=tipoRegistro
                self.nombre=nombre
                self.long=long
                self.tipo=tipo
                self.Nulo=Nulo
                self.pos_inicial=pos_inicial
                self.pos_final=pos_final
        def guardar_campos(self):
                listal=[self.tipoRegistro,self.nombre,self.long,self.tipo,self.Nulo,self.pos_inicial,self.pos_final]
                listaCampos.append(listal)

listaCampos=list()