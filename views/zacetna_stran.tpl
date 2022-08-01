% rebase("osnova.tpl")

<h1>Dobrodosel v tvojem osebnem trening centru!</h1>

<h4>Tvoji treningi:</h4>
<ul>
% for trening in treningi:
    <li><a href="trening/{{treningi.index(trening)}}/">{{trening.ime}}</a></li>
% end
</ul>

 

<a href="nov_trening/" role="button">Dodaj trening</a>

<a href="vaje/" role="button">Vaje</a>



