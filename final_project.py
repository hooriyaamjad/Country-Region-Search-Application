# ENDG 233 Final Project
# Hooriya Amjad (30131172)
# Country/Region database. 
# User inputs a country or region and code outputs country, population, or species data based on user selection.


import numpy as np
import matplotlib.pyplot as plt

class AvgYearPopRegSubreg:
    '''A class used to print the average population of a sub region or region during a certain year object.

        Attributes:
            reg_or_subreg (str): String that represents region or sub region
            year (str): String that represents the inputted year by user
            avg_pop (int): Integer that represents the average population of region or sub region
            during inputted year
    '''

    def __init__(self, reg_or_subreg, year, avg_pop):              
        self.reg_or_subreg = reg_or_subreg
        self.year = year
        self.avg_pop = avg_pop

    def print_avg_reg_or_subreg_pop(self):
        '''A function that prints the average pop for region or sub region in year

        Parameters: None
        Returns: None

        '''
        print(f'The average population in {self.reg_or_subreg} for the year {self.year[:4]} was {self.avg_pop}\n')


#---------- FUNCTIONS FOR COUNTRY

def ctry_func(ctry_or_region, country_2, country_3, ctry_list, reg_list, subreg_list, sqkm_list, pop_data):             # function is created and defined by the name 'ctry_function'
    '''A function that prints country information and average people per sqkm for first inputted country, and
        prints most densely populated country from the 3 inputted countries along with its average people per sq km

        Parameters: ctry_or_region(country input), country_2, country_3, ctry_list, reg_list, subreg_list, sqkm_list, pop_data
        Returns: none

        '''
    
    input_index_1 = ctry_list.index(ctry_or_region)                             # 'input_index_1' is defined by the index of user's input for 'ctry_or_region' in the list of countries (ctry_list)
    input_index_2 = ctry_list.index(country_2)                                  # 'input_index_2' is defined by the index of user's input for 'country_2' in the list of countries (ctry_list)
    input_index_3 = ctry_list.index(country_3)                                  # 'input_index_3' is defined by the index of user's input for 'country_3' in the list of countries (ctry_list)

    un_region = reg_list[input_index_1]                                         # 'un_region' is defined by the value from a 'input_index_1''s position in the region list (reg_list)
    un_sub_reg = subreg_list[input_index_1]                                     # 'un_sub_reg is defined by the value from 'input_index_1''s position in the subregion list (subreg_list)
    
    sqkm_1 = sqkm_list[input_index_1]                                           # 'sqkm_1' is defined by the value in the position of 'input_index_1' in the list of square kilometres (sqkm_list)
    sqkm_2 = sqkm_list[input_index_2]                                           # 'sqkm_2' is defined by the value in the position of 'input_index_2' in the list of square kilometres (sqkm_list)
    sqkm_3 = sqkm_list[input_index_3]                                           # 'sqkm_3' is defined by the value in the position of 'input_index_3' in the list of square kilometres (sqkm_list)

    int_sqkm_1 = sqkm_1.astype(int)                                             # 'int_sqkm_1' is defined by the integer value of 'sqkm_1'
    int_sqkm_2 = sqkm_2.astype(int)                                             # 'int_sqkm_2' is defined by the integer value of 'sqkm_2'
    int_sqkm_3 = sqkm_3.astype(int)                                             # 'int_sqkm_3' is defined by the integer value of 'sqkm_3'

    pop_1 = list(pop_data[input_index_1])                                       # 'pop_1' is a list of the value of the position 'input_index_1' in the dataset 'pop_data'
    pop_2 = list(pop_data[input_index_2])                                       # 'pop_2' is a list of the value of the position 'input_index_2' in the dataset 'pop_data'
    pop_3 = list(pop_data[input_index_3])                                       # 'pop_3' is a list of the value of the position 'input_index_3' in the dataset 'pop_data'

    del pop_1[0]                                                                # deletes the first value of 'pop_1'
    del pop_2[0]                                                                # deletes the first value of 'pop_2'
    del pop_3[0]                                                                # deletes the first value of 'pop_3'

    int_pop_1 = [int(i) for i in pop_1]                                         # 'int_pop_1' is defined by the integer values from 'pop_1'
    int_pop_2 = [int(i) for i in pop_2]                                         # 'int_pop_2' is defined by the integer values from 'pop_2'
    int_pop_3 = [int(i) for i in pop_3]                                         # 'int_pop_3' is defined by the integer values from 'pop_3'

    avg_pop_1 = (sum(int_pop_1)) // 21                                            # 'avg_pop_1' is defined by the sum of all the populations across 2000 - 2020 for the user's first inputted country divided by total years (21)
    avg_pop_2 = (sum(int_pop_2)) // 21                                            # 'avg_pop_2' is defined by the sum of all the populations across 2000 - 2020 for the user's second inputted country divided by total years (21)
    avg_pop_3 = (sum(int_pop_3)) // 21                                            # 'avg_pop_3' is defined by the sum of all the populations across 2000 - 2020 for the user's third inputted country divided by total years (21)

    ppl_per_sqkm_1 = avg_pop_1 / int_sqkm_1                                     # 'ppl_per_sqkm_1' is defined by the total average population across 2000 - 2020 (avg_pop_1) divided by the square kilometres of the inputted country
    ppl_per_sqkm_2 = avg_pop_2 / int_sqkm_2                                     # 'ppl_per_sqkm_2' is defined by the total average population across 2000 - 2020 (avg_pop_2) divided by the square kilometres of the inputted country
    ppl_per_sqkm_3 = avg_pop_3 / int_sqkm_3                                     # 'ppl_per_sqkm_3' is defined by the total average population across 2000 - 2020 (avg_pop_3) divided by the square kilometres of the inputted country

    print(f'\n{ctry_or_region} is in the sub region of {un_sub_reg} which is located in {un_region}')                           # prints the first inputted country, it's subregion, and it's region
    print(f'{ctry_or_region} is {sqkm_1} square kilometres in area')                                                            # prints the first inputted country and it's area in square kilometres 
    print('~')                                                                                                                  # prints '~' for formatting purposes

    print(f'{ctry_or_region} has an average of {ppl_per_sqkm_1:.2f} people per square kilometre')                               # prints the first inputted country and it's people per square kiloemtre to two decimal places

    if ppl_per_sqkm_1 > ppl_per_sqkm_2 and ppl_per_sqkm_1 > ppl_per_sqkm_3:                                                     # if the ppl per sqkm of the first country is greater than that of the second and third countries, the branch will execute
        print(f'{ctry_or_region} is the most densely populated of all the countries')                                           # prints that the first inputted country is the most densely populated of all inputted countries
    
    elif ppl_per_sqkm_2 > ppl_per_sqkm_1 and ppl_per_sqkm_2 > ppl_per_sqkm_3:                                                                                               # if the ppl per sqkm of the second country is greater than that of the first and third countries, the branch will execute
        print(f'{country_2} is the most densely populated of all the countries\n{country_2} has an average of {ppl_per_sqkm_2:.2f} people per square kilometre')            # prints that the second inputted country is the most densely populated of all inputted countries and prints the average ppl per sqkm to two decimal places

    elif ppl_per_sqkm_3 > ppl_per_sqkm_1 and ppl_per_sqkm_3 > ppl_per_sqkm_2:                                                                                               # if the ppl per sqkm of the third country is greater than that of the first and second countries, the branch will execute
        print(f'{country_3} is the most densely populated of all the countries\n{country_3} has an average of {ppl_per_sqkm_3:.2f} people per square kilometre')            # prints that the third inputted country is the most densely populated of all inputted countries and prints the average ppl per sqkm to two decimal places

