meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GG": "iyi oyun",
            "MEEM":"görsellerle yapılan mizah",
            "OMG":"vay canınaaa"
            "AGGRO":"agresifleşmek/sinirlenmek"
            
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict:
        if word == "CRINGE":
            print("bu kelimenin anlamı: garip ya da utandırıcı bir şey")
        if word == "LOL":
            print("bu kelimenin anlamı: Komik bir şeye verilen cevap")
        if word == "GG":
            print("bu kelimenin anlamı: iyi oyun")
        if word == "MEEM":
            print("bu kelimenin anlamı: görsellerle yapılan mizah")
        if word == "OMG":
            print("bu kelimenin anlamı: vay canınaaa")
        if word == "AGGRO":
            print("bu kelimenin anlamı: ")
    else:
        print("bu sözlükte bu kelime bulunmamaktadır.")
