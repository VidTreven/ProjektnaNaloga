% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>
<ul>
  % for vaja in vaje_treninga:
  <li>{{vaja.ime,}}, {{vaja.ponovitve}} krat</li>
  % end
</ul>

% if vaje_treninga != []:
    <a href="treniraj/" role="button">Zacni s treningom!</a>
% end

% if vaje_treninga == []:
    <a href="uredi_novo/" role="button">Uredi trening</a>
%  else:
    <a href="uredi/" role="button">Uredi trening</a>
% end


