import sqlite3

class Translator:
    starter = sqlite3.connect("dictionary-de.db")
    syn = starter.cursor()

    def __init__(self):
        pass

    def de_to_en(self, w: str):
        syn = self.syn
        meaning = syn.execute(f"SELECT gloss FROM senses WHERE word = '{w}' AND sort_order = 0")
        return meaning.fetchone()[0]

    def en_to_de(self, w: str):
        syn = self.syn
        meaning = syn.execute(f"SELECT word FROM senses WHERE gloss ='{w}'")
        return meaning.fetchone()[0]
    

def main():
    word = Translator()
    print(word.de_to_en(input("Ger Word: ")))
    print(word.en_to_de(input("Eng Word: ")))


if __name__ == "__main__":
    main()