import sqlite3
import csv
import random

class Translator:

    def __init__(self, w: str):
        self.w = w
        self.starter = sqlite3.connect("dictionary-de.db")
        self.syn = self.starter.cursor()

    def de_to_en(self):
        syn = self.syn
        meaning = syn.execute("SELECT gloss FROM senses WHERE word = ?", (self.w,))
        des = meaning.fetchall()
        if not des:
            return 'no word found :('
        for _ in des:
            print(_[0])

    def en_to_de(self):
        syn = self.syn
        meaning = syn.execute("SELECT word FROM senses WHERE gloss = ? ", (self.w,))
        des = meaning.fetchall()
        if not des:
            return 'no word found :('
        for _ in des:
            print(_[0])

    def artikle(self):
        w = self.w.capitalize()
        with open('nouns.csv', encoding= 'utf-8') as nouns:
            csv_f = csv.DictReader(nouns)
            genus = [(row['genus']) for row in csv_f if (row['lemma']) == w]
            try:
                match genus[0]:
                    case 'n':
                        return 'das' + ' ' + w
                    case 'f':
                        return 'die' + ' ' + w
                    case 'm':
                        return 'der' + ' ' + w
            except IndexError:
                return ('Word not found :( ')


    def plural(self):
        w = self.w.capitalize()
        with open('nouns.csv', encoding= 'utf-8') as nouns:
            csv_f = csv.DictReader(nouns)
            plural = [row['nominativ plural'] for row in csv_f if (row['lemma'])== w]
            if not plural:
                return 'No word found :('
            return ', '.join(plural) 

        

def main():
    connection = sqlite3.connect("dictionary-de.db")
    word_all = connection.cursor()
    word_get = word_all.execute("SELECT word FROM SENSES WHERE pos = 'noun' ")
    word = random.choice(word_get.fetchall())[0]
    diction = Translator(word)
    ask = input('Wanna know the word of the day? if yes, type yes:  ').capitalize()
    if ask.startswith('Ye'):
        print(f"Word: {word}\nPlural: {diction.plural()}\nArticle: {diction.artikle()}")
        print("..................meaning....................")
        diction.de_to_en()
    else:
        ask_again = input('Wanna search a word? ').capitalize()
        if ask_again.startswith('Ye'):
            find_meaning = input('What word do you wan to know about? ')
            find_meaning = Translator(find_meaning)
            en_or_de = input('Is the word English or German? ').capitalize()
            if en_or_de == 'English':
                find_meaning.en_to_de()
            else:
                find_meaning.de_to_en()

if __name__ == "__main__":
    main()