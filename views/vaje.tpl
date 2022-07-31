<h2>Vaje:</h2>
<ul>
% for vaja in vaje:
    <li>
        <a href="{{vaje.index(vaja)}}/">{{vaja.ime}}</a>
    </li>
% end
</ul>

<button>
<a href="uredi/">Uredi</a>
</button>
