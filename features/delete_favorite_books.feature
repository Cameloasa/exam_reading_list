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
