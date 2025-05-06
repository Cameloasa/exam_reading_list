Feature: Visa bokkatalog lista

  För att kunna välja bland tillgängliga böcker
  Som en användare
  Vill jag kunna se en lista med böcker i katalogen

  Scenario Outline: Användaren ser en lista med böcker i katalogen
    Given användaren är på startsidan
    When boken "<titel>" av "<författare>" visas i katalogen
    Then användaren ska kunna se "<titel>" och "<författare>" i katalogen

  Examples:
    | titel                                                       | författare        |
    | Mio min Mio                                                 | Astrid Lindgren   |
    | Bröderna Lejonhjärta                                        | Astrid Lindgren   |
    | Pippi Långstrump                                            | Astrid Lindgren   |
    | Hur man tappar bort sin TV-fjärr 10 gånger om dagen         | Bertil Flimmer    |
    | Kaffekokaren som visste för mycket                          | Saga Espresson    |
    | Min katt är min chef                                        | Kattis Jamsson    |
    | 100 sätt att undvika måndagar                               | Göran Snooze      |
    | Gräv där du står – och hitta en pizzameny                   | Maja Skruv        |
    | Jag trodde det var tisdag                                   | Kim Vilsen        |
    | Att prata med växter – och vad de egentligen tycker om dig  | Flora Tistel      |
