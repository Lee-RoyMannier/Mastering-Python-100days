def add(nb1, nb2):
    return nb1 + nb2


def sub(nb1, nb2):
    return nb1 - nb2


def multiply(nb1, nb2):
    return nb1 * nb2


def divide(nb1, nb2):
    try:
        result = nb1 / nb2
    except ZeroDivisionError:
        print("Cannot divide by 0")
        return
    else:
        return result


logo = '''
___                            ___
 ||  |   ___         ___        ||  |
 || _|__/  _\_______/  _\_______|| _|
 ||(___(  (________(  (_________||((_)
 ||  |  \___/       \___/       ||  |
 ||  |         ___              ||  |
 || _|________/  _\_____________|| _|
 ||(_________(  (_______________||((_)
 ||  |        \___/             ||  |
 ||  |                          ||  |
 ||  |                          ||  | lf
 ||  |                          ||  |'''

calc = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}


def calculator():
    app_runnig = True
    first_number = float(input("'What's the first number? "))

    print(logo)

    while app_runnig:
        for op in calc:
            print(op)
        operation = input("pick an operation: ")

        if operation not in calc.keys():
            print("Invalid opération")
            continue
        else:
            next_number = float(input("What's the next number? "))
            resultat = calc[operation](first_number, next_number)
            print(f"{first_number} {operation} {next_number}= {
                resultat}")
            first_number = resultat

            continue_cal = input("Type y to continue or n")
            if continue_cal == "n":
                app_runnig = False
                calculator()


calculator()
