<%page args="model, request"/>
<h1>SEZNAM DATABÁZÍ</h1>
<ol>
% for databáze in model:
        <li>${databáze}</li>
% endfor
</ol>
{% url 'home'  %}

## výchozí namespace
<p>${local.filename}</p>

<%text filter="h">
    heres some fake mako ${syntax}
    <%def name="x()">${x}</%def>
</%text>

##užití caller.body v def
<%def name="buildtable()">
    <table>
        <tr><td>
            ${caller.body()}
        </td></tr>
    </table>
</%def>

<%self:buildtable>
    I am the table body.
</%self:buildtable>

## užití bloku
% for i in range(1, 4):
    <%block>i is ${i}</%block>
% endfor