def pop_func(ctry_or_region, country_2, country_3, pop_year_input, pop_data, ctry_list, year_list):                               # function is created and is defined by the name 'pop_func'
    '''A function that prints average population of the country with highest population in the inputted year, 
        the population difference between the first inputted country and the second inputted country,
        the population difference between the first inputted country and the third inputted country, and
        the average population of the first inputted countrys from 2000 - 2020
    
        Parameters: ctry_or_region(country input), country_2, country_3, pop_year_input, pop_data, ctry_list, year_list
        Returns: none

        '''
    col_index = year_list.index(pop_year_input)                                               # 'col_index' is defined by the index of 'pop_year_input' in the list of years 2000 - 2020 (year_list)

    ctry_1 = ctry_list.index(ctry_or_region)                                                  # 'ctry_1' is defined by the index of the user's first inputted country (ctry_or_region) in the list of countries (ctry_list)
    ctry_2 = ctry_list.index(country_2)                                                       # 'ctry_2' is defined by the index of the user's second inputted country (ctry_or_region) in the list of countries (ctry_list)
    ctry_3 = ctry_list.index(country_3)                                                       # 'ctry_3' is defined by the index of the user's last inputted country (ctry_or_region) in the list of countries (ctry_list)

    pop_ctry_1 = (pop_data[ctry_1, col_index]).astype(int)                                    # 'pop_ctry_1' is defined by the integer value of the row index of 'ctry_1' and the column index of 'col_index' 
    pop_ctry_2 = (pop_data[ctry_2, col_index]).astype(int)                                    # 'pop_ctry_2' is defined by the integer value of the row index of 'ctry_2' and the column index of 'col_index' 
    pop_ctry_3 = (pop_data[ctry_3, col_index]).astype(int)                                    # 'pop_ctry_3' is defined by the integer value of the row index of 'ctry_3' and the column index of 'col_index' 

    if pop_ctry_1 > pop_ctry_2 and pop_ctry_1 > pop_ctry_3:                                   # if the population of the first country is greater than that of the second and third countries then the branch will execute
        max_ctry = ctry_or_region                                                             # 'max_ctry' is equal to the user's input of the first country 'ctry_or_region'
        max_pop = pop_ctry_1                                                                  # 'max_pop' is equal to the value of the first inputted country's population (pop_ctry_1)
    elif pop_ctry_2 > pop_ctry_1 and pop_ctry_2 > pop_ctry_3:                                 # else if the population of the second country is greater than that of the first and third countries then the branch will execute
        max_ctry = country_2                                                                  # 'max_ctry' is equal to the user's input of the second country 'country_2'
        max_pop = pop_ctry_2                                                                  # 'max_pop' is equal to the value of the second inputted country's population (pop_ctry_2)
    elif pop_ctry_3 > pop_ctry_1 and pop_ctry_3 > pop_ctry_2:                                 # else if the population of the third country is greater than that of the first and second countries then the branch will execute
        max_ctry = country_3                                                                  # 'max_ctry' is equal to the user's input of the third country 'country_3'
        max_pop = pop_ctry_3                                                                  # 'max_pop' is equal to the value of the third inputted country's population (pop_ctry_3)


    input_index_1 = ctry_list.index(ctry_or_region)                                           # 'input_index_1' is equal to the index position of 'ctry_or_region' in the list 'ctry_list'
    input_index_2 = ctry_list.index(country_2)                                                # 'input_index_2' is equal to the index position of 'country_2' in the list 'ctry_list'
    input_index_3 = ctry_list.index(country_3)                                                # 'input_index_3' is equal to the index position of 'country_3' in the list 'ctry_list'

    pop_array = (pop_data[input_index_1,:])                                                   # 'pop_array' is an array defined by the row index 'input_index_1' to the end of available columns
    pop_array = np.delete(pop_array, 0)                                                       # deletes the value in the array with the row value 'pop_array' in column position [0] and reassigns the array to 'pop_array'
    pop_array = pop_array.astype(int)                                                         # all the values in the array 'pop_array' are converted to integers
    
    max = np.max(pop_array)                                                                   # 'max' is defined by the highest value in 'pop_array'
    min = np.min(pop_array)                                                                   # 'min' is defined by the lowest value in 'pop_array'
    
    pop_1 = list(pop_data[input_index_1])                                                     # 'pop_1' is a list defined by the value of the index 'input_index_1' in the dataset 'pop_data'
    pop_2 = list(pop_data[input_index_2])                                                     # 'pop_2' is a list defined by the value of the index 'input_index_2' in the dataset 'pop_data'
    pop_3 = list(pop_data[input_index_3])                                                     # 'pop_3' is a list defined by the value of the index 'input_index_3' in the dataset 'pop_data'

    del pop_1[0]                                                                              # deletes the first value of 'pop_1'
    del pop_2[0]                                                                              # deletes the first value of 'pop_2'
    del pop_3[0]                                                                              # deletes the first value of 'pop_3'
    
    int_pop_1 = [int(i) for i in pop_1]                                                       # 'int_pop_1' is defined by the integer values of 'pop_1'
    int_pop_2 = [int(i) for i in pop_2]                                                       # 'int_pop_2' is defined by the integer values of 'pop_2'
    int_pop_3 = [int(i) for i in pop_3]                                                       # 'int_pop_3' is defined by the integer values of 'pop_3'

    avg_pop_1 = (sum(int_pop_1))//21                                                          # 'avg_pop_1' is the sum of all the values in 'int_pop_1' divided by the total number of years from 2000 - 2020, (21)
    avg_pop_2 = (sum(int_pop_2))//21                                                          # 'avg_pop_2' is the sum of all the values in 'int_pop_2' divided by the total number of years from 2000 - 2020, (21)
    avg_pop_3 = (sum(int_pop_3))//21                                                          # 'avg_pop_3' is the sum of all the values in 'int_pop_3' divided by the total number of years from 2000 - 2020, (21)

    pop_diff_1 = (avg_pop_1 - avg_pop_2)                                                      # 'pop_diff_1' is defined by the difference of 'avg_pop_1' and 'avg_pop_2' (first and second country)
    pop_diff_2 = (avg_pop_1 - avg_pop_3)                                                      # 'pop_diff_2' is defined by the difference of 'avg_pop_1' and 'avg_pop_3' (first and third country)
    
    if pop_diff_1 > 0:                                                                        # if 'pop_diff_1' is greater than 0
        symbol_1 = 'more people than'                                                         # 'symbol_1' is equal to the string 'more people than'
    else:                                                                                     # else 'pop_diff_1' is smaller than 0
        pop_diff_1 = str(pop_diff_1)                                                          # 'pop_diff_1' is converted to a string
        pop_diff_1 = pop_diff_1[1:]                                                           # the first value of 'pop_diff_1' is sliced and the rest of the string remains
        symbol_1 = 'less people than'                                                         # 'symbol_1' is equal to the string 'less people than'

    if pop_diff_2 > 0:                                                                        # if 'pop_diff_2' is greater than 0
        symbol_2 = 'more people than'                                                         # 'symbol_2' is equal to the string 'more people than'
    else:                                                                                     # else 'pop_diff_2' is smaller than 0
        pop_diff_2 = str(pop_diff_2)                                                          # 'pop_diff_1' is converted to a string
        pop_diff_2 = str(pop_diff_2[1:])                                                      # the first value of 'pop_diff_2' is sliced and the rest of the string remains
        symbol_2 = 'less people than'
    
    pop_in_year = pop_data[input_index_1, col_index]
    
    print(f'\nIn the year {pop_year_input[:4]}, {ctry_or_region} had a population of {pop_in_year}')
    print(f'{max_ctry} had the highest population with {max_pop} people')                                                     # prints 'In the year' {user's inputted year} {country name with the highest population in that year} and the country's population
    print('~')                                                                                                                # prints '~'
    print(f'{ctry_or_region} has {pop_diff_1} {symbol_1} {country_2} on avg.')                                                # prints the first inputted country and the difference in population between the second inputted country on average from 2000 - 2020
    print(f'{ctry_or_region} has {pop_diff_2} {symbol_2} {country_3} on avg.')                                                # prints the first inputted country and the difference in population between the third inputted country on average from 2000 - 2020
    print(f'{ctry_or_region} has a max and min population of {max} and {min}')                                                # prints the first inputted country's maximum and minimum populations from 2000 - 2020
    print('~')                                                                                                                # prints '~'
    print(f'The avg. population of {ctry_or_region} from (2000 - 2020) was {avg_pop_1}')                                      # prints a new line and the average population of the first inputted country from 2000 - 2020

