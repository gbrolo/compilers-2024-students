import sys
from antlr4 import *
from gen.ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from gen.ConfRoomSchedulerParser import ConfRoomSchedulerParser

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()