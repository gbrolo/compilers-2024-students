%{
#include "y.tab.h"
%}

%%

[a-zA-Z][a-zA-Z0-9]*    { yylval.str = strdup(yytext); return ID; }
[0-9]+                   { yylval.num = atoi(yytext); return NUMBER; }
"+"                      { return '+'; }
"-"                      { return '-'; }
"*"                      { return '*'; }
"/"                      { return '/'; }
"="                      { return '='; }
"\n"                     { return '\n'; }
[ \t]                    ;  // skip whitespace

.                        { return yytext[0]; }

%%

int yywrap() {
    return 1;
}
