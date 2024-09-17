import sys 

class CamRes:
    def __init__(self,campo):
        self.campo=campo

    def guardar_resp(self):
        f=open("ProgramaT\Archivos\ArchivoListaTemporalCAMPOS.txt",'a+',encoding="utf-8")
        f.write((str(self.campo)).replace("', '","'	'").replace("', ['","'	'").replace(", '","'	'").replace(r"\n']]","]]"))
        f.write("\n")      
        f.close()
    def guardar_resp2(self):
        f=open("ProgramaT\Archivos\ArchivoListaTemporalValidacion.txt",'a+',encoding="utf-8")
        f.write((str(self.campo)).replace("', '","'	'").replace("', ['","'	'").replace(", '","'	'").replace(r"\n']]","]]"))
        f.write("\n")      
        f.close()
    


