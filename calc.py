import string

def parser(equ, symbols, numbers, position):    # function parses numbers and symbols from user input string
    firstDigit = 0                      # initializes variable to point to the first digit in a number          
    
    for i in range(len(equ)):           # this loop runs through the user input and adds any symbols to the symbols list
        if(equ[i] not in string.digits and equ[i] not in string.ascii_letters):     # condition for non-number non-letter symbols
            symbols.append(equ[i])      # append symbols to list
            position.append(i)          #append symbol position to list

    position.append(len(equ)+1)         # adds a symbol to the end of the user input for use in the next loop
    
    for i in range(len(position)):      # this loop finds numbers in the user input and adds them to the numbers list
        numbers.append(equ[firstDigit: int(position[i])])   # append numbers to list
        firstDigit = int(position[i]) + 1                   # set firstDigit equal to the first character after the current symbol in the user input


def calc(equ, symbols, numbers):    # function does simple calculations using parsed numbers and symbols
    sum = 0                         # initialize sum to the value of the first number in the equation
    while('*' in symbols):          # while loop to check if any multiplication is left to be done
        for i in range(len(symbols)):       
            if(symbols[i] == "*"):          
                sum = int(numbers[i]) * int(numbers[i+1])   # preform opperation on numbers before and after the opperator
                del numbers[i]                              #delete the numbers we opperated on
                del numbers[i]
                numbers.insert(0, sum)                      #insert their new value into the numbers list
                del symbols[i]                              #delete the opperand from the symbols list
                break                                       #we must break out of the for loop because deleting a symbol has changed the length of our symbols list, this is the reason for the while loop

    while('/' in symbols):          # while loop to check if any division is left to be done
        for i in range(len(symbols)):
            if(symbols[i] == "/"):  
                sum = int(numbers[i]) / int(numbers[i+1])
                del numbers[i]
                del numbers[i]
                numbers.insert(0, sum)
                del symbols[i]
                break

    while('+' in symbols):          # while loop to check if any addition is left to be done
        for i in range(len(symbols)):
            if(symbols[i] == "+"):  
                sum = int(numbers[i]) + int(numbers[i+1])
                del numbers[i]
                del numbers[i]
                numbers.insert(0, sum)
                del symbols[i]
                break

    while('-' in symbols):          # while loop to check if any subtraction is left to be done
        for i in range(len(symbols)):
            if(symbols[i] == "-"):  
                sum = int(numbers[i]) - int(numbers[i+1])
                del numbers[i]
                del numbers[i]
                numbers.insert(0, sum)
                del symbols[i]
                break

    return sum


def main():
    symbols = list()  # initialize list for mathematical symbols
    position = list()
    numbers = list()  # initialize list for numbers
    equ = ""  # initialize user input equation

    while True:
        print("Enter simple equation to calculate:")

        equ = input()  # user input
        if(equ == "exit"):  # keyword 'exit' to end program
            break

        parser(equ, symbols, numbers, position)  # call to parser function
        # call to calc function and print result
        print("%s = %d \n" % (equ, calc(equ, symbols, numbers)))

        symbols.clear()  # reset symbol list
        numbers.clear()  # reset number list


if __name__ == "__main__":
    main()
