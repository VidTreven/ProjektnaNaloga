
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css">
    <title>Super sportnik</title>
  </head>
    <body>
        <h1>Pozdravljen, {{uporabnisko_ime}}!</h1>
        <big><big><big>Dobrodošel v tvojem osebnem trening centru!</big></big></big>
        <a href="/prijava/" role="button">Odjavi se</a>

        <hr />

        <h4>Tvoji treningi:</h4>
        <ul>
            % for trening in treningi:
                <li><a href="trening/{{treningi.index(trening)}}/">{{trening.ime}}</a></li>
            % end
        </ul>

        <a href="nov_trening/" role="button">Dodaj trening</a>

        <a href="vaje/" role="button">Vaje</a>
    </body>
</html>