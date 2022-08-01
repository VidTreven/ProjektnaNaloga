% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>


<b>POZOR!</b> Pred vsakim treningom se je dobro ogreti, saj s tem zmanjsamo stevilo poskodb.

% if st_vaj >= 2:
    <button><a href="0/">start</a></button>
% else:
    <button><a href="/trening/{{id_treninga}}/treniraj_zadnjo/">start</a></button>
% end