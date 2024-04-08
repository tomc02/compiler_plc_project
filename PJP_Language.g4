grammar PJP_Language;

start : statement+ EOF ;

statement
    : blockOfStatements
    | declaration
    | ifElse
    | while
    | for
    | doWhile
    | readStatement
    | writeStatement
    | baseExpr
    | emptyStatement
    ;

blockOfStatements
    : '{' statement (statement)* '}';
declaration
    : primitiveType IDENTIFIER ( COMMA IDENTIFIER)* SEMI
    | primitiveType IDENTIFIER '=' expr ( COMMA IDENTIFIER '=' expr)* SEMI;
ifElse
    : IF '(' expr ')' pos=statement (ELSE neg=statement)?;
while
    : WHILE '(' expr ')' statement;
for
    : FOR '(' declaration expr SEMI expr ')' statement
    | FOR '(' expr SEMI expr SEMI expr ')' statement;
doWhile
    : DO statement WHILE '(' expr ')' SEMI;
readStatement
    : READ IDENTIFIER ( COMMA IDENTIFIER)* SEMI;
writeStatement
    : WRITE expr ( COMMA expr)* SEMI;
baseExpr
    : expr SEMI;
emptyStatement
    : SEMI;


expr
    : IDENTIFIER                            # id
    | ('true'|'false')                      # bool          
    | '(' expr ')'                          # parenthesis
    | INT                                   # int           
    | FLOAT                                 # float         
    | STRING                                # string        
    | prefix=SUB expr                       # unaryMinus
    | prefix=NEG expr                       # negation      
    | expr op=(MUL|DIV|MOD) expr            # mulDivMod     
    | expr op=(ADD|SUB|CON) expr            # addSubCon     
    | expr op=(LES|GRE) expr                # relation      
    | expr op=(EQ|NEQ) expr                 # comparison    
    | expr AND expr                         # logicalAnd
    | expr OR expr                          # logicalOr
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    | <assoc=right> expr '=' expr           # assignment
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=STRING_KEYWORD
    | type=BOOL_KEYWORD
    ;


INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
STRING_KEYWORD : 'string';
BOOL_KEYWORD : 'bool';

CON : '.' ;
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
ADD : '+' ;
SUB : '-' ;
LES : '<' ;
GRE : '>' ;
NEG : '!' ;
EQ  : '==' ;
NEQ : '!=' ;
AND : '&&' ;
OR : '||' ;
SEMI : ';';
COMMA : ',';

READ : 'read' ;
WRITE : 'write' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
DO : 'do' ;
FOR : 'for' ;

INT : [0-9]+ ;
FLOAT : [0-9]+'.'[0-9]+ ;
STRING : '"' (~["\\\r\n] | EscapeSequence)* '"';
BOOL : ('true'|'false') ;

IDENTIFIER : [a-zA-Z] ([a-zA-Z0-9]*)? ;

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' ([0-3]? [0-7])? [0-7]
    ;

WS : [ \t\r\n]+ -> skip ;
COMMENT: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