def threatened_spec(ctry_or_region, country_2, country_3, ctry_list, plant_list, fish_list, bird_list, mammal_list):          # creates a new function defined by the name 'threatened_spec'
    '''A function that prints species data for first inputted country, prints average species per class for first
        inputted country, print country with max endangered species and print total sum of countrys endangered species, 
        print country with min endangered species and print total sum of countrys endangered species, prints average 
        total sum between the 3 inputted countries

        Parameters: ctry_or_region(country input), country_2, country_3, ctry_list, plant_list, fish_list, bird_list, mammal_list
        Returns: none

        '''

    input_index = ctry_list.index(ctry_or_region)                                             # 'input_index' is an index defined by the value of the first inputted country in the list 'ctry_list'
    index_2 = ctry_list.index(country_2)                                                      # 'index_2' is an index defined by the value of the second inputted country in the list 'ctry_list'
    index_3 = ctry_list.index(country_3)                                                      # 'index_3' is an index defined by the value of the third inputted country in the list 'ctry_list'
    
    plant = int(plant_list[input_index])                                                      # 'plant' is an integer value defined by 'input_index' in the list 'plant_list'
    fish = int(fish_list[input_index])                                                        # 'fish' is an integer value defined by 'input_index' in the list 'fish_list'
    bird = int(bird_list[input_index])                                                        # 'bird' is an integer value defined by 'input_index' in the list 'bird_list'
    mammal = int(mammal_list[input_index])                                                    # 'mammal' is an integer value defined by 'input_index' in the list 'mammal_list'
    species_avg = int((plant + fish + bird + mammal) / 4)                                     # 'species_avg' is an integer defined by the sum of all 4 values of 'plant', 'fish', 'bird', and 'mammal' divided by 4

    species_tot_1 = int((int(plant_list[input_index]) + int(fish_list[input_index]) + int(bird_list[input_index]) + int(mammal_list[input_index])))              # 'species_tot_1' is an integer defined by the sum of each species class for the first inputted country            
    species_tot_2 = int((int(plant_list[index_2]) + int(fish_list[index_2]) + int(bird_list[index_2]) + int(mammal_list[index_2])))                              # 'species_tot_2' is an integer defined by the sum of each species class for the second inputted country
    species_tot_3 = int((int(plant_list[index_3]) + int(fish_list[index_3]) + int(bird_list[index_3]) + int(mammal_list[index_3])))                              # 'species_tot_3' is an integer defined by the sum of each species class for the third inputted country
    
    species_tot_list = [species_tot_1, species_tot_2, species_tot_3]                          # 'species_tot_list' is a list of each species total from each of the inputted countries
    species_tot_arr = np.array(species_tot_list)                                              # 'species_tot_arr' is an array of the values from 'species_tot_list' 
    species_tot_max = np.max(species_tot_arr)                                                 # 'species_tot_max' is defined by the highest value in 'species_tot_arr' 
    species_tot_min = np.min(species_tot_arr)                                                 # 'species_tot_min' is defined by the lowest value in 'species_tot_arr' 
    
    species_per_class_1 = int(species_tot_1 / 4)                                              # 'species_per_class_1' is the species per class for the first inputted country and is an integer defined by 'species_tot_1' divided by 4
    species_per_class_2 = int(species_tot_2 / 4)                                              # 'species_per_class_2' is the species per class for the second inputted country and is an integer defined by 'species_tot_2' divided by 4
    species_per_class_3 = int(species_tot_3 / 4)                                              # 'species_per_class_3' is the species per class for the third inputted country and is an integer defined by 'species_tot_3' divided by 4
    
    
    if species_tot_1 == species_tot_max:                                                      # if 'species_tot_1' is equal to 'species_tot_max' the branch will execute
        ctry_max = ctry_or_region                                                             # 'ctry_max' is equal to the first inputted country (ctry_or_region)
    elif species_tot_2 == species_tot_max:                                                    # else if 'species_tot_2' is equal to 'species_tot_max' the branch will execute
        ctry_max = country_2                                                                  # 'ctry_max' is equal to the second inputted country (country_2)
    elif species_tot_3 == species_tot_max:                                                    # else if 'species_tot_3' is equal to 'species_tot_max' the branch will execute
        ctry_max = country_3                                                                  # 'ctry_max' is equal to the third inputted country (country_3)
    
    if species_tot_1 == species_tot_min:                                                      # if 'species_tot_1' is equal to 'species_tot_min' the branch will execute
        ctry_min = ctry_or_region                                                             # 'ctry_min' is equal to the first inputted country (ctry_or_region)
    elif species_tot_2 == species_tot_min:                                                    # else if 'species_tot_2' is equal to 'species_tot_min' the branch will execute
        ctry_min = country_2                                                                  # 'ctry_min' is equal to the second inputted country (country_2)
    elif species_tot_3 == species_tot_min:                                                    # else if 'species_tot_3' is equal to 'species_tot_min' the branch will execute
        ctry_min = country_3                                                                  # 'ctry_min' is equal to the third inputted country (country_3)

    species_class_avg = int((species_per_class_1 + species_per_class_2 + species_per_class_2) / 3)                                          # 'species_class_avg' is defined by the sum of each country's endangered species per class divided by 3
    
    print(f'\n{ctry_or_region} has the following endangered species data:')                                                                 # prints a new line and the first inputted country 'has the following endangered species data'
    print('~')                                                                                                                              # prints '~'
    print(f'Plant species: {plant}\nFish species: {fish}\nBird species: {bird}\nMammals: {mammal}')                                         # prints each species class and their values for the first inputted country
    print(f'\n{ctry_or_region} has {species_avg} endangered species per class on average')                                                  # prints a new line, the first inputted country, and the species                   
    print('~')                                                                                                                              # prints '~'
    print(f'{ctry_max} has the highest amount of endangered species - {species_tot_max} species are endangered')                            # prints the country name with the highest total endangered species and prints it's total endangered species 
    print(f'{ctry_min} has the lowest amount of endangered species - {species_tot_min} species are endangered')                             # prints the country name with the lowest total endangered species and prints it's total endangered species 
    print(f'{ctry_or_region}, {country_2}, and {country_3} have {species_class_avg} endangered species per class on average')               # prints the first, second, and third inputted countries and the mean value of their species per class
    
    
    plt.figure(1)                                                                                                               # creates a figure (1) with the matplotlib.pyplot module

    plt.subplot(2,1,1)                                                                                                          # subplot is created at position (2,1,1) in the figure
    
    plt.plot(ctry_or_region, species_tot_1, 'yo', label = (f'{ctry_or_region}\'s Total Endangered Species'))                    # plot is created and has the x value 'ctry_or_region' and the y value 'species_tot_1'. The colour of the line is yellow and the line type is dot. Subplot is labelled '(first inputted country)\'s Total Endangered Species'
    plt.plot(country_2, species_tot_2, 'co', label = (f'{country_2}\'s Total Endangered Species'))                              # plot is created and has the x value 'country_2' and the y value 'species_tot_2'. The colour of the line is cyan and the line type is dot. Subplot is labelled '(second inputted country)\'s Total Endangered Species'
    plt.plot(country_3, species_tot_3, 'mo', label = (f'{country_3}\'s Total Endangered Species'))                              # plot is created and has the x value 'country_3' and the y value 'species_tot_3'. The colour of the line is magenta and the line type is dot. Subplot is labelled '(third inputted country)\'s Total Endangered Species'
    
    plt.title('Relationships of Endangered Species between different Countries')                                                # subplot is titled 'Relationships of Endangered Species between different Countries'
    plt.ylabel('Number of Endangered Species')                                                                                  # the subplot's y axis is labelled 'Number of Endangered Species'
    plt.legend(shadow = True)                                                                                                   # the subplot's legend is created and has a shadow. Labels depend on inputted countries
    
    plt.subplot(2,1,2)                                                                                                          # subplot is created at position (2,1,2) in the figure

    plt.plot(ctry_or_region, species_per_class_1, 'yo', label = (f'{ctry_or_region}\'s Avg. Endangered Species/Class'))         # plot is created and has the x value 'ctry_or_region' and the y value 'species_per_class_1'. The colour of the line is yellow and the line type is dot. Subplot is labelled '(first inputted country)\'s Avg. Endangered Species/Class'
    plt.plot(country_2, species_per_class_2, 'co', label = (f'{country_2}\'s Avg. Endangered Species/Class'))                   # plot is created and has the x value 'country_2' and the y value 'species_per_class_2'. The colour of the line is cyan and the line type is dot. Subplot is labelled '(second inputted country)\'s Avg. Endangered Species/Class'
    plt.plot(country_3, species_per_class_3, 'mo', label = (f'{country_3}\'s Avg. Endangered Species/Class'))                   # plot is created and has the x value 'country_3' and the y value 'species_per_class_3'. The colour of the line is magenta and the line type is dot. Subplot is labelled '(third inputted country)\'s Avg. Endangered Species/Class'

    plt.xlabel('Country')                                                                                                       # subplot's x axis is labelled 'Country'
    plt.ylabel('Number of Endangered Species per Class')                                                                        # subplot's y axis is labelled 'Number of Endangered Species per Class'
    plt.legend(shadow = True)                                                                                                   # the subplot's legend is created and has a shadow. Labels depend on inputted countries

    plt.gcf().set_size_inches(10, 7)                                                                                            # the plot's size is set to 10 inches length (x axis) and 7 inches height (y_axis)
    plt.show()                                                                                                                  # presents figure (1) to the user which varies on the user's input for all three countries
    
    
