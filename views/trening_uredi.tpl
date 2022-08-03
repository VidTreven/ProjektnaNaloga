% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>

<ul>
  % for vaja_treninga in vaje_treninga:

    <form method="POST" action="dodaj/vecer/{{vaje_treninga.index(vaja_treninga)}}/prosim/" role="button" class="secondary outline">

        <select name="dodana_vaja" required>
          <option value="" disabled selected>Izberi vajo</option>
          % for vaja in vaje:
              <option value="{{vaja.ime}},{{vaja.opis}}">{{vaja.ime}}</option>
          % end
        </select>

        <select name="st_ponovitev" required>
          <option value="" disabled selected>Število ponovitev</option>
          % for stevilka in range(1,101):
              <option value={{stevilka}}>{{stevilka}}</option>
          % end
        </select>

        <input type="submit" value="Dodaj vajo">

    </form>

        <li>
            <big><big><b>{{vaja_treninga.ime}}</b>, {{vaja_treninga.ponovitve}} krat </big></big>
            <form method="POST" action="odstrani/{{vaje_treninga.index(vaja_treninga)}}/" role="button" class="secondary outline">
                <button>Odstrani</button>
            </form>
        </li>
  % end

    <form method="POST" action="dodaj/vecer/" role="button" class="secondary outline">

        <select name="dodana_vaja" required>
          <option value="" disabled selected>Izberi vajo</option>
          % for vaja in vaje:
              <option value="{{vaja.ime}},{{vaja.opis}}">{{vaja.ime}}</option>
          % end
        </select>

        <select name="st_ponovitev" required>
          <option value="" disabled selected>Število ponovitev</option>
          % for stevilka in range(1,101):
              <option value={{stevilka}}>{{stevilka}}</option>
          % end
        </select>

        <input type="submit" value="Dodaj vajo">
        
    </form>

<form method="POST" action="izbrisi/">
    <button>Izbriši trening</button>
</form>

