from hospital import Hospital
from paciente import Paciente
from atencion import AtencionMedica, AtencionFarmacia

def aBooleano(valor):
    return str(valor).strip().lower() in ("true", "1", "si")

def cargarPacientes(nombre_archivo="./data/pacientes.csv"):
    pacientes = {}
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        archivo.readline()  # Saltear cabecera
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            campos = linea.split(",")
            codigo_atencion = int(campos[0])
            nombre = campos[1]
            sintoma = int(campos[2])
            habitual = aBooleano(campos[3])
            
            # Paciente no lleva codigo en su constructor segun los tests
            paciente = Paciente(nombre, sintoma, habitual)
            pacientes[codigo_atencion] = paciente
    return pacientes

def cargarAtencionesMedicas(pacientes, nombre_archivo="./data/atenciones_medicas.csv"):
    atencionesMedicas = []
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            campos = linea.split(",")
            codigo = int(campos[0])
            tipo_cobro = int(campos[1])
            importe = float(campos[2])
            
            paciente = pacientes[codigo]
            atencion = AtencionMedica(codigo, tipo_cobro, paciente, importe)
            atencionesMedicas.append(atencion)
    return atencionesMedicas

def cargarAtencionesFarmacia(nombre_archivo="./data/atenciones_farmacia.csv"):
    atencionesFarmacia = []
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        archivo.readline()
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            campos = linea.split(",")
            codigo = int(campos[0])
            tipo_cobro = int(campos[1])
            importeTotal = float(campos[2])
            descuento = float(campos[3])
            
            atencion = AtencionFarmacia(codigo, tipo_cobro, importeTotal, descuento)
            atencionesFarmacia.append(atencion)
    return atencionesFarmacia




def cargarHospital():
    hospital = Hospital("Hospital San Roque")
    pacientes = cargarPacientes()
    medicas = cargarAtencionesMedicas(pacientes)
    farmacia = cargarAtencionesFarmacia()
    
    for a in medicas:
        hospital.addAtencion(a)
    for a in farmacia:
        hospital.addAtencion(a)
        
    return hospital

def main():
    hospital = cargarHospital()
    print(hospital)
    print("-"*200)
    print(f"Total consultas medicas: ${hospital.importe_total_atencion_consulta():.2f}")
    print(f"Codigo primera atencion habitual: {hospital.codigo_primera_atencion_habitual()}")


    


if __name__ == "__main__":
    main()