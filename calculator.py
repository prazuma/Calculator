def readNumber(line, index):
    number = 0
    divide = 10
    point = False
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
       if line[index] == '.':
           point = True
	   index += 1
       if point == False:
           number = number * 10 + float(line[index])
           index += 1
       else:
           number = number + float(line[index]) / divide
           divide *= 10
           index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMul(line, index):
    token = {'type': 'MUL'}
    return token, index + 1

def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1

def tokenize(line):
    """
    Tokenize the input line and return a list of tokens
    """
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def calcMulAndDiv(tokens):
    """
    Calculate only Multiplication and Division.
    return a calculated result
    """
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'MUL':
            number1 = tokens[index - 1]['number']
            number2 = tokens[index + 1]['number']
            tokens[index - 1]['number'] = number1 * number2
            tokens.pop(index + 1)
            tokens.pop(index)
        elif tokens[index]['type'] == 'DIV':
            number1 = tokens[index - 1]['number']
            number2 = tokens[index + 1]['number']
            if number2 == 0:
                print 'Invalid syntax(zero divide)'
                exit(1)
            tokens[index - 1]['number'] = number1 / number2
            tokens.pop(index + 1)
            tokens.pop(index)
        else:
            index += 1
    return tokens

def evaluate(tokens):
    """
    Evaluate the list of tokens and return a calculated result
    """
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    lenToken = len(tokens)
    tokens = calcMulAndDiv(tokens)
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print tokens[index - 1]['type']
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    print tokens
    answer = evaluate(tokens)
    print "answer = %d\n" % answer
