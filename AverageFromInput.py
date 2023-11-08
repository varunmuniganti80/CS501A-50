#CS 175L
#Varun
#Average From Input File with Exception Handling

import sys

def main():
    try:
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
        
    except ValueError:
        print('Non-numeric data found in the file.Skipping..')
        
    except IOError:
        print('An error occurred trying to open the file.')
        
        sys.exit()
        average = total / count
        
        print("Average:", average)
        sys.exit()



if __name__ == '__main__':
    main()
