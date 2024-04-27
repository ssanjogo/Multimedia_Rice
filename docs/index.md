# Multimedia_Rice
## Description
The idea of this code is to do a Rice encoder. 

For the algorithm we need a value M that will be a power of 2 and a value N taht will be the number to codify.
    - We have to calculate the sign of the number N. If the number is positive or 0 we will write the sign as 1, if the number is negative we will write the number as 0. 
    - The second step is to calculate the quotient by dividing the absolute value of the number divided by the number M. 
    - The reminder is the absolut value of the number N mod M. 

So in order to generate the code we have to write the < sign > < quotient > < reminder >.

## Work to develop
a) How many bits are needed to encode all integers between -1023 and +1023 (in natural binary encoding with a sign bit)?

b) Calculate the Rice code for all integers N between -1023 and +1023 with M = 32.

c) For what range of values of N does the Rice code require fewer bits than the natural binary encoding with a sign bit necessary to represent the entire range between -1023 and +1023? If the majority of data to be encoded belongs to this range (optimal input range), the use of Rice code will be advisable (there will be a bit savings). What is the maximum bit savings?

d) For what value of M does the optimal input range extend between -255 and +255? What is the maximum bit savings now?

e) What is the largest value of M that allows achieving a maximum savings of up to 6 bits? What is the optimal input range now?

## Execution of the code
First you have to install the requirements.txt located in the main directory using this code: 

> 
    pip install -r requirements.txt

To run the code you have to go to the folder that contains the main.py, in this case the address of this folder is: MULTIMEDIA_RICE/src/ and in this directory we will find the main.py
The next step is to execute the main.py file using the command:

> 
    python main.py

*Maybe you have to use python3 instead of python. 

## Execution of the documentation
To run the documentation using mk you must do the following, from the root folder:

***Important**: you must install the requirements first*.

> 
    mkdocs build
    

> 
    mkdocs serve

When you run the serve, you will get the web page address on the command line, so you have to open it on your browser. 

## Developed by 
- Oscar Blazquez Jimenez
- Sara San José Gómez