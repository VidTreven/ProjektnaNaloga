% rebase("osnova.tpl")

<h2>Vaje:</h2>

<ul>
    % for vaja in vaje:
        <li>
            <a href="/vaje/{{vaje.index(vaja)}}/">{{vaja.ime}}</a>
            <form method="POST" action="{{vaje.index(vaja)}}/izbrisi/" role="button" class="secondary outline">
                <input type="submit" value="Izbrisi">
            </form>
        </li>
    % end
        <li> 
            <form method="POST" action="/vaje/dodaj/">
                <input type="text" name="ime" placeholder="Vaja '{{ime}}' ze obstaja">
                <input type="text" name="opis" placeholder="Opis vaje">
                <button>dodaj</button>
            </form>
        </li>
</ul>