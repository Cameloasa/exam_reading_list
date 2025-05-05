Feature: Sidans statiska innehåll

  Som en användare
  Vill jag se att sidan har korrekt titel och välkomsttext
  Så att jag vet att jag har kommit till rätt plats

  Scenario: Startsidans titel och rubrik visas korrekt
  Given användaren är på startsidan
  Then sidans titel ska vara "Läslistan"
  And texten "Läslistan" visas i rubriken
  And texten "Välkommen!" visas i underrubriken
  And texten "Sidan för dig som gillar att läsa. Välj dina favoriter." ska visas i brödtexten


  Scenario Outline: Välkomsttexten visas i varje sektion
    Given användaren är på startsidan
    When användaren går till sektionen "<sektion>"
    Then texten "Välkommen!" visas i underrubriken
    And texten "Sidan för dig som gillar att läsa. Välj dina favoriter." ska visas i brödtexten

    Examples:
      | sektion        |
      | Katalog        |
      | Lägg till bok  |
      | Mina böcker    |

