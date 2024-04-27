from RiceFunctions import riceFunctions as rice

def main():
    print("Bits required to encode in a natural binary, the values from -1023 to 1023:", bitsNeedToCodify(-1023, 1023), "bits.")

    encodedRice = rice.encodeRice(256, 578)
    decodedRice = rice.decodeRice(encodedRice, 256)

    print("Example with M = 256 and N = 578 for encode with Rice algorithm:", encodedRice)
    print("Example with M = 256 and encodedNumber =", encodedRice, " for decode with Rice algorithm:", decodedRice)
    
    listEncodedRice = calculateRiceEncodedRange(-1023, 1023, 32)

    print("List of the number from -1023 to 1023 encoded with the algorithm Rice: ")
    for (num, encodedNum) in listEncodedRice[1::]:
        print("Number:", num, "Encoded number:", encodedNum)

    print("List of the numbers that require less bits with the rice codification than with the natural binary codification:", checkBits(listEncodedRice))
def bitsNeedToCodify(fNum, sNum):
    '''
    Method to calculate the number ob bits necessary to encode all the numbers between a 
    range (fNumb, sNumb), in a natural binary encode. 

    Args:
        - fNum(int): first number from where we want to codify, should be the bigest one. 
        - sNum(int): second number to where we want to codify, should be the smallest one. 
    Return: 
        - nBits(int): number of bits to do the encode. 
    '''

    if (abs(fNum) >= abs(sNum)):                                    # Check if the absolute value of the first number is bigger or equal than the absolute value of the second number.   
        nBits = len(rice.calculNaturalBinaryBits(fNum)) + 1         # If the first number is bigger we calculate the number of bits of the value + 1 (the sign + or -)
    else:                                                           # Check if the absolute value of the second number is smaller than the first one. 
        nBits = len(rice.calculNaturalBinaryBits(sNum)) + 1         # Calculate the number of bits of the second number + 1 (the sign + or -)
    
    return nBits
    
def calculateRiceEncodedRange(num1, num2, M):
    '''
    Method to calculate the Rice code for all the integer numbers from num1 to num2 with a specific M.

    Args:
        - num1(int): firs limit number.
        - num2(int): second limit number. 
        - M(int): Integer value, power of 2, necessary to the encode.

    Returns:
        - listEncodedRice(list): A list of tuples, where the first value is the decimal 
                                 number and the second value is the encoded number with Rice. 
                                 The first element of the list is the value M
    '''
    listEncodedRice = []
    listEncodedRice.append(M)

    for num in range(min(num1, num2), max(num1, num2) + 1):
        listEncodedRice.append((num, rice.encodeRice(M, num)))

    return listEncodedRice

def checkBits(listEncodedRice):
    '''
    Method to check if the compression with Rice is optimal or is not. 

    Args:
        - listEncodedRice(list): A list of tuples, where the first value is the decimal 
                                 number and the second value is the encoded number with Rice. 
                                 The first element of the list is the value M
    Returns:
        - optimalNumbers(list): List wit the numbers that are optimal compressed with Rice algorithm, 
                                so the length of the encoded number is smaller that the natural binary number.
    '''
    
    optimalNumbers = []
    M = listEncodedRice[0]

    for (num, encodedNum) in listEncodedRice[1::]:
        naturalBinaryNum = rice.calculNaturalBinaryBits(num)
        if (len(encodedNum) < len(naturalBinaryNum)):
            optimalNumbers.append(num)

    return optimalNumbers


if __name__ == '__main__':
    main()