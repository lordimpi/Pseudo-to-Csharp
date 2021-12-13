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
    for i in range(1, len(pseudo)-1, 1):
        cadenas = pseudo[i].split(" ")
        j = 0
        listaCodigo.append("\t\t\t")
        while j < len(cadenas):
            EsClave = False
            for element in Diccionario:
                if element.get(cadenas[j]) != None:
                    listaCodigo.append(element[cadenas[j]])
                    EsClave = True
                    break
            if not EsClave:
                listaCodigo.append(" " + cadenas[j])
                if j < len(cadenas)-1:
                    listaCodigo.append(" ")
            j = j + 1
            if j == len(cadenas):
                cadena = str(cadenas[len(cadenas)-1])
                cadena = cadena.lower();
                cadena = cadena.replace("\t","");
                if (cadena.find("fin") == -1):
                    if (cadena.find("entonces") == -1):
                        if(cadena.find("hacer") == -1):
                            listaCodigo.append(";" + "\n")
                listaCodigo.append("\n")
    return listaCodigo


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
    print("Codigo C# generado con exito...")
else:
    print("No se puede generar codigo c#")
