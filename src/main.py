from RiceFunctions import riceFunctions as rice
import matplotlib.pyplot as plt

def main():
    print("############## A ##############")
    print(rice.calculNaturalBinaryBits(1023, 32))
    print("Bits required to encode in a natural binary, the values from -1023 to 1023:", bitsNeedToCodify(-1023, 1023), "bits.")

    # encodedRice = rice.encodeRice(256, 578)
    # decodedRice = rice.decodeRice(encodedRice, 256)

    # print("Example with M = 256 and N = 578 for encode with Rice algorithm:", encodedRice)
    # print("Example with M = 256 and encodedNumber =", encodedRice, " for decode with Rice algorithm:", decodedRice)

    # encodedRice = rice.encodeRice(32, 32)
    # decodedRice = rice.decodeRice(encodedRice, 32)

    # print("Example with M = 32 and N = 32 for encode with Rice algorithm:", encodedRice)
    # print("Example with M = 32 and encodedNumber =", encodedRice, " for decode with Rice algorithm:", decodedRice)
    
    print("############## B ##############")
    listEncodedRice = calculateRiceEncodedRange(-1023, 1023, 32)
    # print("List of the number from -1023 to 1023 encoded with the algorithm Rice: ")
    # for (num, encodedNum) in listEncodedRice[1::]:
    #     print("Number:", num, "Encoded number:", encodedNum)

    
    print("############## C ##############")
    barPlot([num for (num, encodedNum) in listEncodedRice[1::]], [len(encodedNum) for (num, encodedNum) in listEncodedRice[1::]], len(rice.calculNaturalBinaryBits(1023)), "Number of bits to encode with Rice algorithm", "Number", "Number of bits")

    listOptimal, minimal_value, minimal_encoded_value, maximal_difference= checkBits(listEncodedRice,1023)
    print("List of the numbers that require less bits with the rice codification than with the natural binary codification:", listOptimal)
    print("\n")
    print("We can see how from -128 to 128 the M = 32 works well. However, other values are not working. So if the most part of our values are inside that range, this is a good number")
    print("\n")
    print("Best codification with Rice algorithm is for the number:", minimal_value)
    print("Difference between the natural binary codification and the Rice codification for the number", minimal_value, "is:", maximal_difference, "bits.")
    print("This makes sense since it must always use the residue bits, and in change it does not use any quotient bits. That is why all values below M will always be the best encoded. However, we will not always save bits. This depends on the bits used before encoding and the M used.")
    print("\n")

    print("############## D ##############")
    print("We search between 64, 128 and 256 to see which one is the best for the range -256 to 256. that's because we already know that 32 doesn't work well for more than 128")
    values= [64,128,256]
    best_M = float('inf')
    best_encoded=[]
    for M in values:
        listEncodedRice = calculateRiceEncodedRange(-1023, 1023, M)
        total_length = sum(len(encodedNum) for (num, encodedNum) in listEncodedRice[1::] if -256 <= num <= 256)
        print("[",str(M),"] Total length of encodedNums for numbers between -256 and 256:", total_length)
        if total_length < best_M:
            best_M = total_length
            best_encoded = listEncodedRice

    listOptimal, minimal_value, minimal_encoded_value, maximal_difference= checkBits(best_encoded,1023)      
    print("The best M is:", best_M)
    print("Difference between the natural binary codification and the Rice codification for the number", minimal_value, "is:", maximal_difference, "bits.")
    barPlot([num for (num, encodedNum) in best_encoded[1::]], [len(encodedNum) for (num, encodedNum) in best_encoded[1::]], len(rice.calculNaturalBinaryBits(1023)), "Number of bits to encode with Rice algorithm", "Number", "Number of bits")


    print("\n")
    print("############## E ##############")
    best_encoded = []
    for M in [2**i for i in range(1,11)]:
        if M > 1023:
            break
        listEncodedRice = calculateRiceEncodedRange(-1023, 1023, M)
        _, minimal_value, _, maximal_difference = checkBits(listEncodedRice, 1023)
        print("For M =", M, "the maximal difference is:", maximal_difference, "bits.", "Minimal value:", minimal_value)
        if maximal_difference == 6:
            best_M = M
            best_encoded = listEncodedRice

    print("The best M for the E which has a maximal difference of 6 is:", best_M)
    barPlot([num for (num, encodedNum) in best_encoded[1::]], [len(encodedNum) for (num, encodedNum) in best_encoded[1::]], len(rice.calculNaturalBinaryBits(1023)), "Number of bits to encode with Rice algorithm", "Number", "Number of bits")
    print("As we can see, the optimal input range is [-64,64]")


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
        nBits = len(rice.calculNaturalBinaryBits(fNum))          # If the first number is bigger we calculate the number of bits of the value + 1 (the sign + or -)
    else:                                                           # Check if the absolute value of the second number is smaller than the first one. 
        nBits = len(rice.calculNaturalBinaryBits(sNum))        # Calculate the number of bits of the second number + 1 (the sign + or -)
    
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

def checkBits(listEncodedRice, max_number=0):
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
   

    minimal_value= float('inf')
    minimal_enoded_value = listEncodedRice[1][1]
    maximal_difference =  0
    prev_len=len(rice.calculNaturalBinaryBits(max_number))

    for (num, encodedNum) in listEncodedRice[1::]:
        if (len(encodedNum) < prev_len):
            optimalNumbers.append(num)
            if prev_len-len(encodedNum) > maximal_difference:
                minimal_value = num
                minimal_enoded_value = encodedNum
                maximal_difference = prev_len-len(minimal_enoded_value)

    return optimalNumbers,minimal_value, minimal_enoded_value, maximal_difference


def barPlot(x,y, base,title, xLabel, yLabel):
    '''
    Method to create a bar plot. 

    Args:
        - x(list): List with the values of the x axis.
        - y(list): List with the values of the y axis. 
        - base(number): Represents the normal codification of the numbers.
        - title(string): Title of the plot.
        - xLabel(string): Label of the x axis.
        - yLabel(string): Label of the y axis.
    '''

    # Create bar plot
    plt.bar(x, y)

    # Add vertical line at y=100
    plt.axhline(y=base, color='r', linestyle='--')

    # Add labels and title
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)

    # Show plot
    plt.show()

if __name__ == '__main__':
    main()