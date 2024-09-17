import sys

class CamCampos:
    def __init__(self,name,sizeLen,Len,formatoCampo,bit,formatoLen,Proteger,bcdrellenoZero,bcdrellenofinal,tipoDato,bcdLeninbytes):
        self.name=name
        self.sizeLen=sizeLen
        self.Len=Len    
        self.formatoCampo=formatoCampo         
        self.bit=bit       
        self.formatoLen=formatoLen
        self.Proteger=Proteger
        self.bcdrellenoZero=bcdrellenoZero
        self.bcdrellenofinal=bcdrellenofinal
        self.tipoDato=tipoDato
        self.bcdLeninbytes=bcdLeninbytes   
    def guardar_campos(self):
        listal=[self.name,self.sizeLen,self.Len,self.formatoCampo,self.bit,self.formatoLen,self.Proteger,self.bcdrellenoZero,self.bcdrellenofinal,self.tipoDato,self.bcdLeninbytes]
        listaCamposLogs.append(listal)

listaCamposLogs=list()

