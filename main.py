import sqlite3

def main():
    get_word('bild')

def get_word(w: str):
    starter = sqlite3.connect("dictionary-de.db")

if __name__ == "__main__":
    main()