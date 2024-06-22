grammar TerraformSubset;

terraform: (provider | resource | variable | output)* EOF;

provider: 'provider' IDENTIFIER '{' providerBody '}';
providerBody: (keyValuePair)*;

resource: 'resource' IDENTIFIER IDENTIFIER '{' resourceBody '}';
resourceBody: (keyValuePair)*;

variable: 'variable' IDENTIFIER '{' variableBody '}';
variableBody: (keyValuePair)*;

output: 'output' IDENTIFIER '{' outputBody '}';
outputBody: (keyValuePair)*;

keyValuePair: IDENTIFIER '=' STRING;

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' ('\\' . | ~["\\])* '"';

WS: [ \t\r\n]+ -> skip;
