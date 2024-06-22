grammar ConfRoomScheduler;

prog: stat+ ;

stat: reserve NEWLINE                # reserveStat
    | cancel NEWLINE                 # cancelStat
    | NEWLINE                        # blank
    ;

reserve: 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME ; 

cancel: 'CANCELAR' ID 'PARA' DATE 'DE' TIME 'A' TIME ; 

DATE: [0-9]{2}'/'[0-9]{2}'/'[0-9]{4} ; 
TIME: [0-9]{2}':'[0-9]{2} ; 
ID  : [a-zA-Z0-9]+ ; 
NEWLINE:'\r'? '\n' ; 
WS  : [ \t]+ -> skip ; 