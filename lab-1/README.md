# Laboratorio 1

## Changelog

**V2, Updates:**

* Hemos cambiado la gramática de este laboratorio un poco ya que presentaba ciertos problemas.
  * Lamento los inconvenientes, ahora no debe de dar problema al compilarlo.
* Para hacer mucho más fácil este ejercicio, y tomando en cuenta que la idea es solamente re-familiarizarse con conceptos de generadores de analizadores sintácticos, usando Lex y Yacc como herramientas, he agregado también un Dockerfile distinto. Los pasos para compilar y correr esto correctamente son ahora los siguientes:
  * En el root del lab, deben correr lo siguiente:
    ```
    docker build --rm . -t lab1-image && docker run --rm -ti -v "$(pwd)":/home lab1-image
    ```
  * Esto creará un container en modo interactivo. Al ingresar, deberán compilar ustedes la gramática corriendo:
    ```
    sh buildLanguage.sh
    ```
  * Luego, ya pueden correr el compilador corriendo `./calc` y con ello ejecutar directivas/programas del lenguaje.
  * No les pongo ejemplos de los programas que pueden correr porque esa es la idea del lab, que experimenten y ustedes determinen qué expresiones si son válidas y cuales no y ya con ello completar los incisos del lab.
  * Cualquier duda, estamos a la orden.
