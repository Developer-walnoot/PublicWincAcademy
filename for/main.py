4
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

def shortest_names(x):
    x_sorted = list(sorted(x, key = len))
    new_list = []
    for count in range(len(x_sorted)):
        if len(x_sorted[count]) > len(x_sorted[0]):
            break
        new_list.append(x_sorted[count])
    return new_list

def most_vowels(x):
    countries = x
    vowels_str = ("aeiou")
    rankings = []
    total_country = len(countries)
    for count in range(total_country):
        c = 0
        current_country = countries[count]
        for count in range(len(vowels_str)):
            z = vowels_str[count]
            y_lower = current_country.lower()
            y = y_lower.count(z)
            c = c + y        
        rankings.append(c)                   
    most_vowel = max(rankings)
    most_vowels_list = []
    step = 1
    for count in range(most_vowel):
        step = step + 1
        if rankings.count(most_vowel - count) != 0:
            indices = [i for i, x in enumerate(rankings) if x == most_vowel - count]
            for count in range(len(indices)):
                current_count = countries[indices[count]]
                most_vowels_list.append(current_count)
                if len(most_vowels_list) == step:
                    return most_vowels_list      

def alphabet_set(x):
    return x
       
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`

            


if __name__ == '__main__':
    countries = get_countries()
    print(most_vowels(countries))    
 

#print(countries[vowels_list[0]]) 

#for count in range(len(vowels_str)):
#    x = vowels_str[count]
#    y_lower = text.lower()
#    y = y_lower.count(x)
#    c = c + y




    
