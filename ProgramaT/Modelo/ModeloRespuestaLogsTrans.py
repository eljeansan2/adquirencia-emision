import sys 

class CamRes:
    def __init__(self,fila,tipo,detalleRegistro):
        self.fila=fila
        self.tipo=tipo
        self.detalleRegistro=detalleRegistro
    
    def guardar_resp(self):
        lista1=[self.fila,self.tipo,self.detalleRegistro]
        f=open("ProgramaT\Archivos\ArchivoListaTemporalCAMPOS.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("', ['","'	'").replace(", '","'	'").replace(r"\n']]","]]"))
        f.write("\n")      
        f.close()
    def guardar_resp2(self):
        lista1=[self.fila,self.tipo,self.detalleRegistro]
        f=open("ProgramaT\Archivos\ArchivoListaTemporalValidacion.txt",'a+',encoding="utf-8")
        f.write((str(lista1)).replace("', '","'	'").replace("', ['","'	'").replace(", '","'	'").replace(r"\n']]","]]"))
        f.write("\n")      
        f.close()        


