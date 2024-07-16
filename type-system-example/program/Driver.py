import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from type_check_visitor import TypeCheckVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.prog()

    visitor = TypeCheckVisitor()
    try:
        visitor.visit(tree)
        print("Type checking passed")
    except TypeError as e:
        print(f"Type checking error: {e}")

if __name__ == '__main__':
    main(sys.argv)
