def validar_expressao(expressao):
    limitadores = {'(' : ')', '{' : '}', '[' : ']'}
    pilha = []

    for char in expressao:
        if char in limitadores:
            pilha.append(char)
        elif char in limitadores.values():
            if not pilha or limitadores[pilha.pop()] != char:
                return False

    return not pilha

expressoes = [
    "3 * [(5 - 2) + (4 - 2)]",
    "a{[b(c*d)+(b+c)]*[a-b(b/c)]}*5",
    "a[d]",
    "a{b[c]d}e",
    "a{b(c]d}e",
    "a[b{c}d]e}",
    "a{b(c)"
]

print(validar_expressao("a[b{c}d]e}"))
