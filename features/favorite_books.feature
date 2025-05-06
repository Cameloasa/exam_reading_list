Feature: Favoritböcker

  Som användare
  vill jag kunna se en lista med böcker i katalogen
  så att jag kan välja mina favorit böcker

  Scenario Outline: Användaren lägger till en bok som favorit och ser den i "Mina böcker"
    Given användaren är på startsidan
    And boken "<titel>" av "<författare>" visas i katalogen
    When användaren klickar på hjärtat bredvid "<titel>"
    And användaren klickar på navigeringsknappen "Mina böcker"
    Then boken "<titel>" av "<författare>" visas i Mina böcker

  Examples:
    | titel                          | författare     |
    | Min katt är min chef           | Kattis Jamsson |