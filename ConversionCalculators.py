# Program that can convert a Hexadecimal to Binary and Binary to Hexadecimal.

def hexToBin():

    cnt = 0

    while ( True and (cnt != 5) ):
        try:        
            hexNum = str(input("Please Enter the hexadecimal you would like to convert to binary: "))
            if hexNum == "exit":
                break
            else:
                binNum = bin(int(hexNum, 16))
                num = binNum
                slcBin = num[2:]
                print(slcBin.zfill(len(hexNum)*4))
        except:
            print("Please print a valid hexadecimal number")
            cnt += 1
        
    print("See you in space cowboy...")  
    return

def binToHex():
    cnt = 0

    while ( True and (cnt != 5) ):
        try:        
            binNum = str(input("Please Enter the binary number you would like to convert to hexadecimal: "))
            if binNum == "exit":
                break
            else:
                hexNum = hex(int(binNum, 2))
                print(hexNum)
        except:
            print("Please print a valid binary number")
            cnt += 1
        
    print("See you in space cowboy...")  
    return

def main():

    print("Number Conversion Calculator\n".center(15), "[1] - Hexadecimal -> Binary\n", "[2] - Binary -> Hexadecimal\n")

    decision = input("Please enter which function you would like to use: ")

    if decision == "1":
        hexToBin()
    elif decision == "2":
        binToHex()
    else:
        print("Have nice day")
        
    return

main()
    
