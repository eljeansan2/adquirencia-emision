#----inicio
#---segundo comentario
import os
import concurrent.futures
from time import sleep
import json
from json import loads
from tkinter import scrolledtext as st
from datetime import datetime
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import traceback

#----------variables globales
RUTAGLOGALA=str("555")
VAROPCION=""
CARPETA1='ProgramaT\Archivos\ArchivosV2'
CARPETA2='ProgramaT\Archivos\ArchivosV2\Procesados'
#----------Primer Proceso
def __init__():print("Clase Control Lectura")
def validarTodo(ruta,varOpcion):
    #Variables
    global RUTAGLOGALA;RUTAGLOGALA=(str(ruta)).replace("/","\\").replace("/","\\") #se establece la ruta del archivo para su correcta lectura
    global VAROPCION;VAROPCION=varOpcion
    print(varOpcion)
    limpiar_carpeta_uso(CARPETA1)
    limpiar_carpeta_uso(CARPETA2)
    print(ruta)
        #Estructura1-----para interfaces de MPS2
    if(varOpcion=="Posicion Comercio"):PriEstru(r"ProgramaT\Archivos\config_adquiencia\conf_adq_posicion_comercio.json",155,157)
    elif(varOpcion=="Emisor Adquirente"):PriEstru(r"ProgramaT\Archivos\config_adquiencia\conf_adq_envio_tarifario_producto.json",160,162)
    elif(varOpcion=="Pago Comercio"):PriEstru(r"ProgramaT\Archivos\config_adquiencia\conf_adq_pago_comercios.json",146,148)
    elif(varOpcion=="Operaciones Diarias a comercios"):PriEstru(r"ProgramaT\Archivos\config_adquiencia\conf_adq_operaciones_diarias.json",155,157)
    elif(varOpcion=="Contabilidad"):SegEstru(r"ProgramaT\Archivos\config_adquiencia\conf_adq_contabilidad.json",0,2,"CO")
    #emision
    elif(varOpcion=="Contabilidad Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_contable_emision.json",0,2,"CO")
    elif(varOpcion=="Proximas a Vencer Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_proximas_vencer.json",0,2,"TV")
    elif(varOpcion=="Domiciliaciones Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_envi_resp_domiciliaciones.json",0,2,"DM")
    elif(varOpcion=="Estampacion Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_envi_resp_estampacion.json",0,2,"ET")
    elif(varOpcion=="Operaciones diarias a Comercios Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_operaciones_diarias_comercio_emision.json",155,157)
    elif(varOpcion=="Notificaciones Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_notificaciones.json",0,2,"NT")
    elif(varOpcion=="Devoluciones Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_devoluciones_sin_cobro.json",0,2,"DV")
    elif(varOpcion=="Comunicaciones Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_comunicaciones_clientes.json",35,36)
    elif(varOpcion=="Posiciones contrato Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_posicion_contrato.json",20,22)
    elif(varOpcion=="Extractos comercios Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_extractos_comercios.json",42,44)
    elif(varOpcion=="Operaciones diarias Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_operacion_diaria_emisor.json",42,44)
    elif(varOpcion=="Vigentes canceladas y amortizadas Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_vigentes_canceladas_amortizadas.json",62,64)
    elif(varOpcion=="Cuentas Baja Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_cuentas_baja.json",0,2,"BJ")
    elif(varOpcion=="Tarifario Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_tarifario.json",160,162)
    elif(varOpcion=="Bloqueos y desbloqueos Emision"):SegEstru(r"ProgramaT\Archivos\config_emision\conf_adq_bloqueo_desbloqueo.json",0,2,"BL")
    elif(varOpcion=="Posiciones a comercios Emision"):PriEstru(r"ProgramaT\Archivos\config_emision\conf_adq_posiciones_comercio_emisor.json",155,157)
    
    print('ok fin proceso')
    return "Listo"
#----------Segundo Proceso