#--------- FUNCTIONS FOR REGION

def year_avg_pop_reg_or_subreg(reg_or_subreg_ctrys, pop_data, year_list, year) -> int:                                                # function is created and defined by the name 'year_avg_pop_reg_or_subreg'
    '''A function that returns the average population of a region or sub region during a specified year

        Parameters: reg_or_subreg_ctrys(countries in region or subregion), pop_data, year_list, year
        Return: average population of region

        '''
    avg = 0 
    year_index = 0
                                        
    for i in range(len(year_list)):                       # find the index of the year in pop_data using year_list
        if year_list[i] == year:
            year_index = i

    for i in reg_or_subreg_ctrys:                         # for countries i in the reg_or_subreg_ctrys list
        for j in pop_data:                                # for population data j in pop_data
            if j[0] == i:                                 # if j[0] which is the country column, equals i
                avg = avg + int(j[year_index])            # add the population of the country to the average
    return avg // len(reg_or_subreg_ctrys)                # return the average by dividing the total sum by the total number of countries in the reg_or_subreg_ctrys list

def avg_pop_ctry(ctry_list, user_input_ctry, pop_data):
    '''A function that prints the average population of a country from 2000-2020

        Parameters: ctry_list, user_input_ctry, pop_data
        Return: none

        '''
    ctry_index = ctry_list.index(user_input_ctry)               # get country index of users inputted country               
    pop_ctry = list(pop_data[ctry_index])                       # get country populations from 2000-2020 for specified country
    del pop_ctry[0]                                             # del country name from pop_ctry list
    int_pop = [int(i) for i in pop_ctry]                        # make all list items into integers
    average_pop = (sum(int_pop)) // 21                          # calculate average population for country from 2000-2020
    
    print(f'The average population from 2000 - 2020 for {user_input_ctry} is {average_pop}')       # print average population of country

