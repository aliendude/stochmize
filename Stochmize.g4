grammar Stochmize;

/*
 * Parser Rules
 */
 
program					: (MODEL ID '{' model '}')+ EOF ;
 
model 					: VARS_DEF '{' vars_def '}' SUBJTO '{' subjto '}' OBJECTIVES '{' objectives '}';

vars_def 				: (ID ( fixed_range_random ) ';')+ ;

fixed_range_random		: (fixed | rang | random);

fixed					: '=' NUMBER;

random					: '~' (normal| unif );

rang					: ':' '(' limit ',' limit ')';

limit					: (MINUS)? NUMBER ;

normal 					: NORMAL '(' normal_params ')';

unif 					: UNIF '(' unif_params ')';

normal_params			: 'm' '=' NUMBER ',' 'v' '=' NUMBER;

unif_params				: 'a' '=' NUMBER ',' 'b' '=' NUMBER;

subjto 					: (expr SUBJTO_DEF NUMBER ';')+ ;

objectives				: (min_max ID '=' expr';')+ ;

min_max					: (MAX | MIN);

expr					: expr_content ( operators expr_content )*;

expr_content			: (ID | NUMBER) | ('(' expr ')') | (MINUS expr_content) ;

operators				: (PLUS | MINUS | PROD | DIV| POW);


/*
 * Lexer Rules
 */

WHITESPACE 			: (' ' | '\t') -> skip ;

NEWLINE             : ('\r'? '\n' | '\r')+ -> skip;

MODEL				: 'model';

VARS_DEF			: 'vars';

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

NUMBER        		: DIGIT+ ([.] DIGIT+)? ;

SUBJTO_DEF			: ('=' | '<' | '>' | '<=' | '>=' )+;