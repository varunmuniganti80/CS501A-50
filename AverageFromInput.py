#CS 175L
#Varun
#AverageFromInput

import sys

def main():
    
        total = 0
        count = 0
        
        file = open("numbers.txt", "r")
        
        for line in file:
            lines = float(line)
            total += lines
            count += 1
            
            print("I read in", count, "number(s) Current number is:", lines, "Total is:", total)
            
        average = total / count

        print("Average:", average)
        
        sys.exit()
        average = total / count
        
        print("Average:", average)
        sys.exit()



if __name__ == '__main__':
    main()
