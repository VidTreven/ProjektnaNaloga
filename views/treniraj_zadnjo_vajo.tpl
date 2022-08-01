% rebase("osnova.tpl")

<h2>{{trening.ime.upper()}}</h2>
<hr />
Trenutno izvajas vajo: <b>{{vaja_trenutna.ime.upper()}} </b><br />
Ponovitve: {{vaja_trenutna.ponovitve}}
<hr />

<b> TO JE ZADNJA VAJA! </b>

<hr />


<a href="/trening/{{id_treninga}}/" role="button">koncaj s treningom</a>
