for case in range(1, int(input()) + 1):
    word = input()
    N = len(word)
    print(f'{"..#." * N}.')
    print(f'{".#.#" * N}.')
    print(f'#.{".#.".join(word)}.#')
    print(f'{".#.#" * N}.')
    print(f'{"..#." * N}.')
    