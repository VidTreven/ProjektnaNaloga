% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>


<ul>
  % for vaja_treninga in vaje_treninga:
    <form method="POST" action="dodaj/vecer/{{vaje_treninga.index(vaja_treninga)}}/prosim/" role="button" class="secondary outline" width="40" height="20">
      <select name="dodana_vaja" required>
        <option value="" disabled selected>Izberi vajo</option>
        % for vaja in vaje:
            <option value="{{vaja.ime}},{{vaja.opis}}">{{vaja.ime}}</option>
        % end
      </select>
      <select name="st_ponovitev" required>
        <option value="" disabled selected>stevilo ponovitev</option>
        % for stevilka in range(0,101):
            <option value={{stevilka}}>{{stevilka}}</option>
        % end
      </select>
      <input type="submit" value="Dodaj vajo">
    </form>
        <li>
            <b>{{vaja_treninga.ime}}</b>, {{vaja_treninga.ponovitve}} krat
            <form method="POST" action="odstrani/{{vaje_treninga.index(vaja_treninga)}}/" role="button">
                Odstrani
            </form>
        </li>
     % end

  <form method="POST" action="dodaj/vecer/" role="button" class="secondary outline">
      <select name="dodana_vaja">
        <option value="" disabled selected>Izberi vajo</option>
        % for vaja in vaje:
            <option value="{{vaja.ime}},{{vaja.opis}}">{{vaja.ime}}</option>
        % end
      </select>
      <select name="st_ponovitev">
        <option value="" disabled selected>stevilo ponovitev</option>
        % for stevilka in range(0,101):
            <option value={{stevilka}}>{{stevilka}}</option>
        % end
      </select>
      <input type="submit" value="Dodaj vajo">
  </form>



