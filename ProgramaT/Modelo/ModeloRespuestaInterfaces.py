import sys 

class CamRes:
    def __init__(self,tipo,tiporeg,filaa,detalleRegistro,detalleComun,detalleIndividual):
        self.tipo=tipo
        self.tiporeg=tiporeg
        self.filaa=filaa
        self.detalleRegistro=detalleRegistro
        self.detalleComun=detalleComun
        self.detalleIndividual=detalleIndividual
    
    def guardar_resp(self):
        lista1=[self.tipo,self.tiporeg,self.filaa,self.detalleRegistro,self.detalleComun,self.detalleIndividual]
        f=open(r"ProgramaT\Archivos\ArchivoListaTemporalCAMPOS.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("',","'	'").replace("'], ['","'	'").replace(", ['","'	'").replace("['Registro'","'Registro'"))
        f.write("\n")      
        f.close()
    def guardar_resp2(self):
        lista1=[self.tipo,self.tiporeg,self.filaa,self.detalleRegistro,self.detalleComun,self.detalleIndividual]
        f=open(r"ProgramaT\Archivos\ArchivoListaTemporalValidacion.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("',","'	'").replace("'], ['","'	'").replace(", ['","'	'").replace("['Registro'","'Registro'"))
        f.write("\n")      
        f.close()    


