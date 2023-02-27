class DictEntry:
    def __init__(self, name, surname, birth_date, birth_place, fav_books):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.fav_books = fav_books

    def print_entry(self, *args):
        return "Imię i nazwisko:", self.name, self.surname, "Data urodzenia:", self.birth_date, "Miejsce urodzenia", self.birth_place, "Ulubione książki", self.fav_books

if __name__ == "__main__":
    name = str(input("Podaj imię \n"))
    surname = str(input("Podaj nazwisko \n"))
    birth_date = str(input("Podaj datę urodzenia \n"))
    birth_place = str(input("Podaj miejsce urodzenia \n"))
    books_list = []
    while True:
        fav_books = str(input("Podaj ulubione ksiażki \n"))
        if fav_books == 'q':
            break
        if fav_books != 'q':
            books_list.append(fav_books)


user_entry = DictEntry(name, surname, birth_date, birth_place, fav_books)

print(f'Dane postaci: {user_entry.print_entry()}')
