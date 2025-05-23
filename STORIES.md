# STORIES.md – User Stories för Läslistan

---

## 1. Se statisk sidoinformation i varje sektion

**Som** en användare  
**Vill jag** kunna se samma titel och välkomstmeddelande i alla sektioner  
**Så att** jag vet att jag är på rätt plats och att sidan fungerar konsekvent

### Acceptanskriterier:
- Sidans huvudrubrik `<h1>` ska alltid visa "Läslistan"
- Välkomsttexten "Välkommen!" och introduktionstexten ska alltid visas i huvudsektionen

---

## 2. Navigering i applikationen

**Som** användare  
**Vill jag** kunna se och använda navigeringsknapparna i toppmenyn  
**Så att** jag enkelt kan växla mellan "Katalog", "Lägg till bok" och se "Mina böcker"

### Acceptanskriterier:
1. När användaren öppnar startsidan **ska alla tre knappar vara synliga**:
   - "Katalog"
   - "Lägg till bok"
   - "Mina böcker"
2. En knapp ska vara **inaktiverad** på sin egen sektion

---

## 3. Lägga till en ny bok i katalogen

**Som** användare  
**Vill jag** kunna lägga till en ny bok via formuläret  
**Så att** den visas i katalogen

### Scenario 1: Formuläret visas
- **Given** användaren är på startsidan  
- **When** användaren klickar på navigeringsknappen "Lägg till bok"  
- **Then** fältet "Titel" ska vara synligt  
- **And** fältet för författare ska vara synligt  
- **And** knappen "Lägg till ny bok" ska vara inaktiverad  

### Scenario 2: Lägg till bok
- **Given** användaren är på startsidan  
- **When** användaren klickar på "Lägg till bok"  
- **And** fyller i "Titel" med "<titel>"  
- **And** fyller i "Författare" med "<författare>"  
- **Then** knappen "Lägg till ny bok" ska vara aktiverad  
- **When** användaren klickar på "Lägg till ny bok"  
- **And** klickar på "Katalog"  
- **Then** boken "<titel>" av "<författare>" ska visas i katalogen  

#### Exempel:
- Titel: Mio min Mio, Författare: Astrid Lindgren  
- Titel: Bröderna Lejonhjärta, Författare: Astrid Lindgren  
- Titel: Pippi Långstrump, Författare: Astrid Lindgren

---

## 4. Visa böcker i katalogen

**Som** användare  
**Vill jag** kunna se en lista med böcker i katalogen  
**Så att** jag kan titta på alla tillgängliga böcker

### Acceptanskriterier:
1. Startsidan visar katalogen  
2. Varje bok ska visa både titel och författare  

### Scenario outline: Användaren ser en lista med böcker i katalogen
- **Given** användaren är på startsidan  
- **When** boken "<titel>" av "<författare>" visas i katalogen  
- **Then** användaren ska kunna se "<titel>" och "<författare>"  

---

## 5. Lägga till Favoritböcker

**Som** användare  
**Vill jag** kunna markera böcker som favoriter  
**Så att** jag snabbt hittar mina favoriter i sektionen "Mina böcker"

### Acceptanskriterier:
1. Användaren är i katalogen  
2. Klickar på hjärtat bredvid "<titel>"  
3. Går till "Mina böcker"  
4. Ser boken "<titel>" av "<författare>" i "Mina böcker"

### Scenario outline: Användaren lägger till en bok som favorit och ser den i "Mina böcker"
- **Given** användaren är på startsidan  
- **Then** boken "<titel>" av "<författare>" visas i katalogen 
- **When** användaren favoritmarkerar boken "<titel>"
- **And** användaren klickar på navigeringsknappen "Mina böcker"
- **Then** användaren ska kunna se "<titel>" och "<författare>" i "Mina böcker"

## 6. Ta bort Favoritböcker

**Som** användare  
**Vill jag** kunna ta bort en bok från mina favoriter
**Så att** jag kan ångra ett val eller uppdatera min lista

### Acceptanskriterier:
1. Användaren är i katalogen  
2. Klickar på hjärtat bredvid "<titel>"  
3. Går till "Mina böcker"  
4. Ser boken "<titel>" av "<författare>" i "Mina böcker"
5. Användaren går till "Katalog"
6. Klickar på hjärtat bredvid "<titel>" 
7. Går till "Mina böcker"  
8. Ser inte boken "<titel>" av "<författare>" i "Mina böcker"

### Scenario: En användare favoritmarkerar och sedan avmarkerar en bok
- **Given** användaren är på startsidan  
- **Then** boken "<titel>" av "<författare>" visas i katalogen 
- **When** användaren favoritmarkerar boken "<titel>"
- **And** användaren klickar på navigeringsknappen "Mina böcker"
- **Then** användaren ska kunna se "<titel>" och "<författare>" i "Mina böcker"
- **When** användaren klickar på navigeringsknappen "Katalog"
- **Then** användaren favoritmarkerar boken "<titel>"
- **And** användaren klickar på navigeringsknappen "Mina böcker"
- **Then** användaren ska inte kunna se "<titel>" och "<författare>" i "Mina böcker"

### Scenario outline: En användare favoritmarkerar två böcker och avmarkerar en

## 7. Växlande favoritstatus vid upprepade klick

**Som** användare  
**Vill jag** favoritmarkering ska växla varje gång jag klickar på hjärtat
**Så att** det alltid stämmer med min avsikt.

### Acceptanskriterier:
1. Användaren är i katalogen  
2. Klickar på hjärtat bredvid "<titel>"  
3. Går till "Mina böcker"  
4. Ser boken "<titel>" av "<författare>" i "Mina böcker"
5. Användaren går till "Katalog"
6. Klickar på hjärtat bredvid "<titel>" 
7. Går till "Mina böcker"  
8. Ser inte boken "<titel>" av "<författare>" i "Mina böcker"
9. Upprepa flera gånger

### Scenario:
- **Given** användaren är på startsidan  
- **Then** boken "<titel>" av "<författare>" visas i katalogen 
- **When** användaren favoritmarkerar boken "<titel>"
- **And** användaren klickar på navigeringsknappen "Mina böcker"
- **Then** användaren ska kunna se "<titel>" och "<författare>" i "Mina böcker"
- **When** användaren klickar på navigeringsknappen "Katalog"
- **Then** användaren favoritmarkerar boken "<titel>"
- **And** användaren klickar på navigeringsknappen "Mina böcker"
- **Then** användaren ska inte kunna se "<titel>" och "<författare>" i "Mina böcker"




  

