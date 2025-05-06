Feature: Visa bokkatalog lista

  För att kunna välja bland tillgängliga böcker
  Som en användare
  Vill jag kunna se en lista med böcker i katalogen

  Background:
    Given användaren är på startsidan

  Scenario: Användaren ser en lista med böcker i katalogen
    Then användaren ska kunna se titlar och författare för varje bok
    And användaren ska kunna klicka på varje bok för att lägga till den i "Mina böcker"