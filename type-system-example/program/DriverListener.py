import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from type_check_listener import TypeCheckListener
from antlr4.tree.Tree import ParseTreeWalker

def main(argv):
  input_stream = FileStream(argv[1])
  lexer = SimpleLangLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = SimpleLangParser(stream)
  tree = parser.prog()

  walker = ParseTreeWalker()
  listener = TypeCheckListener()
  walker.walk(listener, tree)

  if listener.errors:
    for error in listener.errors:
      print(f"Type checking error: {error}")
  else:
    print("Type checking passed")

if __name__ == '__main__':
  main(sys.argv)
