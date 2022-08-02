% rebase("osnova.tpl")

<form method="POST" action="/trening/dodaj/" role="button" class="secondary outline" width: 50%>
  <input type="text" name="ime_treninga" placeholder="Trening '{{ime}}' ze obstaja">
  <button>Dodaj</button>
</form>