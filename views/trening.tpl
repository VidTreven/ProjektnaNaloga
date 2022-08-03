% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>

<hr />

<ul>
  % for vaja in vaje_treninga:
    <li><b>{{vaja.ime}}</b>, {{vaja.ponovitve}} krat</li>
  % end
</ul>

<hr />

% if vaje_treninga != []:
    <a href="treniraj/" role="button">Začni s treningom</a>
% end

% if vaje_treninga == []:
    <a href="uredi_novo/" role="button">Uredi trening</a>
%  else:
    <a href="uredi/" role="button">Uredi trening</a>
% end


