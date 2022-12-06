class InvalidSyntax(Exception):
    pass

cmd_line = 'a = 10 + 2'

try:
    tokens = cmd_line.split()
    if len(tokens) != 3:
        raise InvalidSyntax('Expressions should have only var, op, val')
    print('Syntax is fine', tokens)
except InvalidSyntax:
    print('InvalidSyntax')




