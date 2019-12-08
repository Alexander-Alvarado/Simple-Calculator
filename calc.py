import string

def parser(equ, symbols, numbers):      #function parses numbers and symbols from user input string
    firstDigit = 0                      #initializes variable to point to the first digit in a number

    for i in range(len(equ)):           #this loop runs through the user input and adds any symbols to the symbols list
        if(equ[i] not in string.digits and equ[i] not in string.ascii_letters): #condition for non-number non-letter symbols
            symbols.append(i)           #append symbols to list

    symbols.append(len(equ)+1)          #add a temporary symbol to the end of the user input for use in the next loop

    for i in range(len(symbols)):       #this loop finds numbers in the user input and adds them to the numbers list
        numbers.append(equ[firstDigit : int(symbols[i])])   #append numbers to list
        firstDigit = int(symbols[i]) + 1                    #set firstDigit equal to the first character after the current symbol in the user input
    
    symbols.pop()       #pop temporary symbol

def calc(equ, symbols, numbers):    #function does simple calculations using parsed numbers and symbols
    sum = int(numbers[0])           #initialize sum to the value of the first number in the equation

    for i in range(len(symbols)):       #this loop calculates each sub equation returns the overall total
        if(equ[symbols[i]] == "+"):     #addition
            sum += int(numbers[i+1])

        elif(equ[symbols[i]] == "-"):   #subtraction
            sum -= int(numbers[i+1])

        elif(equ[symbols[i]] == "*"):   #multiplication
            sum = sum * int(numbers[i+1])

        elif(equ[symbols[i]] == "/"):   #division
            sum = sum / int(numbers[i+1])

        else:
            print("--This mathematical operator is not supported--")
            exit(1)
    return sum  #return total

def main():
    symbols = list()    #initialize list for mathematical symbols
    numbers = list()    #initialize list for numbers
    equ = ""            #initialize user input equation

    while True:
        print("Enter simple equation to calculate:")

        equ = input()       #user input
        if(equ == "exit"):  #keyword 'exit' to end program
            break

        parser(equ, symbols, numbers)  #call to parser function
        print("%s = %d \n" % (equ, calc(equ,symbols,numbers))) #call to calc function and print result

        symbols.clear()    #reset symbol list
        numbers.clear()    #reset number list

if __name__ == "__main__":
    main()
