def fizzbuzz(rules):
    for i in range(1, 101):
        output = ''
        for condition, word in rules:
            if condition(i):
                output += word
        print(f'{i}. {output}' if output else f'{i}.')

# Example usage:
rules = [
    (lambda x: x % 3 == 0, 'buzz'),
    (lambda x: x % 5 == 0, 'fizz'),
]

fizzbuzz(rules)
