#!/bin/bash
flex ./files/simple_language.l
yacc -dtv ./files/simple_language.y
g++ -c lex.yy.c 
g++ -c y.tab.c
g++ -o calc y.tab.o lex.yy.o