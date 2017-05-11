grammar Stochmize;

/*
 * Parser Rules
 */
 
program					: (MODEL ID '{' model '}')+ EOF ;
 
model 					: VARS '{' vars '}' SUBJTO '{' subjto '}' OBJECTIVES '{' objectives '}';

vars 					: (ID (fixed | random) ';')+ ; 

fixed					: '=' NUMBER;

random					: '~' (normal| unif);

normal 					: NORMAL '(' normal_params ')';

unif 					: UNIF '(' unif_params ')';

normal_params			: 'm' '=' NUMBER ',' 'v' '=' NUMBER;

unif_params				: 'a' '=' NUMBER ',' 'b' '=' NUMBER;

subjto 					: (ID SUBJTO_DEF NUMBER ';')+ ;

objectives				: ((MAX | MIN) ID '=' ((PLUS | MINUS)? (NUMBER OPERATOR)? ID)(OPERATOR (ID | NUMBER))+ ';')+ ;


/*
 * Lexer Rules
 */

WHITESPACE 			: (' ' | '\t') -> skip ;

NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;

MODEL				: 'model';

VARS				: 'vars';

SUBJTO				: 'subjto';

OBJECTIVES 			: 'objectives';

NORMAL 				: 'Normal';

UNIF 				: 'Unif';

MAX					: 'max';

MIN					: 'min';

PLUS				: '+';

MINUS				: '-';

POW					: '**';

PROD				: '*';

DIV					: '/';


ID					: ('a'..'z' | 'A'..'Z'|'_')('a'..'z' | 'A'..'Z'|'0'..'9'|'_')*;

fragment DIGIT 		: [0-9];

NUMBER        		: DIGIT+ ([.,] DIGIT+)? ;


OPERATOR			: ( PLUS | MINUS | PROD | DIV | POW) ;

SUBJTO_DEF			: ('=' | '<' | '>' | '<=' | '>=' )+;