# Código en Python para procesar el archivo adjunto
def limpiar_carpeta_uso(carpeta_borrar):
    try:
        # Verificar si la carpeta existe
        if os.path.exists(carpeta_borrar):
            # Listar todos los archivos en la carpeta
            for filename in os.listdir(carpeta_borrar):
                file_path = os.path.join(carpeta_borrar, filename)
                # Verificar si es un archivo antes de eliminarlo
                if os.path.isfile(file_path):
                    os.remove(file_path)
            return f"All files in {carpeta_borrar} have been deleted."
        else:
            return f"The folder {carpeta_borrar} does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def procesar_archivo1(file_path, output_folder, posInic,posfin):
    output_files = {}
    try:
        # Abrir el archivo original para lectura
        with open(file_path, "r",encoding='ISO-8859-15') as infile:
            # Leer línea por línea
            for i, line in enumerate(infile):
                
                
                # Validar que posInic esté dentro del rango de la línea
                if posInic + posfin > len(line):
                    return f"Invalid posInic: {posInic} for line {i+1}"
                
                # Identificar el tipo de registro
                record_type = line[posInic:posfin]

                if line[posInic:posfin] == "  ":
                    continue
                if record_type not in output_files:
                    output_files[record_type] = open(f"{output_folder}/{record_type}.txt", "w",encoding='ISO-8859-15')
                
                # Escribir la línea en el archivo correspondiente
                output_files[record_type].write(line)
                
        # Cerrar todos los archivos de salida
        for file in output_files.values():
            file.close()

        return "Processing complete, files created successfully."
    
    except Exception as e:
        traceback.print_exc()
        print('procesar_archivo1 salio error')
        return f"An error occurred: {e}"


##############################################################################
def load_config(config_file_path):
    try:
        with open(config_file_path, 'r',encoding='ISO-8859-15') as file:
            return json.load(file)
    except Exception as e:
        print('load config salio error')
        print(f"Failed to load configuration: {e}")
        return None

def process_file(p1,p2,filename, folder_path, config_by_type, output_folder):
    file_path = os.path.join(folder_path, filename)
    print(f"Detectado para procesar archivo del registro: {filename}")
    with open(file_path, 'r',encoding='ISO-8859-15') as file:
        lines = file.readlines()#######################################
    if len(lines) < 2:
        print(f"El archivo {filename} no tiene suficientes líneas.")
        return
    tipo_registro = lines[1][p1:p2].strip()
    print(f"Procesando el tipo de registro detectado: {tipo_registro}")

    if tipo_registro in config_by_type:
        detalles = config_by_type[tipo_registro]
        output_file_path = os.path.join(output_folder, f'{tipo_registro}_procesado.txt')
        with open(output_file_path, 'a',encoding='ISO-8859-15') as output_file:
            for line in lines:
                line_list = list(line)
                for detalle in detalles:
                    pos_inicial = detalle['i_pos_inicial'] - 1
                    if pos_inicial < len(line_list):
                        line_list.insert(pos_inicial, '|\t|')
                output_file.write(''.join(line_list))
        print(f"Campos divididos en: {output_file_path}")
    else:
        print(f"Tipo de registro {tipo_registro} no encontrado en la configuración de la Interfaz.")

def proceso_archivo_hilos(folder_path, config,p1,p2):
    config_by_type = {}
    for detalle in config['detalle']:
        tipo_registro = detalle['s_tipo_registro']
        if tipo_registro not in config_by_type:
            config_by_type[tipo_registro] = []
        config_by_type[tipo_registro].append(detalle)
    output_folder = os.path.join(folder_path, 'Procesados')
    os.makedirs(output_folder, exist_ok=True)
    files_to_process = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for filename in files_to_process:
            futures.append(executor.submit(process_file,p1,p2, filename, folder_path, config_by_type, output_folder))
        for future in concurrent.futures.as_completed(futures):
            future.result()

def insertar_tipo(file_path, tipo):
    with open(file_path, 'r',encoding='ISO-8859-15') as file:
        lines = file.readlines()
    
    with open(file_path, 'w',encoding='ISO-8859-15') as output_file:
        for line in lines:
            line_list = list(line)
            line_list.insert(0, tipo)
            output_file.write(''.join(line_list))
    
    print(f"Datos guardados en: {file_path}")

def PriEstru(ConfiguracionFile,p1,p2):
    config = load_config(ConfiguracionFile)
    procesar_archivo1(RUTAGLOGALA, CARPETA1,p1,p2)
    if config:
        proceso_archivo_hilos(CARPETA1, config,p1,p2)
def SegEstru(ConfiguracionFile,p1,p2,tipo):
    insertar_tipo(RUTAGLOGALA,tipo)
    config = load_config(ConfiguracionFile)
    procesar_archivo1(RUTAGLOGALA, CARPETA1,p1,p2)
    
    if config:
        proceso_archivo_hilos(CARPETA1, config,p1,p2)
