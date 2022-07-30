

<h2>{{trening.ime}}</h2>
<ul>
  % for vaja in vaje:
  <li>{{vaja.ime,}}, {{vaja.ponovitve}}</li>
  % end
</ul>

<button><a href="">Zacni s treningom!</a></button>
<button><a href="">Dodelaj trening.</a></button>