/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */




davaj_html = function(element) {
    //window.alert('Ja sem tu uhu ju i ta 3e toto ' + this);
    element.append('<br />... načítám data');
    
    data = $.getJSON('účetní_osnova.json',
                function(data, textStatus, jqxhr){
                    window.alert('JSON data ' + data);
                    //element.html(data);
                    element.append('<br />data su hen');
                    
                    jQuery.each(data['data'], function(klíč, řádek){
                            
                            id = řádek[0];
                            jméno = řádek[1];
                            číslo = řádek[2];
                            //console.log(číslo);
                            element.append('<h1 id="uzel_' + id + '">' + číslo + ': ' + jméno + '</h1>');
                            var div = $('<div>', {
                                /*href: url,
                                text: title,
                                click: function(e) {
                                    alert(this.href);
                                },
                                css: {
                                    color: 'red'
                                }*/
                            });
                            element.append(div);
                            
                            jQuery.each(řádek[3], function(klíč, řádek){
                                id = řádek[0];
                                jméno = řádek[1];
                                číslo = řádek[2];
                                div.append('<h2 id="uzel_' + id + '">' + číslo + ': ' + jméno + '</h2>');
                                var ul = $('<ul>', {});
                                div.append(ul);
                                
                                jQuery.each(řádek[3], function(klíč, řádek){
                                    id = řádek[0];
                                    jméno = řádek[1];
                                    číslo = řádek[2];
                                    ul.append('<li id="uzel_' + id + '">' + číslo + ': ' + jméno + '</li>');
                                    
                                }
                                );
                            }
                            );
                            
                          
                        });
                    
                    console.log('acordijon');
                    $(element).accordion({
                        heightStyle: "content"
                    }
                    );
                }
                
            );
};

