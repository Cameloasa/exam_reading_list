Feature: Favoritböcker

  Som användare
  Vill jag kunna se en lista med böcker i katalogen
  Så att jag kan välja mina favorit böcker

  Scenario Outline: Användaren lägger till en bok som favorit och ser den i "Mina böcker"
    Given användaren är på startsidan
    Then boken "<titel>" av "<författare>" visas i katalogen
    When användaren favoritmarkerar boken "<titel>"
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "<titel>" av "<författare>" visas i Mina böcker

  Examples:
    | titel                                                       | författare        |
    | Hur man tappar bort sin TV-fjärr 10 gånger om dagen         | Bertil Flimmer    |
    | Kaffekokaren som visste för mycket                          | Saga Espresson    |
    | Min katt är min chef                                        | Kattis Jamsson    |
    | 100 sätt att undvika måndagar                               | Göran Snooze      |
    | Gräv där du står – och hitta en pizzameny                   | Maja Skruv        |
    | Jag trodde det var tisdag                                   | Kim Vilsen        |
    | Att prata med växter – och vad de egentligen tycker om dig  | Flora Tistel      |
