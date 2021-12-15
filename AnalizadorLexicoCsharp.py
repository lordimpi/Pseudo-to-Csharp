'''
/**
* +--------------------------------------------------------------------------------------+
* | ESTUDIANTE: Santiago Acuña Obando – cocox-26@unicauca.edu.co |
    ESTUDIANTE: Daniel Zambrano – danielzambrano@unicauca.edu.co | 
* | FECHA: 2021/12/15 |
* +--------------------------------------------------------------------------------------+
'''
def generar_ClaseCsharp(plantillaPseudocodigo):
    archivo = open("codigoCsharp.cs", "w")
    cadena = plantillaPseudocodigo[0].split(" ")
    llave = cadena[0]
    archivo.writelines("Using System;\n\n")
    for element in Diccionario:
        if element.get(llave) != None:
            archivo.writelines("\tclass program\n")
            archivo.writelines("\t{\n")
            if funciones:
                archivo.writelines(escribir_Codigo(PseudoCodigoFunciones, 0))
            archivo.writelines("\t\tvoid Main(string[] args)\n")
            archivo.writelines("\t\t{\n")
            if len(plantillaPseudocodigo) > 2:
                archivo.writelines(escribir_Codigo(plantillaPseudocodigo, 1))
            archivo.writelines("\t\t}\n")
            archivo.writelines("\t}\n")
            archivo.close()
            return


def escribir_Codigo(pseudo, func):
    listaCodigo = []
    for index in range(func, len(pseudo)-1, 1):
        EsPara = False
        cadenas = pseudo[index].split(" ")
        indexCadena = 0
        listaCodigo.append("\t\t\t")
        while indexCadena < len(cadenas):
            EsClave = False
            for element in Diccionario:
                if element.get(cadenas[indexCadena]) != None:
                    listaCodigo.append(element[cadenas[indexCadena]])
                    if(listaCodigo[len(listaCodigo)-1] == "for("):
                        EsPara = True
                    EsClave = True
                    break
            if not EsClave:
                if EsPara:
                    nuevaLinea = crear_para(
                        cadenas[indexCadena], cadenas, indexCadena)
                    if nuevaLinea != None:
                        listaCodigo.append(nuevaLinea)
                        indexCadena = indexCadena + 6
                if not EsPara:
                    listaCodigo.append(" " + cadenas[indexCadena])
                if indexCadena < len(cadenas)-1:
                    listaCodigo.append(" ")
            indexCadena = indexCadena + 1
            if indexCadena == len(cadenas):
                cad = str(cadenas[len(cadenas)-1])
                cad = cad.lower()
                escribir = str(cadenas).lower()
                if escribir.find("escribir") != -1:
                    listaCodigo.append(");")
                if escribir.find("break") != -1:
                    listaCodigo.append(";");
                else:
                    if (cad.find("") == -1):
                        if (cad.find("{") == -1):
                            if (cad.find("}") == -1):
                                if (cad.find(":") == -1):
                                    if (cad.find(";") == -1):
                                        if (cad.find("sino") == -1):
                                            if (cad.find("hacer") == -1):
                                                if (cad.find("fin") == -1):
                                                    if (cad.find("entonces") == -1):
                                                        listaCodigo.append(";" + "\n")
                listaCodigo.append("\n")
    return listaCodigo


def paraRecur(linea, posicionlinea, CadenaPara, cad):
    if posicionlinea < len(linea):
        if BusquedaClave(linea[posicionlinea]) != None:
            if posicionlinea != 5:
                CadenaPara = CadenaPara + BusquedaClave(linea[posicionlinea])
            else:
                CadenaPara = CadenaPara + " " + \
                    linea[posicionlinea-4] + " " + \
                    BusquedaClave(linea[posicionlinea])
            if posicionlinea == len(linea)-1:
                cad.append(CadenaPara)
            posicionlinea = posicionlinea + 1
            paraRecur(linea, posicionlinea, CadenaPara, cad)
        else:
            CadenaPara = CadenaPara + " " + linea[posicionlinea]
            posicionlinea = posicionlinea + 1
            paraRecur(linea, posicionlinea, CadenaPara, cad)


def crear_para(indice, linea, posicionlinea):
    CadenaPara = indice + " = 0; " + indice + " "
    posicionlinea = posicionlinea + 1
    cad = []
    paraRecur(linea, posicionlinea, CadenaPara, cad)
    return cad[0]


def BusquedaClave(ClaveBuscar):
    for element in Diccionario:
        if element.get(ClaveBuscar) != None:
            return element[ClaveBuscar]
    return None


def crear_diccionario(plantillaTablaLexica):
    for i in range(len(plantillaTablaLexica)):
        linea = plantillaTablaLexica[i].split(" ")
        Diccionario.append({linea[0]: linea[1].replace("\n", "")})


'================================================================================================='
Diccionario = []
PseudoCodigo = []
PseudoCodigoFunciones = []
funciones = False
x = True
with open("pseudocodigo.txt", "r") as fPsd:
    contentPsd = fPsd.readlines()
    fPsd.close()
    for element in contentPsd:
        cad = element.replace("\n", "")
        cad = cad.replace("\t", "")
        cad = cad.replace("\'", "\"")
        cad = cad.replace("(", " (")
        if cad.find("principal") == -1 and x:
            PseudoCodigoFunciones.append(cad)
        else:
            x = False
            PseudoCodigo.append(cad)
    if PseudoCodigoFunciones != None:
        funciones = True

with open("tablaLexica.txt", "r") as fTbl:
    contentTbl = fTbl.readlines()

try:
    crear_diccionario(contentTbl)
    generar_ClaseCsharp(PseudoCodigo)
    print("CODIGO C# GENERADO CON EXITO...")
except:
    print("No se puede generar codigo c#")
