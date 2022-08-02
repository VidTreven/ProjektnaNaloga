% rebase("osnova.tpl")

<h2>{{trening.ime}}</h2>


  <form method="POST" action="dodaj/vecer/" role="button" class="secondary outline">
      <select name="dodana_vaja" required>
        <option value="" disabled selected>Izberi vajo</option>
        % for vaja in vaje:
            <option value="{{vaja.ime}},{{vaja.opis}}">{{vaja.ime}}</option>
        % end
      </select>
      <select name="st_ponovitev" required>
        <option value="" disabled selected>stevilo ponovitev</option>
        % for stevilka in range(1,101):
            <option value={{stevilka}}>{{stevilka}}</option>
        % end
      </select>
      <input type="submit" value="Dodaj vajo">
  </form>


<form method="POST" action="izbrisi/">
    <button>Izbrisi trening</button>
</form>


