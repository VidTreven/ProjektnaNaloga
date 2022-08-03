% rebase("osnova.tpl")

<h2>{{trening.ime.upper()}}</h2>


<b>POZOR!</b> 
<br />
Pred vsakim treningom se je potrebno dobro ogreti, saj se s tem zavarujemo pred poškodbami.

<hr />
% if st_vaj >= 2:
    <a href="0/" role="button">Start</a>
% else:
    <a href="/trening/{{id_treninga}}/treniraj_zadnjo/" role="button">Start</a>
% end


