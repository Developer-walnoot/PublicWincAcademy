# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
################################################################################




def alphabetical_order(x):
    return sorted(x)


###Wincpy rekent dit hieronder fout? All mijn outputs zijn correct BUG? 

def won_golden_globe(x):
    globes = ['Jaws', 'Star Wars: Episode IV – A New Hope','E.T. the Extra-Terrestrial','Memoirs of a Geisha']
    x.lower()
    c = x.capitalize()
    return c in globes


def remove_toto_albums(x):
    y = len(x)
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in between', '35th Anniversary – Live in Poland', 'Toto XIV', 'Old Is New', '40 Tours Around the Sun - Live in Holland']
    new_list = []
    z = 0;
    for z in range(y):
        checker = x[z]
        if checker not in toto_albums:
            new_list.append(checker)
    return new_list



### Ugly_list == user input // assign gets all values of ugly_list one by one. Toto albums hard coded. Check if assign in toto_albums if yes 
#for x in range(y):
#    checker = ugly_list[x]
#    if checker not in toto_albums:
#        new_list.append(checker)
#print(new_list)
#        
#### print(ugly_list[x:y])






