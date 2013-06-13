/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function cypher(kod, parametry, funkce) {
    //alert('CYPHER ' + gdb['cypher']  + kod);
    $('#konzole').append('<br />volám cypher ' + kod);
    //$('#konzole').append('<br />do funkce ' + funkce.constructor);

    dotaz = {
        "query" : kod,
        "params" : parametry
    };

/*
    $.ajax({
        url: cypher.url,
        type: "POST",
        data: $.param(dotaz),
        accepts: 'application/json',
    // toto dělá chybu
        //contentType: 'application/json',
        success: funkce
    }
    );*/

    $.post(
        cypher.url,
        $.param(dotaz),
        funkce
    );
}
