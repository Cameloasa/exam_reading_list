Feature: Sidans statiska innehåll

  Som en användare
  Vill jag se att sidan visar titel och välkomsttext
  Så att jag vet att jag har kommit till rätt plats

  Scenario: Sidans titel och välkomsttexter visas
    Given användaren är på startsidan
    Then texten "Läslistan" ska visas
    And texten "Välkommen!" ska visas
    And texten "Sidan för dig som gillar att läsa. Välj dina favoriter." ska visas

