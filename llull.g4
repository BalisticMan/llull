grammar llull;

root: expr EOF;

expr: method*;

// RULES

value: identifier | number | getarray;

number: NUM;

identifier: ID;

relational:
	EQUAL
	| BETWEEN
	| LESS
	| GREATER
	| LESSEQUAL
	| GREATEREQUAL;

string: DOUBLEQUOTE text DOUBLEQUOTE;

write: WRITE LEFTPARENTHESIS writearguments RIGHTPARENTHESIS;

read: READ LEFTPARENTHESIS identifier RIGHTPARENTHESIS;

assignoperation: identifier ASSIGN operation;

operation:
	operation (MULT | DIV | MOD) operation
	| operation (PLUS | MINUS) operation
	| LEFTPARENTHESIS operation RIGHTPARENTHESIS
	| MINUS number
	| value;

relationaloperation: (operation | value) relational (
		operation
		| value
	);

ifconditional:
	IF LEFTPARENTHESIS relationaloperation RIGHTPARENTHESIS OPENBRACKET body CLOSEDBRACKET
		elseconditional?;

elseconditional: ELSE OPENBRACKET body CLOSEDBRACKET;

whileloop:
	WHILE LEFTPARENTHESIS relationaloperation RIGHTPARENTHESIS OPENBRACKET body CLOSEDBRACKET;

forloop:
	FOR LEFTPARENTHESIS assignoperation SEMICOLON relationaloperation SEMICOLON assignoperation
		RIGHTPARENTHESIS OPENBRACKET body CLOSEDBRACKET;

method:
	VOID identifier LEFTPARENTHESIS parameters RIGHTPARENTHESIS OPENBRACKET body CLOSEDBRACKET;

call: identifier LEFTPARENTHESIS arguments RIGHTPARENTHESIS;

parameters: (identifier (COMMA identifier)*)?;

arguments: ((value | operation) (COMMA (value | operation))*)?;

writearguments: (
		(value | operation | string) (
			COMMA (value | operation | string)
		)*
	)?;

body: (
		write
		| read
		| call
		| operation
		| assignoperation
		| ifconditional
		| whileloop
		| forloop
		| declarearray
		| setarray
		| getarray
	)*;

declarearray:
	ARRAY LEFTPARENTHESIS identifier COMMA (value | operation) RIGHTPARENTHESIS;

setarray:
	SET LEFTPARENTHESIS identifier COMMA (value | operation) COMMA (
		value
		| operation
	) RIGHTPARENTHESIS;

getarray:
	GET LEFTPARENTHESIS identifier COMMA (value | operation) RIGHTPARENTHESIS;

text: (
		NUM
		| WORD
		| ID
		| COLON
		| SEMICOLON
		| OPENBRACKET
		| CLOSEDBRACKET
		| LEFTPARENTHESIS
		| RIGHTPARENTHESIS
		| COMMA
		| PLUS
		| MINUS
		| DIV
		| MULT
		| MOD
		| EQUAL
		| ASSIGN
		| BETWEEN
		| LESS
		| GREATER
		| LESSEQUAL
		| GREATEREQUAL
	)*;

// CHARACTER TOKENS

NUM: [0-9]+;
COLON: ':';
SEMICOLON: ';';
OPENBRACKET: '{';
CLOSEDBRACKET: '}';
LEFTPARENTHESIS: '(';
RIGHTPARENTHESIS: ')';
COMMA: ',';
DOUBLEQUOTE: '"';

// KEY TOKENS

IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
READ: 'read';
WRITE: 'write';
ASSIGN: '=';
VOID: 'void';

// ARRAYS
ARRAY: 'array';
SET: 'set';
GET: 'get';

//ARIMETICAL TOKENS

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';

// RELATIONAL TOKENS

EQUAL: '==';
BETWEEN: '<>';
LESS: '<';
GREATER: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';

// COMMENT
COMMENT: ('#') ~'\n'* -> channel(HIDDEN);

// TEXT
ID: [a-zA-Z][a-zA-Z0-9\u0080-\u00FF]*;
WORD: ([0-9] | [A-Za-z\u0080-\uCAAF])+;
WS: [ \n\t]+ -> skip;