def all_years_pop_avg(year_list, reg_or_subreg_ctrys, pop_data):
    '''A function that returns a list of all yearly population averages within a region or sub region

        Parameters: year_list, reg_or_subreg_ctrys(countries in region or sub region), pop_data
        Return: years_pop_avgs (list)

        '''
    years_pop_avgs = []                                                 # yearly average population data list
    year_pop_avg = 0
    year_index = 0

    for year_index in range(1, len(year_list)):                         # for every year
        for i in reg_or_subreg_ctrys:                                   # for every country in the region or subregion
            for j in pop_data:                                          # for every row of pop_data
                if j[0] == i:                                           # if 0th index is country in the region or subregion
                    year_pop_avg = year_pop_avg + int(j[year_index])    # add pop_data for the year to year_pop_avg
        year_pop_avg = year_pop_avg // len(reg_or_subreg_ctrys)         # get the average of that year by dividing by total number of countries
        years_pop_avgs.append(year_pop_avg)                             # add to list
        year_pop_avg = 0                                                # reset year_pop_avg to 0
    return years_pop_avgs                                               # return years_pop_avgs list

def region_graph(year_list, ctry_or_region, reg_yearly_avg_pop):
    '''A function that shows a graph of all yearly population averages within a region

        Parameters: year_list, ctry_or_region(region input), reg_years_avg_pop(average populations for all years for a region)
        Return: years_pop_avgs (list)

        '''
    del year_list[0]                                                            # remove index 0 from year list
    x = (year_list)
    x_axis = range(len(x))
    reg_plot = np.array(reg_yearly_avg_pop)                                     # average populations for a region in each year numpy array

    plt.xticks(np.arange(21), ('2000', '', '', '', '', '2005', '', '', '', '', '2010', '', '', '', '', '2015', '', '', '', '', '2020'))     # plot x axis points
    plt.plot(x_axis, reg_plot, '--', color = 'darkblue', label = (f'Population Change in {ctry_or_region}'))                                # plot yearly average populations on region graph
    plt.title(f'Average Population Change of {ctry_or_region} from 2000 to 2020')       # region graph title
    plt.xlabel('Years')                                                                 # region graph x axis label              
    plt.ylabel(f'Population Average x 10^6')                                                   # region graph y axis label
    plt.legend(shadow = True)
    plt.gcf().set_size_inches(10, 6)                                                    # set graph size
    plt.show()                                                                          # show plot
 

