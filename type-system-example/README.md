# Type System Example

## Instrucciones

Este es un ejemplo de un sistema de tipos básico para una gramática simple.

* En el root de este lab deben crear un container interactivo en dónde van a correr los comandos de ANTLR:
  ```
  docker build --rm . -t tse-image && docker run --rm -ti -v "$(pwd)/program":/program tse-image
  ```
* En este caso creamos un volumen de Docker en `/program` que es en donde se encuentra la gramática de ANTLR. Asimismo, se encuentra un archivo `Driver.py` que sirve como un Main para importar las clases de Lexer y Parser generadas por ANTLR y poder analizar archivos para validarlos sintácticamente con la gramática que proporcionamos.
  * En este caso usamos un Visitor para visitar los nodos del árbol y aplicar análisis semántico.
  * También implementamos un Listener para este efecto.
* Dentro de esta carpeta también se encuentra el archivo `program_test.txt` el cual será el que vamos a parsear para analizar si es válido con nuestra gramática o no.
* Luego que corran el comando de Docker, deberán de generar los archivos de Lexer y Parser de ANTLR con el siguiente comando:
  ```
  antlr -Dlanguage=Python3 -visitor SimpleLang.g4
  antlr -Dlanguage=Python3 -listener SimpleLang.g4

  ```
* Luego, usan el Driver para analizar el archivo de prueba:
  ```
  python3 Driver.py program_test_pass.txt
  python3 DriverListener.py program_test_pass.txt
  ```
* Si el archivo se encuentra sintácticamente correcto, no verán un output en la consola. Por el contrario si hay un error sintáctico/léxico, ANTLR se los hará saber.
* De igual forma ahora manejamos errores a nivel de sistema de tipos también, ya son errores lógicos/semánticos.
* Y listo, con esto ya tienen un playground inicial para probar archivos con ANTLR.
* Para sus proyectos, se recomienda que extiendan este ambiente para sostener una arquitectura más robusta, este solo es un ejemplo básico.
