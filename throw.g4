grammar throw;

prog: id1 del1 id2 del1 id3 del1 id4 ;

    id1 :
    'void'
    ;


    id2 :
    L
    ;

    id3 :
    'throws'
    ;


    id4 :
    L
    ;

    del1:
    ' ';

    L
    : [a-z]+
    |[A-Z]+
    ;

