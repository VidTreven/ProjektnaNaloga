% rebase("osnova.tpl")

<h2>{{trening.ime.upper()}}</h2>
<hr />
Trenutno izvajas vajo: <b>{{vaja_trenutna.ime.upper()}} </b><br />
Ponovitve: {{vaja_trenutna.ponovitve}}
<hr />

Naslednja vaja: {{vaja_naslednja.ime}}, {{vaja_naslednja.ponovitve}} krat

<hr />

% if id_naslednje_vaje + 1 == st_vaj:
    <a href="/trening/{{id_treninga}}/treniraj_zadnjo/" role="button">naprej</a>
%  else:
    <a href="/trening/{{id_treninga}}/treniraj/{{id_naslednje_vaje}}/" role="button">naprej</a>
% end


    
