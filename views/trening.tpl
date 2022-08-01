

<h2>{{trening.ime}}</h2>
<ul>
  % for vaja in vaje_treninga:
  <li>{{vaja.ime,}}, {{vaja.ponovitve}} krat</li>
  % end
</ul>

% if vaje_treninga != []:
    <button><a href="treniraj/">Zacni s treningom!</a></button>
% end

% if vaje_treninga == []:
    <button><a href="uredi_novo/">Uredi trening.</a></button>
%  else:
    <button><a href="uredi/">Uredi trening.</a></button>
% end