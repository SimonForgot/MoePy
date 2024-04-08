grammar Moe;

INT: [0-9]+;
ID: [a-zA-Z_] [a-zA-Z_0-9]*;
NL: ('\r')? '\n';
WS: [ \t]+ -> skip;

file: block (NL+ block)* EOF;
block: expr # ExpBlk | fun_def # FDBlk;
expr:
	ID '(' expr (',' expr)* ')'	# APP
	| expr '*' expr				# MUL
	| expr '+' expr				# ADD
	| INT						# INT
	| ID						# VAR;
fun_def: 'fun' ID '(' ID (',' ID)* '):' NL '{' NL expr NL '}';