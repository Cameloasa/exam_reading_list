## User Story: Se statisk sidoinformation i varje sektion

**Som** en användare  
**Vill jag** kunna se samma titel och välkomstmeddelande i alla sektioner  
**Så att** jag vet att jag är på rätt plats och att sidan fungerar konsekvent

### Acceptanskriterier:
- Sidans huvudrubrik `<h1>` ska alltid visa "Läslistan"
- Välkomsttexten "Välkommen!" och introduktionstexten ska alltid visas i huvudsektionen

---

## User Story: Navigering i applikationen

**Som** användare  
**vill jag** kunna se och använda navigeringsknapparna i toppmenyn  
**så att** jag enkelt kan växla mellan "Katalog", "Lägg till bok" och se "Mina böcker".

### Acceptanskriterier

1. När användaren öppnar startsidan **ska alla tre knappar vara synliga**:
   - "Katalog"
   - "Lägg till bok"
   - "Mina böcker"
   - 
2. En knapp ska vara **inaktiverad på** sin egen sektion

---

# User Story: Lägga till en ny bok i katalogen

## Som användare
Jag vill kunna lägga till en ny bok via formuläret, 
så att den visas i katalogen.

## Acceptanskriterier

### Scenario 1: Formuläret visas när användaren klickar på navigationsknappen "Lägg till bok"
- **Given** användaren är på startsidan
- **When** användaren klickar på navigationsknappen "Lägg till bok"
- **Then** formuläret visas
- **And** fältet för titel ska vara synligt
- **And** fältet för författare ska vara synligt
- **And** navigationsknappen "Lägg till ny bok" ska vara inaktiverad

### Scenario 2: Användaren fyller i formuläret och lägger till bok
- **Given** användaren är på startsidan
- **When** användaren klickar på navigationsknappen "Lägg till bok"
- **And** användaren fyller i "Titel" med "<titel>"
- **And** användaren fyller i "Författare" med "<författare>"
- **Then** navigationsknappen "Lägg till ny bok" ska vara aktiverad
- **When** användaren klickar på navigationsknappen "Lägg till ny bok"
- **Then** boken "<titel>" av "<författare>" ska sparas i katalogen

### Test Examples
- **Titel:** Mio min Mio, **Författare:** Astrid Lindgren
- **Titel:** Bröderna Lejonhjärta, **Författare:** Astrid Lindgren
- **Titel:** Pippi Långstrump, **Författare:** Astrid Lindgren