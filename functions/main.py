# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

def main():
    print(greet("Magician"))

def greet(name):
    return "Hello, " + str(name) + "!" 

def add(x, y, z):
    return x + y + z 

def positive(x):
    return x > 0

def negative(x):
    return x < 0

if __name__ == '__main__':
    main()
