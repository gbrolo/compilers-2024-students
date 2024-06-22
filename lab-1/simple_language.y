%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%token NUMBER
%token ID

%%

program: statement_list
        ;

statement_list: statement
              | statement_list statement
              ;

statement: assignment
         | expression
         ;

assignment: ID '=' expression
          { printf("Assign %s = %d\n", $1, $3); }
          ;

expression: NUMBER
          | ID
          | expression '+' expression
          | expression '-' expression
          | expression '*' expression
          | expression '/' expression
          ;

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    printf("Error: %s\n", s);
    return 0;
}
