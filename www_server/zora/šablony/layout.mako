<!DOCTYPE html>
<html lang="cz">
    <head>
        <meta charset="utf-8">
        <title>Зора на прузи<%block name="title" /></title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        <link href="${url_souboru('css/hlavni.css')}" rel="stylesheet">
        <link  href="${url_souboru('css/south-street/jquery-ui.css')}" rel="stylesheet">
        
        <script src="${url_souboru('js/libs/jquery.js')}" type="text/javascript"></script>
        <script src="${url_souboru('js/libs/jquery-ui.js')}" type="text/javascript"></script>
        <script src="${url_souboru('js/zora/zora.js')}" type="text/javascript"></script>
        
    </head>
    <body>
        <%block  name = "header" />
        ${ next.body() }
        
       
       <%block  name = "footer" >
        <footer class="ui-widget-header ui-corner-all">Изготовила Зора на прузи<small id="copyright">©Домоглед, Петр Болф 2012-2013</small></footer>
        </%block >
    </body>
</html>
