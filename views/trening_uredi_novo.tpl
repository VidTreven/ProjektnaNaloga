% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>

<form method="POST" action="izbrisi/">
    <button>Izbrisi trening</button>
</form>


<h3>Dodaj vajo:</h3>
<ul>
  % for vaja in vaje:
    <li> 
        <form method="POST" action="dodaj/{{vaje.index(vaja)}}/">
            {{vaja.ime}}, <input type="text" name="ponovitve" placeholder="st. ponovitev">
            <button>dodaj</button>
        </form>
    </li>
  % end
</ul>