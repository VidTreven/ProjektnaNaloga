% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>


<b>POZOR!</b> Pred vsakim treningom se je dobro ogreti, saj s tem zmanjsamo stevilo poskodb.

% if st_vaj >= 2:
    <a href="0/" role="button">Start</a>
% else:
    <a href="/trening/{{id_treninga}}/treniraj_zadnjo/" role="button">Start</a>
% end