#---------- MAIN FUNCTION


def main():

    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', encoding = None, dtype = None)                # numpy array for country data
    pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', encoding = None, dtype = None)                 # numpy array for ppopulation data
    species_data = np.genfromtxt('Threatened_Species.csv', delimiter = ',', encoding = None, dtype = None)          # numpy array for threatened species data

    # LISTS MADE FROM CSV DATA
    ctry_list = list(country_data[:,0]) 
    reg_list = list(country_data[:,1])
    subreg_list = list(country_data[:,2])
    sqkm_list = list(country_data[:,3])
    year_list = list(pop_data[0,:])

    plant_list = list(species_data[:,1])
    fish_list = list(species_data[:,2])
    bird_list = list(species_data[:,3])
    mammal_list = list(species_data[:,4])

    print('\nWelcome to the Country/Region information database!\nYou can search information for your desired Countries or Regions below.') 
    ctry_or_region = input('\nPlease input a Country or Region (input style: Capital Words): ')        # prompt user for either country or region
    
    while ctry_or_region not in ctry_list[1:196] and ctry_or_region not in reg_list[1:196]:            # while user does not enter an input in either ctry_list or reg_list
        print('Invalid Country or Region.\n')                                                
        ctry_or_region = input('Please input a Country or Region (input style: Capital Words): ')      # prompt user for valid country or region
    
