grammar Stochmize;

/*
 * Parser Rules
 */
 
program					: (MODEL VARIABLE_NAME '{' model '}')+ EOF ;
 
model 					: VARS '{' vars '}' SUBJTO '{' subjto '}' OBJECTIVES '{' objectives '}';

vars 					: (VARIABLE_NAME (fixed | random) ';')+ ; 

fixed					: '=' NUMBER;

random					: '~' (normal| unif);

normal 					: NORMAL "(" normal_params ")";

unif 					: UNIF "(" unif_params ")";

normal_params			: 'm' '=' NUMBER ',' 'v' '=' NUMBER;

unif_params				: 'a' '=' NUMBER ',' 'b' '=' NUMBER;

subjto 					: (VARIABLE_NAME SUBJTO_DEF NUMBER ';')+ ;

objectives				: (VARIABLE_NAME SUBJTO_DEF NUMBER ';')+ ;



/*
 * Lexer Rules
 */

WHITESPACE 			: (' ' | '\t') -> skip ;

NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;

MODEL				: 'model';

VARS				: 'vars';

SUBJTO				: 'subjto';

OBJECTIVES 			: 'objectives';

VARIABLE_NAME		: ('a'..'z' | 'A'..'Z'|'_')('a'..'z' | 'A'..'Z'|'0'..'9'|'_')*;

fragment DIGIT : [0-9];

NUMBER        		: DIGIT+ ([.,] DIGIT+)? ;

NORMAL 				: 'Normal';

UNIF 				: 'Unif';

OPERATOR			: ( '*' | '+' | '-' | '/' | '**')+ ;

SUBJTO_DEF			: ('=' | '<' | '>' | '<=' | '>=' )+;