# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

### part 1

leek_price = 2 

print("Leek is " + str(leek_price) + " euro per kilo.")

##### part 2

order = 'leek 4'

x = order.find(" ")
amount = int(x) + 1
y = order[amount]

sum_total =  int(leek_price) * int(y)
print(sum_total)

#######part 3

broccoli_perKG = 2.34

order_broc = 1.6

total_broc = 2.34*1.6

print(str(order_broc) + "kg broccoli costs " + str(round(total_broc, 2)) + "e")