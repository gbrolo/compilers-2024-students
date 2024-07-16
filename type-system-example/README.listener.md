# Implementación de un Sistema de Tipos utilizando ANTLR y Python

## Propagación de los tipos

Al usar listeners, debemos asegurarnos de que los tipos de las subexpresiones se establezcan correctamente y luego se utilicen en las expresiones padre. Si los tipos no se propagan adecuadamente, esto resulta en tipos `None` usados en las expresiones padre, causando errores de tipo.

## Arquitectura

### Propagación de Tipos

* Los tipos deben almacenarse en los nodos del contexto del árbol de análisis y propagarse hacia arriba en el árbol. Esto significa que cuando se evalúa una expresión, su tipo debe establecerse en su contexto, para que los contextos padre puedan acceder a él.

### Almacenamiento y Recuperación de Tipos

* Introdujimos un diccionario `self.types` en el `TypeCheckListener` para almacenar los tipos asociados a cada contexto.
* Al ingresar a un contexto, a veces necesitamos pasar porque la determinación real del tipo se realiza al salir del contexto.
* Al salir de un contexto, establecemos el tipo para ese contexto en el diccionario `self.types`, basado en los tipos de sus hijos.

### Implementación

#### Inicialización

* Inicializamos un diccionario `self.types` para almacenar los tipos de cada contexto y una lista `self.errors` para recopilar cualquier error de tipo.

```
class TypeCheckListener(SimpleLangListener):
    def __init__(self):
        self.errors = []
        self.types = {}

```


#### Entrar en Expresiones

* Al entrar en operaciones binarias (`enterMulDiv`, `enterAddSub`), no realizamos ninguna verificación ni establecemos ningún tipo inmediatamente. Las verificaciones y el establecimiento de tipos se realizan en los métodos `exit` después de que ambos operandos han sido visitados.

```
def enterMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    pass

def enterAddSub(self, ctx: SimpleLangParser.AddSubContext):
    pass

```


#### Salir de Expresiones

* Al salir de operaciones binarias (`exitMulDiv`, `exitAddSub`), recuperamos los tipos de los operandos izquierdo y derecho del diccionario `self.types`.
* Luego verificamos si la operación es válida para estos tipos y establecemos el tipo para el contexto actual.

```
def exitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
        self.errors.append(f"Unsupported operand types for * or /: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

def exitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.types[ctx.expr(0)]
    right_type = self.types[ctx.expr(1)]
    if not self.is_valid_arithmetic_operation(left_type, right_type):
        self.errors.append(f"Unsupported operand types for + or -: {left_type} and {right_type}")
    self.types[ctx] = FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

```


#### Manejo de Literales y Paréntesis

* Para literales (`enterInt`, `enterFloat`, `enterString`, `enterBool`), establecemos el tipo directamente en el diccionario `self.types`.
* Para paréntesis, simplemente pasamos en el método `enterParens` y luego propagamos el tipo de la expresión interna en el método `exitParens`.

```
def enterInt(self, ctx: SimpleLangParser.IntContext):
    self.types[ctx] = IntType()

def enterFloat(self, ctx: SimpleLangParser.FloatContext):
    self.types[ctx] = FloatType()

def enterString(self, ctx: SimpleLangParser.StringContext):
    self.types[ctx] = StringType()

def enterBool(self, ctx: SimpleLangParser.BoolContext):
    self.types[ctx] = BoolType()

def enterParens(self, ctx: SimpleLangParser.ParensContext):
    pass

def exitParens(self, ctx: SimpleLangParser.ParensContext):
    self.types[ctx] = self.types[ctx.expr()]

```


#### Funciones Utilitarias

* `get_type`: Una función auxiliar para obtener el tipo de un contexto.
* `is_valid_arithmetic_operation`: Una función auxiliar para verificar si una operación aritmética es válida para los tipos de operandos dados.

```
def get_type(self, ctx):
    if hasattr(ctx, 'type'):
        return ctx.type
    for child in ctx.getChildren():
        if hasattr(child, 'type'):
            return child.type
    return None

def is_valid_arithmetic_operation(self, left_type, right_type):
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return True
    return False

```
