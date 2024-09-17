import sys 

class CamRes:
    def __init__(self,tipo,filaa,detalleIndividual):
        self.tipo=tipo
        self.filaa=filaa
        self.detalleIndividual=detalleIndividual
    
    def guardar_resp(self):
        lista1=[self.tipo,self.filaa,self.detalleIndividual]
        f=open("ProgramaT\Archivos\ArchivoListaTemporalCAMPOS.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("',","'	'").replace(", ['","'	'").replace("' ['","'").replace("ok-Campo-","ok-"))
        f.write("\n")
        f.close()
    def guardar_resp2(self):
        lista1=[self.tipo,self.filaa,self.detalleIndividual]
        f=open("ProgramaT\Archivos\ArchivoListaTemporalValidacion.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("',","'	'").replace(", ['","'	'").replace("' ['","'").replace("ok-Campo-","ok-"))
        f.write("\n")
        f.close() 
