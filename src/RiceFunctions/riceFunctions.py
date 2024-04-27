import math


def encodeRice(M, num):
    '''
    Method to do the Roce codification. 

    Args:
        - M(int): Integer value, power of 2, necessary to the encode. 
        - num(int): Number that we want to encode. 

    Returns:
        - result(string): binary string with the codification. 
    '''

    result = ""                                                                 # Inicialize the codification of the number with the algorithm Rice as an empty string.

    if (num >= 0):                                                              # Check if the number is bigger or equal to 0. 
        sign = 1                                                                # We establish the sign bit as 1. We consider that 0 is a positive value. 
    else:                                                                       # If the number is smaller than 0, a negative number. 
        sign = 0                                                                # We establish the sign number as 0. 

    quotient = int(abs(num)/M)                                                  # Calculate the quotient. 
    remainder = (abs(num) % M)                                                  # Calculate the remainder. 
    result += str(sign)                                                         # We insert the sign to the result. 

    for _ in range(quotient):                                                   # Iterate in the quotient range.
        result += "1"                                                           # We add as much 1's as the number of the quotient.
    
    result += "0"                                                               # Add a final 0 to the codification of the quotient.
    result += calculNaturalBinaryBits(remainder, int(math.log(M, 2)))           # Add the remainder to the result of the codification.

    return result

def decodeRice(encodedNum, M):
    '''
    Method to decode the encoded number in Rice. 

    Args:
        - encodedNum(int): The number encoded with the Rice algorithm. 
        - M(int): Integer value, power of 2, necessary to the encode. 

    Returns: 
        - finalNumber(int): The number decoded. 
    '''
    quotient = 0                                                                # Count the number of 1's, the quotient. 
    sign = encodedNum[0]                                                        # Read the first bit of the encoded number which is the sign. 

    for i in range(1, len(encodedNum)):                                         # Iterate from the first position to the end of the encoded number.
        if (encodedNum[i] == "1"):                                              # If we read a 1.
            quotient += 1                                                       # We sum 1 to the quotient. 
        else:                                                                   # Otherwise.
            pos = i                                                             # Get the position where the remiander starts.
            break                                                               # Break the loop by changing the value of the zeroFound variable. 
    
    remainder = calculateDecimalNumber(encodedNum[pos::])                       # Get the remainder number and convert it to decimal.
    finalNumber = (quotient * M) + remainder                                    # Calculate the number. 

    if sign == 0:                                                               # Check the value of the sign. 
        finalNumber *= -1                                                       # If the value of the sign is 0, the number is negative. 

    return finalNumber                                                          # Return the final number


def calculNaturalBinaryBits(num, M = -1):
    '''
    Method to calculate the bits needed to represent a number in natural binary.

    Args:
        - num(int): Value to be converted to natural binary. 
        - M(int): Power of 2 value. This will specify the number of bits of the Rice codification for the remainder. 

    Returns:
        - string: natural binary string of the number.    
    '''
    bitsNaturalBinary = ""

    if (num < 0):                                                               # Check if the number is negative.
        num *= -1                                                               # If so, we multiply it by - 1, to converti it to a positive value. 

    binaryNum = bin(num)                                                        # Convert the number to binary. 

    if (M != -1):                                                               # Check if we want to have a specific number of bits
        zerosToAdd = M - len(binaryNum[2:])                                     # Calculate the number of zeros that we have to add.
        for _ in range(zerosToAdd):                                             # Iterate through the zeros.
            bitsNaturalBinary += "0"                                            # Add the zeros to te result.
        bitsNaturalBinary += binaryNum[2:]                                      # Add the codification. 
    else:                                                                       # Otherwise,
        bitsNaturalBinary = binaryNum[2:]                                       # Return the necessary bits for representing the natural binary. 

    return bitsNaturalBinary                                                    # Return the natural binary string of the number.


def calculateDecimalNumber(binaryNum):
    '''
    Method to calculate the decimal number from a natural binary number.

    Args:
        - binaryNum(int): Binary number to convert.

    Returns
        - decimalNum(int): The decimal number, converted from the binary number. 
    '''
    return (int(binaryNum, 2))