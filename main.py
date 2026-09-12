import sqlite3
import csv

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

    def artikle(self, w: str):
        w = w.capitalize()
        with open('nouns.csv', encoding= 'utf-8') as nouns:
                csv_f = csv.DictReader(nouns)
                genus = [(row['genus']) for row in csv_f if (row['lemma']) == w]
                match genus[0]:
                     case 'n':
                          return 'das' + ' ' + w
                     case 'f':
                          return 'die' + ' ' + w
                     case 'm':
                          return 'der' + ' ' + w

def main():
    word = Translator()
    print(word.artikle(input('write a word: ')))


if __name__ == "__main__":
    main()