#---------- CHOICE 1: COUNTRY

    if ctry_or_region in ctry_list[1:196]:                                          # if user input is a country

        country_2 = input('Input a second country: ')                               # prompt user for second country

        while not country_2 in ctry_list or country_2 == ctry_or_region:            # while user does not enter a country in ctry_list or 'country_2' is equal to ctry_or_region
            print('Please input a valid country\n')                                 # prompt user for valid country
            country_2 = input('Input a second country: ')                           
                                                                                    
        country_3 = input('Input a third country: ')                                # prompt user for third country 
            
        while not country_3 in ctry_list or country_3 == country_2 or country_3 == ctry_or_region:                  # while user does not enter a country in ctry_list or 'country_3' is equal to 'country_2' or 'country_3' is equal to ctry_or_region
            print('Please input a valid country\n')                                                                 # prompt user for valid country
            country_3 = input('Input a third country: ')                            
        
        print(f'\nSelected countries:\n{ctry_or_region} | {country_2} | {country_3}')                                    # prints the user's inputted countries                                                                                                                      
        print("\n'Country', 'Population', and 'Species' data is available.")                                             # prints a new line and 'Country', 'Population', and 'Species' data is available.

        option_input = input('Please input one of the options from the list above: ')                                    # prompt user to choose to print country, pop, or species data

        while option_input != 'Country' and option_input != 'Population' and option_input != 'Species':                  # while user does not enter a valid option 
            print('Please input a valid option\n')                                                                       # prompt user for valid option
            option_input = input('Please input one of the options from the list above: ')                                

        if option_input == 'Country':                                                                                    # if users choice is country data 
            ctry_func(ctry_or_region, country_2, country_3, ctry_list, reg_list, subreg_list, sqkm_list, pop_data)       # call ctry_func function 

        elif option_input == 'Population':                                                                               # if users choice is pop data
            pop_year_input = input('\nInput a year (2000 - 2020) (enter "year Pop"): ')                                  # prompt user to input a year

            while pop_year_input not in year_list:                                                                       # while user does not enter a year in year list
                print('Please input a valid year\n')                                                                     # prompt user for valid year
                pop_year_input = input('Input a year (2000 - 2020) (enter "year Pop"): ')                                
            
            pop_func(ctry_or_region, country_2, country_3, pop_year_input, pop_data, ctry_list, year_list)               # call pop_func fuction

        elif option_input == 'Species':                                                                                                 # if user's choice is threatened species data
            threatened_spec(ctry_or_region, country_2, country_3, ctry_list, plant_list, fish_list, bird_list, mammal_list)             # call threatened_spec function

