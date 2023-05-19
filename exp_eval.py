from stack_array import Stack


# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass


def check_div(operator: str, operand: str) -> None:
    """Checks for divide by 0 error"""
    """Input argument:  a string containing an operator and a string containing an operand
    Returns None or an error. 
    Will be used in the postfix_eval function"""
    if operator == "/" and operand == "0":
        raise ValueError


def check_token(input_str: str) -> None:
    """Checks for invalid tokens"""
    """Input argument:  a string containing the postfix expression
    Returns None or an error. 
    Will be used in the postfix_eval function"""
    lis = input_str.split()
    for i in lis:
        if i[0] not in "0123456789" and i[0] not in "-+/**>><<":
            raise PostfixFormatException("Invalid token")


def check_operands(input_str: str) -> None:
    """Checks for too many or too few operands"""
    """Input argument:  a string containing the postfix expression
    Returns None or an error. 
    Will be used in the postfix_eval function"""
    lis = input_str.split()
    if input_str == "":
        raise PostfixFormatException("Insufficient operands")
    operator_count = 0
    operand_count = 0
    for i in lis:
        if i in "-+/**>><<":
            operator_count += 1
        else:
            operand_count += 1
    if operand_count <= operator_count:
        raise PostfixFormatException("Insufficient operands")
    if operand_count - 1 > operator_count:
        raise PostfixFormatException("Too many operands")


def check_illegal_bit(operand1: str, operand2: str, operator: str) -> None:
    """Checks for an illegal bit operation"""
    """Input argument:  a string containing an operator, a string containing the first operand and a
    string containing the second operand.
    Returns None or an error. 
    Will be used in the postfix_eval function"""
    if ("." in operand1 or "." in operand2) and (operator == ">>" or operator == "<<"):
        raise PostfixFormatException("Illegal bit shift operand")


def postfix_eval(input_str: str) -> float:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    check_token(input_str)
    check_operands(input_str)
    s = Stack(30)
    lis = input_str.split()
    for i in lis:
        if i[0] in "01234567890":
            s.push(i)
        elif len(i) > 1 and i[0] == "-":
            s.push(i)
        else:
            num1 = s.pop()
            num2 = s.pop()
            check_div(i, num1)
            check_illegal_bit(num1, num2, i)
            s.push(str(eval(num2 + i + num1)))
    return float(s.pop())


def prec(operator: str) -> int:
    """Assigns a numerical value for a given operator"""
    """Input argument:  a string containing an operator. One of the following: + - * / ** << >>
    Returns an integer representing the operator. 
    Will be used in the infix_to_postfix function to compare precedence of two operators"""
    operations = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3, '<<': 4, ">>": 4}
    return operations.get(operator, 0)


def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    s = Stack(30)
    output = ""
    lis = input_str.split()
    for i in lis:
        if i[0] in "0123456789":
            if len(output) == 0:
                output = output + i
            else:
                output = output + " " + i
        elif len(i) > 1 and i[0] == "-":
            if len(output) == 0:
                output = output + i
            else:
                output = output + " " + i
        elif i == "(":
            s.push(i)
        elif i == ")":
            while s.peek() != "(":
                output = output + " " + s.pop()
            s.pop()
        elif i in "-+/**>><<":
            while s.is_empty() is False and s.peek() in "-+/**>><<" and (
                    (i not in "**" and prec(i) <= prec(s.peek())) or (i in "**" and prec(i) < prec(s.peek()))):
                output = output + " " + s.pop()
            s.push(i)
    while s.is_empty() is False:
        output = output + " " + s.pop()
    return output


def prefix_to_postfix(input_str: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    s = Stack(30)
    lis = input_str.split()
    output = ""
    for i in reversed(lis):
        if i[0] in "0123456789":
            s.push(i)
        elif len(i) > 1 and i[0] == "-":
            s.push(i)
        else:
            op1 = s.pop()
            op2 = s.pop()
            string = op1 + " " + op2 + " " + i
            s.push(string)
    while s.is_empty() is False:
        if len(output) == 0:
            output = output + s.pop()
        else:
            output = output + " " + s.pop()
    return output
