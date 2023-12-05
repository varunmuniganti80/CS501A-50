#CS175
#varun sri ram muniganti
#expensePieChart


import matplotlib.pyplot as plt

def main():
    try:
        with open('expenses.txt', 'r') as f:
            data = f.readlines()
            
            expenses = []
            for line in data:
                label, value = line.strip().split('\t')
                try:
                    expenses.append((label, int(value)))
                except ValueError:
                    print("Could not convert data to integer")

            labels = [label for label, value in expenses]
            values = [value for label, value in expenses]
            plt.pie(values, labels=labels)
            plt.title('Monthly Expenses')
            plt.show()

    except IOError:
        print('Error: Could not open file.')
        
if __name__ == '__main__':
    main()


