l = "{"
r = "}"

class Maker:
    def __init__(self):

        self.lenapartados = 0
        self.apartados = {}

        self.main = f"int main() {l}\n    int s = 0;\n    int a;\n    " # inicializa main, s, a y ejecuta el clrscr
        self.main += f"while(1 > 0) {l}\n        clrscr();        \nprintf(\"♥\");\n        "  #agrega un espacio para luego poner el menú e inicia el loop
        self.main += f"printf(\"\\nSeleccione un ejercicio: \");\n        scanf(\"%d\", &s);\n        switch (s) {l}\n" # obtiene el num de ejercicio e inicia el switch

        self.menu = ""
        self.functions = ""

        self.title = ""
        self.final_c = "#include <stdio.h>\n#include <stdlib.h>\n\nvoid clrscr() {\n    system(\"@cls||clear\");\n}\n" # agrega librerías

    def get_data(self):
        """Obtiene los datos para generar la estructura"""
        title = input("Introduzca nombre del práctico: ")
        self.menu += title + "\\n\\n"
        self.lenapartados = int(input("Introduzca número de apartados: "))
        for a in range(self.lenapartados):
            apartado = input(f"Introduzca nombre de apartado {a+1}: ")
            num = int(input(f"Introduzca cantidad de ejercicios del apartado {apartado}: "))
            self.apartados[apartado] = num

    def build(self):
        """Genera la estructura"""
        exercice_num = 1;
        for title, exercices in self.apartados.items():
            self.menu += f"\\n--------------{title}--------------\\n\\n" # agrega un subtítulo al menú
            for i in range(exercices):
                self.functions += f"int Ejercicio{exercice_num}() {l}\n    //consigna de {title} .{i+1}\n{r}\n" # genera las funciones y les agrega la consigna
                self.menu += f"{exercice_num}. Ejercicio {i+1}\\n" # agrega los ejercicios al submenú
                self.main += f"            case {exercice_num}:\n                Ejercicio{exercice_num}();\n                break;\n" # agrega casos al switch
                exercice_num += 1
        self.main += f"            default:\n                printf(\"ejercicio fuera de rango\");\n                break;\n" # detector de valores incorrectos
        self.main += f"        {r}\n" # cierra el switch
        self.main += "        printf(\"\\n----------\\n\\n\");\n        " #separador
        self.main += "printf(\"Introduzca 1 para continuar o 0 para cerrar: \");\n        scanf(\"%d\", &a);\n        " # inicia el selector de cierre
        self.main += "if (a == 0) {\n            break;\n        }\n        printf(\"\\n----------\\n\\n\");\n    }\n    return 0;\n}" # termina el selector y cierra main
        self.main = self.main.replace("♥", self.menu)

    def write(self):
        self.final_c += f"\n\n{self.functions}"
        self.final_c += f"\n\n{self.main}"
        with open("main.c", "w") as file:
            file.write(self.final_c)

def main():
    maker = Maker()
    maker.get_data()
    maker.build()
    maker.write()


main()