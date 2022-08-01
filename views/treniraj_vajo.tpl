% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>
<hr />
Trenutno izvajas vajo: <b>{{vaja_trenutna.ime}} </b><br />
Ponovitve: {{vaja_trenutna.ponovitve}}
<hr />

Naslednja vaja: {{vaja_naslednja.ime}}, {{vaja_naslednja.ponovitve}} krat

<hr />

% if id_naslednje_vaje + 1 == st_vaj:
    <a href="/trening/{{id_treninga}}/treniraj_zadnjo/">naprej</a>
%  else:
    <a href="/trening/{{id_treninga}}/treniraj/{{id_naslednje_vaje}}/">naprej</a>
% end