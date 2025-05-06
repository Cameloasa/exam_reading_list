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
**Vill jag** kunna se och använda navigeringsknapparna i toppmenyn  
**Så att** jag enkelt kan växla mellan "Katalog", "Lägg till bok" och se "Mina böcker".

### Acceptanskriterier

1. När användaren öppnar startsidan **ska alla tre knappar vara synliga**:
   - "Katalog"
   - "Lägg till bok"
   - "Mina böcker"
   - 
2. En knapp ska vara **inaktiverad på** sin egen sektion

---

# User Story: Lägga till en ny bok i katalogen

**Som** användare  
**Vill jag** kunna lägga till en ny bok via formuläret, 
**Så att** den visas i katalogen.

## Acceptanskriterier

### Scenario 1: Formuläret visas när användaren klickar på navigeringsknappen "Lägg till bok"
- **Given** användaren är på startsidan
- **When** användaren klickar på navigeringsknappen "Lägg till bok"
- **Then** fältet "Titel" ska vara synligt
- **And** fältet för författare ska vara synligt
- **And** knappen "Lägg till ny bok" ska vara inaktiverad

### Scenario 2: Användaren fyller i formuläret och lägger till bok
- **Given** användaren är på startsidan
- **When** användaren klickar på navigeringsknappen "Lägg till bok"
- **And** användaren fyller i "Titel" med "<titel>"
- **And** användaren fyller i "Författare" med "<författare>"
- **Then** knappen "Lägg till ny bok" ska vara aktiverad
- **When** användaren klickar på knappen "Lägg till ny bok"
- **And** användaren klickar på navigeringsknappen "Katalog"
- **Then** boken "<titel>" av "<författare>" ska visas i katalogen

### Test Examples
- **Titel:** Mio min Mio, **Författare:** Astrid Lindgren
- **Titel:** Bröderna Lejonhjärta, **Författare:** Astrid Lindgren
- **Titel:** Pippi Långstrump, **Författare:** Astrid Lindgren

---

# User Story: Bokkatalog

**Som** användare 
**vill jag** kunna se en lista med böcker i katalogen 
**så att** jag kan titta på alla tillgängliga böcker

## Acceptanskriterier:

1. Användaren är på **startsidan**, som motsvarar "Katalogen".
2. Användaren kan se en lista med böcker på startsidan, där varje bok har titel och författare.

## Scenario: Visa böcker i katalogen

**Given** användaren är på startsidan som motsvarar "Katalogen"
**When** boken "<titel>" av "<författare>" visas i katalogen
**Then** användaren ska kunna se "<titel>" och "<författare>" i katalogen

---

## User Story: Favoritböcker

**Som** användare 
**vill jag** kunna se en lista med böcker i katalogen 
**så att** jag kan välja mina favorit böcker


## Acceptanskriterier:

1. Användaren är på **startsidan**, som motsvarar "Katalogen".
2. Användaren klickar på hjärtat bredvid "<titel>"
3. Användaren klickar på navigeringsknappen "Mina böcker"
4. boken "<titel>" av "<författare>" visas i Mina böcker

