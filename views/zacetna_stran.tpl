% rebase("osnova.tpl")

<h1>Dobrodosel v tvojem osebnem trening centru!</h1>

<h4>Tvoji treningi:</h4>
<ul>
% for trening in treningi:
    <li><a href="trening/{{treningi.index(trening)}}/">{{trening.ime}}</a></li>
% end
</ul>

<button><a href="nov_trening/">dodaj trening</a></button> 

<button><a href="vaje/">Vaje</a></button>

