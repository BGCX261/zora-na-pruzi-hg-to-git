{% load staticfiles %}
<!DOCTYPE html>
<html lang="cz">
    <head>
        <meta charset="utf-8">
        <title><% block name="titulek" >Зора на прузи</%block></title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        <link href="{% static "css/hlavni.css" %}" rel="stylesheet">
        <link href="{% static "css/south-street/jquery-ui.css" %}" rel="stylesheet">
        
        <script src="{% static "js/libs/jquery.js" %}" type="text/javascript"></script>
        <script src="{% static "js/libs/jquery-ui.js" %}" type="text/javascript"></script>
        <script src="{% static "js/zora/zora.js" %}" type="text/javascript"></script>
        
    </head>
    <body>
        {% block body %}<header><h1>${titulek()}</h1></header>{% endblock %}
        
        
        {% block footer %}
        <footer class="ui-widget-header ui-corner-all">Изготовила Зора на прузи<small id="copyright">©Домоглед, Петр Болф 2012-2013</small></footer>
        {% endblock %}
    </body>
</html>
