<!DOCTYPE html>
<html lang="cz">
    <head>
        <meta charset="utf-8">
        <title>Зора на прузи</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        <link href="${request.static_url('zora:static/css/hlavni.css')}" rel="stylesheet">
        	
        <link href="${request.static_url('zora:static/css/south-street/jquery-ui.css')}" rel="stylesheet">
        
        <script src="${request.static_url('zora:static/js/libs/jquery.js')}" type="text/javascript"></script>
        <script src="${request.static_url('zora:static/js/libs/jquery-ui.js')}" type="text/javascript"></script>
        <script src="${request.static_url('zora:static/js/zora/zora.js')}" type="text/javascript"></script>
        <script src="${request.static_url('zora:static/ajax/cql_loader.js')}" type="text/javascript"></script>
        
    </head>
    <body>
        <header class="ui-widget-header ui-corner-all"><h1>Зора на прузи ADMIN ${project}</h1></header>
        <nav id="hlavni_menu">
            <ul>
                <li><a href="rozcestník">rozcestník</a></li>
                <li><a href="účetní_osnova">účetnictví</a></li>
                <li>Vodítka</li>
                <li>Krmivo</li>
                <li>Pelíšky</li>
                <li>Kontakt</li>
            </ul>
        </nav>
        
        <section>
            <div id="jquery_stav">Tato stránka vyžaduje javaskript a knihovnu jquery.</div>
            <div id="canvas"></div>
        </section>
        
        <section>
        <div id="konzole" class="ui-widget-header ui-corner-all">KONZOLE neo4j:</div>
        </section>
        
        <footer class="ui-widget-header ui-corner-all">Изготовила Зора на прузи<small id="copyright">©Домоглед, Петр Болф 2012-2013</small></footer>
    </body>
</html>
