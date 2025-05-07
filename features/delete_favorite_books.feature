Feature: Ta bort favoritbok

  Som användare
  Vill jag kunna ta bort en bok från mina favoriter
  Så att jag kan ångra mitt val

  Scenario: En användare favoritmarkerar och sedan avmarkerar en bok
    Given användaren är på startsidan
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas i katalogen
    When användaren favoritmarkerar boken "Min katt är min chef"
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas i Mina böcker
    When användaren klickar på navigeringsknappen "Katalog"
    And användaren favoritmarkerar boken "Min katt är min chef" igen
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas inte i Mina böcker

  Scenario Outline: En användare favoritmarkerar två böcker och avmarkerar en
    Given användaren är på startsidan
    Then boken "<titel1>" av "<författare1>" visas i katalogen
    And boken "<titel2>" av "<författare2>" visas i katalogen
    When användaren favoritmarkerar boken "<titel1>"
    And användaren favoritmarkerar boken "<titel2>"
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "<titel1>" av "<författare1>" visas i Mina böcker
    And boken "<titel2>" av "<författare2>" visas i Mina böcker
    When användaren klickar på navigeringsknappen "Katalog"
    And användaren favoritmarkerar boken "<titel2>" igen
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "<titel1>" av "<författare1>" visas i Mina böcker
    And boken "<titel2>" av "<författare2>" visas inte i Mina böcker

  Examples:
    | titel1                                     | författare1     | titel2                                                       | författare2     |
    | Min katt är min chef                       | Kattis Jamsson  | Jag trodde det var tisdag                                    | Kim Vilsen      |
    | Kaffekokaren som visste för mycket         | Saga Espresson  | 100 sätt att undvika måndagar                                | Göran Snooze    |
    | Gräv där du står – och hitta en pizzameny  | Maja Skruv      |  Att prata med växter – och vad de egentligen tycker om dig  | Flora Tistel    |