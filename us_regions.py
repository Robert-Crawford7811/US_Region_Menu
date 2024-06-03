'''Module that plots a histogram of the population of the regions in the United States'''
import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv("PopChange.csv")
housing = pd.read_csv("Housing.csv")

def histogram(data, column_name):
    '''Function that plots histogram analysis'''
    chosen_column = data[column_name]
    #Calculate Statistics
    count = chosen_column.count()
    mean = chosen_column.mean()
    std = chosen_column.std()
    minimum = chosen_column.min()
    maximum = chosen_column.max()
    #Creates Histogram Plot
    chosen_column.plot.hist(bins=10, edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title('Analysis: '+ column_name)
    plt.show()
    #Prints the statistics
    print("Statistics for column", column_name)
    print("Count: ", count)
    print("Mean: ", mean)
    print("Std. Deviation: ", std)
    print("Min: ", minimum)
    print("Max: ", maximum)
def population_data():
    '''Function that allows the user to analyze the population'''
    # Greets and presents user with options
    print("Select the column you want to analyze")
    print("1. Pop Apr 1")
    print("2. Pop Jul 1")
    print("3. Change Pop")
    print("4. Exit Column")

    # Sets condition of menu system
    column_choice = 0
    # Prompt user for choice
    while column_choice != 4:
        column_choice = int(input("Select the column you want to analyze: "))
        if column_choice == 1:
            print("Apr 1")
            histogram(population, "Pop Apr 1")
        elif column_choice == 2:
            print("Jul 1")
            histogram(population, "Pop Jul 1")
        elif column_choice == 3:
            print("Change pop")
            histogram(population, "Change Pop1")
        elif column_choice == 4:
            print("Exiting Columns")
            break
        else:
            print("Invalid Choice")

def housing_data():
    '''Function that allows the user to analyze the population'''
    #Greets and presents user with options
    print("Select the column you want to analyze")
    print("1. AGE")
    print("2. BEDRMS")
    print("3. BUILT")
    print("4. ROOMS")
    print("5. UTILITY")
    print("6. Exit Column")

    #Sets condition of menu system
    column_choice = 0
    #Prompt user for choice
    while column_choice !=6:
        column_choice = int(input("Select the column you want to analyze: "))
        if column_choice == 1:
            print("Age")
            histogram(housing, "AGE")
        elif column_choice== 2:
            print("Bedrooms")
            histogram(housing, "BEDRMS")
        elif column_choice == 3:
            print("Built")
            histogram(housing, "BUILT")
        elif column_choice == 4:
            print("Rooms")
            histogram(housing, "ROOMS")
        elif column_choice == 5:
            print("Utility")
            histogram(housing, "UTILITY")
        elif column_choice == 6:
            print("Exiting Columns")
            break
        else:
            print("Invalid Choice")

def main():
    '''Function that calls the main function'''
    #Greets and presents the user options
    print("Welcome to the Python Analysis App")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")

    #Prompt user for a decision
    user_choice = 0
    #Sets condition to exit the program
    while user_choice!=3:
        user_choice = int(input("Select the file you want to analyze: "))
        #What happens if user chooses to analyze population data
        if user_choice == 1:
            print("You have entered population data")
            #Call function to analyze population data
            population_data()
        elif user_choice == 2:
            print("You have entered housing data")
            #Call function to analyze housing data
            housing_data()
        elif user_choice == 3:
            #Thank you message for using the program
            print("Thank You for using the program")
            break
        else:
            #Informs the user that their choice was invalid
            print("Invalid Choice")

if __name__ == '__main__':
    main()
