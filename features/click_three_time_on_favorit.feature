Feature: Växlande favoritstatus vid upprepade klick

  Som användare
  Vill jag att favoritmarkeringen ska växla varje gång jag klickar på hjärtat,
  Så att det alltid stämmer med min avsikt.

  Scenario: En användare klickar flera gånger på favoritknappen
    Given användaren är på startsidan
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas i katalogen
    When användaren favoritmarkerar boken "Min katt är min chef"
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas i Mina böcker
    When användaren klickar på navigeringsknappen "Katalog"
    And användaren favoritmarkerar boken "Min katt är min chef" igen
    And användaren favoritmarkerar boken "Min katt är min chef" igen
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "Min katt är min chef" av "Kattis Jamsson" visas i Mina böcker