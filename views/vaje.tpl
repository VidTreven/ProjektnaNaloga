% rebase("osnova.tpl")

<h2>Vaje:</h2>

<ul>
    % for vaja in vaje:
        <li>
            <a href="{{vaje.index(vaja)}}/">{{vaja.ime}}</a>
        </li>
    % end
</ul>

<a href="uredi/" role="button">Uredi</a>
