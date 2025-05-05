Feature: Navigeringsknappar

  Som en användare
  Vill jag kunna se och använda navigeringsknapparna i toppmenyn
  För att kunna växla mellan katalogen, lägga till en ny bok och se mina favoriter

  Background:
    Given användaren är på startsidan

  Scenario: Alla navigeringsknappar visas i toppmenyn
    Then ska navigeringsknappen "Katalog" vara synlig
    And ska navigeringsknappen "Lägg till bok" vara synlig
    And ska navigeringsknappen "Mina böcker" vara synlig

  Scenario Outline: Endast knappen för aktuell sektion är inaktiverad
  When användaren klickar på navigeringsknappen "<sektion>"
  Then ska navigeringsknappen "<sektion>" vara inaktiverad
  And ska navigeringsknapparna "<aktiva_knappar>" vara aktiverade

    Examples:
      | sektion         | aktiva_knappar            |
      | Katalog         | Lägg till bok, Mina böcker |
      | Lägg till bok   | Katalog, Mina böcker       |
      | Mina böcker     | Katalog, Lägg till bok     |
