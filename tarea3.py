# -*- coding: utf-8 -*

#Para todas las funciones 'input_mode' representa el formato de input donde
# 0 -> CSV
# 1 -> DL Matricial
# 2 -> DL Lista
#'graph_path' representa la ruta del archivo donde se encuentra el grafo
#'vertex' representa al vertice al que se le calcularan las métricas (los vertice se enumeran desde 0)

#Funcion que retorna el tipo de  formato que eso el grafo
def tipo_archivo(graph_path):
    grafo = open(graph_path,"r")
    #lineas_grafo = readlines(grafo)
    #linea1 = lineas_grafo[0]
    linea1 = grafo.readline()
    if "N" in linea1:
        linea2 = grafo.readline()
        n = int(linea1[2:-1]) 
        if n != 2:
            if linea2.find(" ") != linea2.rfind(" "):
                grafo.close()
                return(1)
            else:
                grafo.close()
                return(2)
        else:
            return(3) # no es posible diferenciar 100% una red  de menos de 3 nodos entre 1 y 2 
    else:
        grafo.close()    
        return(0)

#Funcion que retorna la informacion del grafo, independiente del formato
#def info_grafo(graph_path, input_mode):
    
    #pass
    


#Calcula el in degree de un vertice dado en un grafo
def in_degree(graph_path, input_mode, vertex):
    result = 0
    #formato = tipo_archivo(graph_path)
    grafo = open(graph_path,"r")
    if input_mode == 0:
        linea1 = grafo.readline()
        num_nodos = int(linea1[0:-1])
        nodo = 0 
        while nodo < num_nodos:
            linea = grafo.readline()
            if nodo != vertex:
                division = linea.split(",")
                if vertex != len(division):
                    if int(division[vertex]) == 1:
                        result += 1
                else:
                    if int((division[vertex])[0:-1]) == 1:
                        result += 1
            nodo += 1
    elif input_mode == 1:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
        nodo = 0
        while nodo < num_nodos:
            linea = grafo.readline()
            if nodo != vertex:
                division = linea.split(" ")
                if vertex != len(division):
                    if int(division[vertex]) == 1:
                        result += 1
                else:
                    if int((division[vertex])[0:-1]) == 1:
                        result += 1
            nodo+=1
    elif input_mode == 2:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
        try:
            while (True):
                linea = grafo.readline()
                division = linea.split(" ")
                if ((division[1])[-1]) == " \n":
                    if int((division[1])[0:-1]) == vertex:
                        result += 1
                else:
                    if int(division[1]) == vertex:
                        result += 1
        except:
            grafo.close()
            return(result)
    grafo.close()                
    return result

#Calcula el out degree de un vertice dado en un grafo 
def out_degree(graph_path, input_mode, vertex):
    result = 0
    #formato = tipo_archivo(graph_path)
    grafo = open(graph_path,"r")
    if input_mode == 0:
        linea1 = grafo.readline()
        num_nodos = int(linea1[0:-1])
        nodo = 0 
        while nodo < num_nodos:
            linea = grafo.readline()
            if nodo == vertex:
                division = linea.split(",")
                if nodo != num_nodos - 1:
                    for i in division[0:-1]:
                        if int(i) == 1:
                            result += 1
                    if int((division[-1])[0:-1]) == 1:
                        result += 1
                else:
                    for i in division:
                        if int(i) == 1:
                            result += 1
                break
            nodo += 1
    elif input_mode == 1:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
        nodo = 0
        while nodo < num_nodos:
            linea = grafo.readline()
            if nodo == vertex:
                division = linea.split(" ")
                if nodo != num_nodos - 1:
                    for i in division:
                        if int(i) == 1:
                            result += 1
                    if int((division[-1])[0:-1]) == 1:
                        result += 1
                    break
                else:
                    for i in division:
                        if int(i) == 1:
                            result += 1                    
                break    
            nodo+=1
    elif input_mode == 2:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
        try:
            while (True):
                linea = grafo.readline()
                division = linea.split(" ")
                if int(division[0]) == vertex:
                    result += 1
        except:
            grafo.close()
            return(result)
    grafo.close()
    return result
	
#Calcula el degree de un vertice dado en un grafo
def degree(graph_path, input_mode, vertex):
    out_d = out_degree(graph_path, input_mode, vertex)
    in_d = in_degree(graph_path, input_mode, vertex) 
    return out_d + in_d
	
