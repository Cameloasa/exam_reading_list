Feature: Lägga till en ny bok i katalogen

  Som användare
  Vill jag kunna lägga till en ny bok via formuläret
  Så att den visas i katalogen

  Scenario: Formuläret visas när användaren klickar på navigeringsknappen "Lägg till bok"
    Given användaren är på startsidan
    When användaren klickar på navigeringsknappen "Lägg till bok"
    Then ska formuläret visas
    And fältet för titel ska vara synligt
    And fältet för författare ska vara synligt
    And knappen "Lägg till ny bok" ska vara inaktiverad

  Scenario Outline: Användaren fyller i formuläret och lägger till bok
    Given användaren är på startsidan
    When användaren klickar på navigeringsknappen "Lägg till bok"
    And användaren fyller i "Titel" med "<titel>"
    And användaren fyller i "Författare" med "<författare>"
    Then knappen "Lägg till ny bok" ska vara aktiverad
    When användaren klickar på knappen "Lägg till ny bok"
    Then boken "<titel>" av "<författare>" ska sparas i katalogen

  Examples:
    | titel                 | författare          |
    | Mio min Mio           | Astrid Lindgren     |
    | Bröderna Lejonhjärta  | Astrid Lindgren     |
    | Pippi Långstrump      | Astrid Lindgren     |
