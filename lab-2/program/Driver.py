import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

if __name__ == '__main__':
    main(sys.argv)
