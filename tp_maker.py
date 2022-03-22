# -*- coding: utf-8 -*-

import PyPDF2
import os
import subprocess
import re

l = "{" # se definen los corchetes para 
r = "}" # poder ser utilizados en strings 

class Maker:
    def __init__(self):

        self.lenapartados = 0
        self.apartados = {}

        self.main = f"int main() {l}\n    int s = 0;\n    int a;\n    " # inicializa main, s, a y ejecuta el clrscr
        self.main += f"while(1 > 0) {l}\n        clrscr();        \n        printf(\"♥\");\n        "  #agrega un espacio para luego poner el menú e inicia el loop
        self.main += f"printf(\"\\nSeleccione un ejercicio: \");\n        scanf(\"%d\", &s);\n        switch (s) {l}\n" # obtiene el num de ejercicio e inicia el switch

        self.menu = ""
        self.functions = ""

        self.title = ""
        self.final_c = "#include <stdio.h>\n#include <stdlib.h>\n\nvoid clrscr() {\n    system(\"@cls||clear\");\n}\n" # agrega librerías

        Maker.menu(self)

    def menu(self):
        print("Welcome to tp_maker\n")
        print("\n---------\n")
        print("[1] Automatic")
        print("[2] Manual")
        option = input("Choose an option: ")
        if option == "1":
            print(Maker.auto_data(self))
        if option == "2":
            Maker.get_data(self)

    def get_data(self):
        """Obtiene los datos para generar la estructura"""
        title = input("Introduzca nombre del práctico: ")
        self.menu += title + "\\n\\n"
        self.lenapartados = int(input("Introduzca número de apartados: "))
        for a in range(self.lenapartados):
            apartado = input(f"Introduzca nombre de apartado {a+1}: ")
            self.apartados[apartado] = []
            num = int(input(f"Introduzca cantidad de ejercicios del apartado {apartado}: "))
            for i in range(num+1):
                self.apartados[apartado].append(f"Consigna de apartado {apartado} ejercicio {i}")
        Maker.build(self)

    def auto_data(self):
        """Genera la data de manera automática"""
        main_path = (os.path.dirname(os.path.abspath(__file__)))
        files = os.listdir(main_path)
        for file in files:
            if file.endswith(".txt") and file != "readme.txt":
                break
        path = (f"{main_path}\\{file}")
        try:
            with open(f"{main_path}\\{file}".format(file), "r", encoding="utf-8") as txt:
                raw_data = str(txt.read())
        except:
            return "Can't find the .txt file"

        data_list = raw_data.split("\n")
        del data_list[0]
        del data_list[0]
        self.title = data_list[0]
        del data_list[0]
        current_subtitle = ""
        for line in data_list:
            if re.search("^[a-zA-Z]", line) is not None:
                self.apartados[line.strip()] = []
                current_subtitle = line.strip()
            if re.search("^[0-9]", line) is not None:
                self.apartados[current_subtitle].append(line.strip())

        Maker.build(self)

    def build(self):
        """Genera la estructura"""
        exercice_num = 1;
        for title, exercices in self.apartados.items():
            self.menu += f"\\n--------------{title}--------------\\n\\n" # agrega un subtítulo al menú
            self.functions += f"//---------{title}---------//\n\n"
            for i in range(len(exercices)):
                self.functions += f"//{exercices[i]}\nint Ejercicio{exercice_num}() {l}\n    \n{r}\n\n" # genera las funciones y les agrega la consigna
                self.menu += f"[{exercice_num}] Ejercicio {i+1}\\n" # agrega los ejercicios al submenú
                self.main += f"            case {exercice_num}:\n                Ejercicio{exercice_num}();\n                break;\n" # agrega casos al switch
                exercice_num += 1
        self.main += f"            default:\n                printf(\"ejercicio fuera de rango\");\n                break;\n" # detector de valores incorrectos
        self.main += f"        {r}\n" # cierra el switch
        self.main += "        printf(\"\\n----------\\n\\n\");\n        " # separador
        self.main += "printf(\"Introduzca 1 para continuar o 0 para cerrar: \");\n        scanf(\"%d\", &a);\n        " # inicia el selector de cierre
        self.main += "if (a == 0) {\n            break;\n        }\n        printf(\"\\n----------\\n\\n\");\n    }\n    return 0;\n}" # termina el selector y cierra main
        self.main = self.main.replace("♥", self.menu)
        self.final_c += f"\n\n{self.functions}" # agrega las funciones al archivo final
        self.final_c += f"\n\n{self.main}" # agrega el main al archivo final

        Maker.write(self)

    def write(self):
        with open(f"{os.getcwd()}\\main.c", "w", encoding="utf-8") as file:
            file.write(self.final_c)
        print("File generated\nPress enter to exit")
        input("")

def main():
    maker = Maker()



main()