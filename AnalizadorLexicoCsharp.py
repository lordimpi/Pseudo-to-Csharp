def generar_ClaseCsharp(plantillaPseudocodigo):
    archivo = open("codigoCsharp.cs", "w")
    cadena = plantillaPseudocodigo[0].split(" ")
    llave = cadena[0]
    for element in Diccionario:
        if element.get(llave) != None:
            archivo.writelines(element[llave] + " " + cadena[1])
            archivo.writelines("{\n")
            archivo.writelines("\tclass program\n")
            archivo.writelines("\t{\n")
            archivo.writelines("\t\tstatic void Main(string[] args)\n")
            archivo.writelines("\t\t{\n")
            if len(plantillaPseudocodigo) > 2:
                archivo.writelines(escribir_Codigo(plantillaPseudocodigo))
            archivo.writelines("\t\t}\n")
            archivo.writelines("\t}\n")
            archivo.writelines("}")
            archivo.close()
            return

def escribir_Codigo(pseudo):
    listaCodigo = []
    for index in range(1, len(pseudo)-1, 1):
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
                    listaCodigo.append(")")
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

Diccionario = []
PseudoCodigo = []
with open("pseudocodigo.txt", "r") as fPsd:
    contentPsd = fPsd.readlines()
    fPsd.close()
    for element in contentPsd:
        PseudoCodigo.append(element.replace("\n", ""))

with open("tablaLexica.txt", "r") as fTbl:
    contentTbl = fTbl.readlines()

if contentPsd[0].find("InicioAlgoritmo") != -1 and contentPsd[len(contentPsd) - 1].find("FinAlgoritmo") != -1:
    crear_diccionario(contentTbl)
    generar_ClaseCsharp(PseudoCodigo)
    print("CODIGO C# GENERADO CON EXITO...")
else:
    print("No se puede generar codigo c#")