#---------- CHOICE 2: REGION

    elif ctry_or_region in reg_list[1:196]:                                 # if user choice is a region
        print(f'\nCountries in the region of {ctry_or_region}:')
        
        ctrys_in_region = []                                                # list of countries in the region
        for i in country_data:                                              # for i in country data
            if i[1] == ctry_or_region:                                      # if i index 1 (region) equals inputted region
                ctrys_in_region.append(i[0])                                # append index 0 (country) to ctrys_in_region list                                                    
        
        for i in ctrys_in_region:                                           # for i in ctrys_in_region list
            print(i, end = ' | ')                                           # print country i in region
        
        reg_year_input = input(f'\n\nInput a year from (2000 - 2020) to find the average population of {ctry_or_region} (enter "year Pop"): ')      # prompt user to input year to find average pop of region in that year
        
        while reg_year_input not in year_list:                                                                                                      # while inputted year is not in year_list
            print('Please input a valid year')                                                                                                      # prompt user for valid year
            reg_year_input = input(f'\nInput a year from (2000 - 2020) to find the average population of {ctry_or_region} (enter "year Pop"): ')    

        avg_pop_of_region_in_year = year_avg_pop_reg_or_subreg(ctrys_in_region, pop_data, year_list, reg_year_input)               # call year_avg_pop_reg_or_subreg function
        avg_pop_reg = AvgYearPopRegSubreg(ctry_or_region, reg_year_input, avg_pop_of_region_in_year)                            # pass in variables to AvgYearPopRegSubreg
        avg_pop_reg.print_avg_reg_or_subreg_pop()                                                                               # call print_avg_reg_or_subreg_pop from class AvgYearPopRegSubreg

        print(f'Sub Regions in the region of {ctry_or_region}:')

        subreg_in_region = []                                               # list of sub regions in the region
        for i in country_data:                                              # for i in country data
            if i[1] == ctry_or_region:                                      # if i index 1 (region) equals inputted region
                subreg_in_region.append(i[2])                               # append index 2 (sub region) to subreg_in_region list                                                    
        
        subreg_in_region = list(dict.fromkeys(subreg_in_region))            # create dictionary and convert back to list to remove duplicates
        for i in subreg_in_region:                                          # for i in subreg_in_region list
            print(i, end = ' | ')                                           # print sub region i in region

        subreg_input = input(f'\n\nInput a sub region (input style: Capital Words) from {ctry_or_region}: ')        # prompt user for a sub region in inputted region
        
        while subreg_input not in subreg_in_region:                                                                 # while user input is not a sub region in subreg_in_region
            print(f'Please input a valid sub region in {ctry_or_region}')                                           # prompt user for valid sub region
            subreg_input = input('\nInput a sub region (input style: Capital Words): ')    
            
        print(f'\nCountries in the sub region of {subreg_input}:')

        ctrys_in_subreg = []                                # list of countries in the sub region
        for i in country_data:                              # for i in country data
            if i[2] == subreg_input:                        # if i index 2 (sub region) equals inputted sub region
                ctrys_in_subreg.append(i[0])                # append index 0 (country) to ctrys_in_subreg list 
                
        for i in ctrys_in_subreg:                           # for i in ctrys_in_subreg list
            print(i, end = ' | ')                           # print country i in sub region
            
        subreg_year_input = input(f'\n\nInput a year from (2000 - 2020) to find the average population in {subreg_input} (enter "year Pop"): ')         # prompt user to input year to find average pop of sub region in that year
        
        while subreg_year_input not in year_list:                                                                                                       # while inputted year is not in year_list
            print('Please input a valid year')                                                                                                          # prompt user for valid year
            subreg_year_input = input(f'\nInput a year from (2000 - 2020) to find the average population in {subreg_input} (enter "year Pop"): ')      

        avg_pop_of_sub_region_in_year = year_avg_pop_reg_or_subreg(ctrys_in_subreg, pop_data, year_list, reg_year_input)            # call year_avg_pop_reg_or_subreg function
        avg_pop_subreg = AvgYearPopRegSubreg(subreg_input, subreg_year_input, avg_pop_of_sub_region_in_year)                        # pass in variables to AvgYearPopRegSubreg
        avg_pop_subreg.print_avg_reg_or_subreg_pop()                                                                                # call print_avg_reg_or_subreg_pop from class AvgYearPopRegSubreg

        user_input_ctry = input(f"Input a country (input style: Capital Words) from the region of {ctry_or_region} to find it's average population from (2000 - 2020): ")           # prompt user to input a country in the region

        while user_input_ctry not in ctrys_in_region:                                                                                                                               # while user does not enter an input in ctrys_in_region
            print(f'Please input a valid country from {ctry_or_region}')                                                                                                            # prompt user for valid country
            user_input_ctry = input(f"\nInput a country (input style: Capital Words) from the region of {ctry_or_region} to find it's average population from (2000 - 2020): ")     

        if user_input_ctry in ctrys_in_region:                                    # if user input is a country in ctrys_in_region                                                                           
            avg_pop_ctry(ctry_list, user_input_ctry, pop_data)                    # call avg_pop_ctry function

        print(f"\nGraph data of {ctry_or_region}'s average populations from (2000 - 2020):")                   # print graph data of inputted region statement
        reg_yearly_avg_pop = all_years_pop_avg(year_list, ctrys_in_region, pop_data)                         # call all_years_pop_avg function
        region_graph(year_list, ctry_or_region, reg_yearly_avg_pop)                                          # call region_graph function

#---------- CALL MAIN FUNCTION

if __name__ == '__main__': 
    main()                  