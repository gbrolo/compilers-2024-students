
# Laboratorio 3

## Para correr el lab

Utilicen nuevamente el container del lab anterior o su propia implementación. No usen Java si no quieren, pueden usar Python.

* En el root de este lab deben crear un container interactivo en dónde van a correr los comandos de ANTLR:

  ```
  docker build --rm . -t lab2-image && docker run --rm -ti -v "$(pwd)/program":/program lab2-image
  ```
* Siga utilizando el mismo volumen de Docker en `/program` y coloque los archivos y la gramática de ANTLR. Asimismo, coloque el archivo `DriverConfroom.py` que sirve como un Main para importar las clases de Lexer y Parser generadas por ANTLR y poder analizar archivos para validarlos sintácticamente con la gramática que proporcionamos.

  * Aquí es donde después, conforme avance el curso, ustedes van a generar inclusive otras clases con ANTLR, ya sean Visitors o Listeners y van a aplicar un análisis semántico.
* Coloque también el archivo `program_test_confroom.txt` el cual será el que vamos a parsear para analizar si es válido con nuestra gramática o no.
* Luego que corran el comando de Docker, deberán de generar los archivos de Lexer y Parser de ANTLR con el siguiente comando:

  ```
  antlr -Dlanguage=Python3 ConfRoomScheduler.g4
  ```
* Luego, usan el Driver para analizar el archivo de prueba:

  ```
  python3 DriverConfroom.py program_test_confroom.txt
  ```
* Si el archivo se encuentra sintácticamente correcto, no verán un output en la consola. Por el contrario si hay un error sintáctico/léxico, ANTLR se los hará saber.
* Y listo, con esto ya tienen un playground inicial para probar archivos con ANTLR.
* Para sus proyectos, se recomienda que extiendan este ambiente para sostener una arquitectura más robusta, este solo es un ejemplo básico.
