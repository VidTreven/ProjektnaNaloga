<h2>{{trening.ime}}</h2>



<ul>
  % for vaja in vaje_treninga:
    <li>
        <form method="POST" action="{{vaje_treninga.index(vaja)}}/">
            {{ime_nase_vaje}}, <input type="text" name="ponovitve" placeholder="st. ponovitev">
            <button>dodaj</button>
        </form>
        {{vaja.ime}}, {{vaja.ponovitve}} krat
    </li>
  % end
    <li>
        <form method="POST" action="{{vaje_treninga.index(vaja) + 1}}/">
            {{ime_nase_vaje}}, <input type="text" name="ponovitve" placeholder="st. ponovitev">
            <button>dodaj</button>
        </form>
    </li>
</ul>