#Calcula el local clustering coefficient de un vertice dado en un grafo
def local_clustering_coefficient(graph_path, input_mode, vertex):
    u = input_mode + 1
    vertice = vertex
    nom_archivo = graph_path
    grafo=open(nom_archivo,"r")
    uniones=0
    contador=-2
    if u==1:
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==vertice:
                p=l[:-1].split(",")
                grafo.close()
                vertices=[i for i,val in enumerate(p) if val=="1"]
                break
        contador=-1
        grafo.close()
        grafo=open(nom_archivo,"r")
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==0:
                continue
            else:
                if "1"==l[vertice*2]:
                    if (contador-1) not in vertices:
                        vertices=vertices+[contador-1]
        grafo=open(nom_archivo,"r")
        contador=-2
        vertices=sorted(vertices)
        for i in vertices:
            for l in grafo:
                if "\n" not in l:
                    l=l+"\n"
                contador=contador+1
                if contador==i:
                    r=l[:-1].split(",")
                    vertices2=[i for i,val in enumerate(r) if val=="1"]
                    for j in vertices:
                        if i==j:
                            continue
                        elif j in vertices2:
                            uniones=uniones+1
                    break                    
    elif u==2:
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==vertice:
                p=l[:-1].split(" ")
                grafo.close()
                vertices=[i for i,val in enumerate(p) if val=="1"]
                break
        contador=-1
        grafo.close()
        grafo=open(nom_archivo,"r")
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==0:
                continue
            else:
                if "1"==l[vertice*2]:
                    if (contador-1) not in vertices:
                        vertices=vertices+[contador-1]
        grafo=open(nom_archivo,"r")
        contador=-2
        vertices=sorted(vertices)
        for i in vertices:
            for l in grafo:
                if "\n" not in l:
                    l=l+"\n"
                contador=contador+1
                if contador==i:
                    r=l[:-1].split(" ")
                    vertices2=[i for i,val in enumerate(r) if val=="1"]
                    for j in vertices:
                        if i==j:
                            continue
                        elif j in vertices2:
                            uniones=uniones+1
                    break
    elif u==3:
        vertices=[]
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==-1:
                continue
            if str(vertice)==(l[:(l.index(" "))]):
                vertices=vertices+[int(l[(l.index(" "))+1:-1])]
            elif vertices!=[]:
                grafo.close()
                break
        grafo=open(nom_archivo,"r")
        contador=-1
        for l in grafo:
            if "\n" not in l:
                l=l+"\n"
            contador=contador+1
            if contador==0:
                continue
            else:
                if str(vertice)==l[(l.index(" ")+1):-1]:
                    if int(l[:(l.index(" "))]) not in vertices:
                        vertices=vertices+[int(l[:(l.index(" "))])]  
        grafo.close()
        vertices=sorted(vertices)
        for i in vertices:
            for j in vertices:
                grafo=open(nom_archivo,"r")
                prim_linea=1
                for l in grafo:
                    if "\n" not in l:
                        l=l+"\n"
                    if prim_linea==1:
                        prim_linea=0
                    elif i==j:
                        break
                    elif str(i)+" "+str(j)+"\n"==l:
                        uniones=uniones+1
                        break
                    elif int(i)<int(l[:(l.index(" "))]):
                        break
                grafo.close()
    grafo.close()
    ki=len(vertices)
    if ki==0:
        return (0)
    else:
        return float(uniones)/(ki*(ki-1))



#Calcula el network average clustering coefficient de un grafo 
def clustering_coefficient(graph_path, input_mode):
    result = 0
    grafo = open(graph_path,"r")
    if input_mode == 0:
        linea1 = grafo.readline()
        num_nodos = int(linea1[0:-1])            
    elif input_mode == 1:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
    elif input_mode == 2:
        linea1 = grafo.readline()
        num_nodos = int(linea1[2:-1])
    grafo.close()
    nodo = 0
    suma = 0
    while nodo < num_nodos:
        suma += local_clustering_coefficient(graph_path, input_mode, nodo)
        nodo+=1
    result = float(suma)/num_nodos
    return result
    


#poner ruta del archivo
#path = "archivo.txt"

#para porbar indegree:
#print(in_degree(path, tipo_archivo(path), vertice))

#para porbar outdegree:
#print(out_degree(path, tipo_archivo(path), vertice))

#para porbar indegree:
#print(degree(path, tipo_archivo(path), vertice))

#para probar local_clustering_coefficient
#print(local_clustering_coefficient(path, tipo_archivo(path), vertice))

#para probar clustering_coefficient
#print(clustering_coefficient(path, tipo_archivo(path)))
