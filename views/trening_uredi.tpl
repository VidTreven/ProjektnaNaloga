% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>


<ul>
  % for vaja in vaje_treninga:
    <li>
        <b>{{vaja.ime}}</b>, {{vaja.ponovitve}} krat
        <form method="POST" action="odstrani/{{vaje_treninga.index(vaja)}}/" role="button">
            Odstrani
        </form>
    </li>
  % end
</ul>

<h3>Dodaj vajo:</h3>
<ul>
  % for vaja in vaje:
    <li> 
            {{vaja.ime}}
            <a href="dodaj/{{vaje.index(vaja)}}/" role="button">Dodaj</a>
    </li>
  % end
</ul>

<form method="POST" action="izbrisi/">
    <button>Izbrisi trening</button>
</form>