/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    // vizuální kontrola na stránce da li je přítomno JQuery
    // ako ne, je tam zpráva
    $('#jquery_stav').remove();
    
    // aktivace hlavního menu jako jq-ui komponenta
    $('#hlavni_menu').tabs({
        activate: function(event, ui){
            $.each(event.target, function(key, value) {
                    $('#konzole').append('<br/>tabs ' + key + ': ' + value);
                }
            );
            window.alert("vybrano jest " + ui.newTab + ui.newTab.attr("href") + event.type);
            //window.alert(event.type);
            //window.alert(event.target.attr("id"));
        }
        
    });
    
    // nastavím ohlašování chyb
    $( document ).ajaxError(function(event, jqxhr, settings, exception) {
        msg = '<div class="chyba">Chyba ' + jqxhr.status + ': ' + jqxhr.statusText;
        msg = msg + '<br/>' + settings.url;
        //msg = msg + '<br/>Při události ' + event.type;
        //msg = msg + '<br/>status ' + jqxhr.status + ': ' + jqxhr.statusText;
        //msg = msg + '<br/>' + jqxhr.getAllResponseHeaders();
        //msg = msg + '<br/>' + jqxhr.statusCode();
        msg = msg + '<br/>Message: ' + exception;
        msg = msg + '</div>';
        $( '#konzole' ).append(msg);
        });
        
     $(document).ajaxSend(function(event, request, settings) {
        $('#konzole').append('<div class="info">Starting request at ' + settings.url + '</div>' );
     });
    
    // zavolám neo4j server a nastavím url
    
    $.get("http://localhost:7474/db/data/",
        {},
        function(data) {
            var url = data['cypher'];
            
            loadScripts(['js/zora/neo4j/cypher.js',
                'js/libs/js-url.js'
            
                ],
                function(){
                    $('#konzole').append('vše načteno');
                    cypher.url = url;
                    nactu_hlavni_stranku();
                }
            );
                
            $.each(data, function(key, value) {
                    $('#konzole').append('<br/>' + key + ': ' + value);
                }
            );
             
            $('footer').append(' ,neo4j ' + data['neo4j_version']);
            
            $('#konzole').append('<br/>načten cypher js pro url ' + url);
            
        }
    );
    
   /* $.get("http://localhost:7474/db/data/",
        {},
        function(data) {
            $.each(data, function(key, value) {
                    $('#konzole').append('<br/>' + key + ': ' + value);
                }
            );
             
            $('footer').append(' ,neo4j ' + data['neo4j_version']);
            nastavim_cypher(data['cypher']);
        }
     );*/
    
});

function zora(){
    
}    

function loadScripts(scripts, callback){

    var scripts = scripts || new Array();
    var callback = callback || function(){};

    for(var i = 0; i < scripts.length; i++){
    (function(i) {
        $.getScript(scripts[i], function() {

          if(i + 1 == scripts.length){
            callback();
          }
        });
      })(i);  
    }
};





function pridam_uzly(data) {
    $.each(data['data'], function(key, value) {
        //alert(key + ': ' + value);
        //$('#konzole').append('<br />přidávám uzel id ' + value[0] + ' ' + value[2] + ': ' + value[1]);
        $( "<div><p>" + value[2] + ': ' + value[1] + "</p></div>" ).appendTo( "body" );
        //graf.addNode(value[0]);
    });
    /*nacteno++;
    if(nacteno == 3) {
        cypher("MATCH n-[r:`MÁ SKUPINU`|`MÁ ÚČET`]->m RETURN ID(n) AS z_id, ID(m) AS do_id;", {}, pridam_hrany);

    }*/
    
/*
    var layouter = new Graph.Layout.Spring(g);
    layouter.layout();

    var renderer = new Graph.Renderer.Raphael('canvas', g, 400, 300);
    renderer.draw();*/
    
}

function nactu_hlavni_stranku(){
    $('#konzole').append('<br/>načtu hlavní stránku pro ' + window.location.href);
    
    $('#konzole').append('<br/> hledám ' + url(-1));
    $('#konzole').append('<br/>cypher url je nastaveno ' + cypher.url);
    
    //cypher("START n= node({id}) RETURN n;", {'id': 0}, pridam_uzly);
    //cypher("START n= node(0) RETURN n;", {}, pridam_uzly);
    cypher("MATCH n:`Účtová třída` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
    cypher("MATCH n:`Účtová skupina` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
    cypher("MATCH n:`Účet` RETURN ID(n) AS id, n.`jméno` AS `jméno`, n.`číslo` AS `číslo`;", {}, pridam_uzly);
}

