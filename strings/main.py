# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)


report = scorer_0 + " scored in the " + str(goal_0) + "nd minute" + '\n' + scorer_1 + " scored in the " + str(goal_1) + "th minute" 




#### EDITED FIXED PART!!!! 

player = scorer_0 # or 1?

space = player.find(" ")
first_name = player[0:space]
last_name = player[space + 1:len(player)]


last_name_len = len(player[space + 1:len(player)])

name_short = first_name[0] + ". " +last_name


cheer = ((first_name + "! ") * len(first_name))
chant = cheer[0:len(cheer) -1]  

good_chant = ' ' not in chant[len(chant) -1] # my brain can't crack this one :( ...... it works though 
