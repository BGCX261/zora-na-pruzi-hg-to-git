<%inherit file="../layout.mako" />
##<%page args="model, request" />



<h1>SEZNAM DATABÁZÍ</h1>
<ol>
% for databáze in model:
        <li>${databáze}</li>
% endfor
</ol>
${url('vytvoř_databázi',  jméno_databáze = 'brum')}
${url_souboru('css/styl.css')}

