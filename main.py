meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "OMG": "Abbreviazione in inglese di 'OH MIO DIO'",
            "CAP": "Parola usata per indicare una bugia",
            "DRIP": "Un senso di stile 'figo'",
            "GOAT": "Abbreviazione in inglese di 'Migliore di tutti i tempi' ",
            "GG": "Abbreviazione in inglese di 'Bella giocata', 'Bella partita'"
            }
saluto = print("Ciao! Io sono Trnslatr! Qui potrai chiedermi qualsiasi parola appartenente allo sleng Gen Z")
while True:
    chiedi = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    if chiedi in meme_dict.keys():
        print(meme_dict[chiedi])
    else:
        print("Type Error: Parola non trovata")
