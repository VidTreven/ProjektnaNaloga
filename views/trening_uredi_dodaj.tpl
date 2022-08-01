% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>



<ul>
  % for vaja in vaje_treninga:

        <form method="POST" action="{{vaje_treninga.index(vaja)}}/" role="button" class="secondary outline">
            {{ime_nase_vaje}} <input type="text" name="ponovitve" placeholder="st. ponovitev">
            <button>dodaj</button>
        </form>
    <li>
        <b>{{vaja.ime}}</b>, {{vaja.ponovitve}} krat
    </li>
  % end

        <form method="POST" action="{{vaje_treninga.index(vaja) + 1}}/" role="button" class="secondary outline">
            {{ime_nase_vaje}}, <input type="text" name="ponovitve" placeholder="st. ponovitev">
            <button>dodaj</button>
        </form>
</ul>

