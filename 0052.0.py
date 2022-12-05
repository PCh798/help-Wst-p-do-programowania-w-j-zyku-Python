# Napisać funkcję przyjmującą jako parametr listę i zwracającą True,
# jeśli którykolwiek jej element jest listą, False w każdym innym razie.

# Przykład 1:
# Lista: [15, 'abcd', 42]
# Zwrócony wynik: False

# Przykład 2:
# Lista: [77, [1, 2, 3], {'haslo': 'Jozef Tkaczuk'}]
# Zwrócony wynik: True

list_one = [15, 'abcd', 42]
list_two = [77, [1, 2, 3], {'haslo': 'Jozef Tkaczuk'}]


def is_nested_list(l):

    try:
          next(x for x in l if isinstance(x,list))

    except StopIteration:
        return False

    return True


if __name__ == "__main__":
    print(is_nested_list(list_one))
    print(is_nested_list(list_two))


