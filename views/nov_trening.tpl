

<form>
  <label for="ime">Ime treninga:</label>
  <input type="text" id="ime" name="ime"><br><br>
</form>




<form>
    <ul>
    % for vaja in vaje:
        <li><input type="button" id={{vaja.ime}}><label for={{vaja.ime}}>{{vaja.ime}}</label></li>
    % end
    </ul>
</form>