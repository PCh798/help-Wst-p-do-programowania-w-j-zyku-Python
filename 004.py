# Napisać funkcję przyjmującą jako parametr listę stringów i zwracającą string będący ich połączeniem:
# Przykład:
# Lista: ['P', 'y', 't', 'h', 'o', 'n']
# Zwracany wynik: 'Python'

letters = ['P', 'y', 't', 'h', 'o', 'n']

result_word = []
for elem in letters:
    result_word = "".join(letters)

if __name__ == '__main__':
    print(result_word)


