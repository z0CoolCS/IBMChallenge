from bs4 import BeautifulSoup as bs
import requests as req
import json


# Crea el set de stepwords
# Action: crea el objeto set de python con todos los stepwords insertados desde archivo filename
def get_stopwords (filename):
    stepwords = []
    with open("stopwords") as f:
        for line in f.readlines():
            for word in line.split(" "):
                stepwords.append(word.strip())
    stepwords = set(stepwords)
    return stepwords


# Genera el title de un json file
# Action: Remueve los stopwords
def generate_title  (stepwords, body):
    title_new = ""
    for word in body.split(" "):
        if word in stepwords:
            continue
        title_new += " " + word
    return title_new


# Verifica si existe un archivo JsonFile con el mismo title
# Action: itera sobre todos los archivos json ya insertados 
def exist_jsonFiles (data, jsonfiles):
    #print("----------------- Checking Duplicity --------------")
    for jsonfile in jsonfiles:
        if jsonfile['title'] == data['title']:
            return True
    return False

def create_objectJson (body, url, stepwords):
    global jsonfiles
    data = {}
    data['body'] = ''.join(l for l in body if l.isalnum() or l == ' ')
    data['url'] = url 
    data['title'] = generate_title(stepwords, data['body'])
    if not exist_jsonFiles(data, jsonfiles) :
        jsonfiles.append(data)


# Genera el archivo Json 
# Action: crea el archivo json file dentro de la carpeta definida por path 
def generate_jsonFile (path, data, cont):
    with open(path + str(cont) + ".json", "w") as json_file:
        json.dump(data, json_file, indent = 4, ensure_ascii = False)


# Genera todos los archivos Json 
# Action: crea todos los archivos archivo json file dentro de la carpeta definida por path 
def create_JsonFiles (path, jsonfiles):
    for index, data in enumerate(jsonfiles):
        generate_jsonFile(path, data, index)

def check_EachJsonFile (path, jsonfiles):
    cont = 1
    for index, data in enumerate(jsonfiles):
        print(" ")
        print(f"---------- Json File numero {index + 1} ---------- ")
        print(data['body'])
        ans = int(input("Desea contruis este json object? [si=1, no=0]: "))
        if (ans) :
            generate_jsonFile(path, data, cont)
            cont += 1


urls = [
    "https://desarrolloweb.com/articulos/introduccion-componentes-angular2.html",
    "https://www.acontracorrientech.com/directives-en-angular-guia-practica",
    "https://medium.com/@ogomez/guia-rapida-para-entender-el-patron-redux-y-angular-con-ngrx-e60d39d35f1b",
    "https://profile.es/blog/angular-templates-las-directivas-ng-template-ng-container-y-ngtemplateoutlet/",
    "https://guru99.es/java-interface/",
    "https://www.oscarblancarteblog.com/2017/02/28/ordenar-listas-en-java/",
    "https://www.javanicaragua.org/2019/09/21/introduccion-a-maven-primeros-pasos/",
    "https://desarrolloweb.com/articulos/servicios-angular.html",
    "https://desarrolloweb.com/articulos/trabajar-modulos-angular.html",
    "https://www.adictosaltrabajo.com/2015/09/25/introduccion-a-colecciones-en-java"
    ]

stepwords = get_stopwords("stopwords")
path_file = "json/"
jsonfiles = []

for url in urls:
    page = req.get(url)
    soup = bs(page.content, "html.parser")
    ps = soup.find_all("p")
    title = soup.title.string

    for i in ps:
        body = i.get_text()
        body = body.lower()
        if "component" in body:
            create_objectJson(body, url, stepwords) 

        if "directiv" in body:
            create_objectJson(body, url, stepwords) 

        if "servic" in body:
            create_objectJson(body, url, stepwords) 

        if "modulo" in body or "módulo" in body or "modulos" in body or "módulos" in body or "module" in body:
            create_objectJson(body, url, stepwords) 

        if "redux" in body or "patr" in body:
            create_objectJson(body, url, stepwords) 

        if "ng-container" in body or "ng-template" in body:
            create_objectJson(body, url, stepwords) 

        if "abstract" in body or "interf" in body:
            create_objectJson(body, url, stepwords) 

        if "colecci" in body or "object" in body:
            print(body)
            create_objectJson(body, url, stepwords) 

        if "map" in body:
            create_objectJson(body, url, stepwords) 

        if "set" in body:
            create_objectJson(body, url, stepwords) 

        if "list" in body:
            create_objectJson(body, url, stepwords) 

        if "singleton" in body:
            create_objectJson(body, url, stepwords) 

        if "implement" in body:
            create_objectJson(body, url, stepwords) 

        if "strategy" in body:
            create_objectJson(body, url, stepwords) 

        if "pom" in body or "maven" in body:
            create_objectJson(body, url, stepwords) 


build_aut = input("Desea construir los json files automaticamente? [si/no]:")
if build_aut == "no":
    check_EachJsonFile(path_file, jsonfiles)
else:
    create_JsonFiles(path_file, jsonfiles)

print("---------------------------------------------------------------------")
print("----------------- Archivos Json Creados Exitosamente!! --------------")
print("---------------------------------------------------------------------")

#title = soup.find_all("title")
#for x in title:
#    print(x.attrs.get("title"))
#print(title)
#print(title[0].attrs.get("title"))
'''
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)
print(title[0].string)
print(title[0].text)
'''
