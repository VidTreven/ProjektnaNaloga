

<h2>{{trening.ime}}</h2>
<ul>
  % for vaja in vaje_treninga:
  <li>{{vaja.ime,}}, {{vaja.ponovitve}} krat</li>
  % end
</ul>

<button><a href="">Zacni s treningom!</a></button>
<button><a href="uredi/">Uredi trening.</a></button>