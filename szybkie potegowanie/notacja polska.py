def obliczRpm(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                raise ValueError('Niewystarczająco operatorów dla operatora')
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError('Dzielenie przez zero')
                result = a / b
            stack.append(result)

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError('Niewłaściwa liczba operatorów')

expression1 = '20 4 / 5 + 4 *'
result1 = obliczRpm(expression1)
print(f'Wynik wyrażenia {expression1} to {result1}')