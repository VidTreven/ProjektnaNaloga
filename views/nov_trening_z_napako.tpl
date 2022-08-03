% rebase("osnova.tpl")

<form method="POST" action="/trening/dodaj/" class="secondary outline">
  <input type="text" name="ime_treninga" placeholder="Trening '{{ime}}' ze obstaja">
  <button>Dodaj</button>
</form>