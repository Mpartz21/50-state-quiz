def main():
    welcome()
    filename = request()
    mydictionary = newdic(filename)
    noq = 0
    noq = len(mydictionary)
    if noq > 0:
        score = 0
        answer = " "
        while answer != 'quit':
            if len(mydictionary) > 0:
                state,capital  = mydictionary.popitem()
                answer = input("What is the capital of " + str(state) + "?")
                if answer.upper() == capital.upper():
                    score += 1
                    print("You got that right?")
                else:
                    print(" HAHA YOU GOT THAT WRONG!! ")
            else:
                print(" No more questions left ")
                print(" Your score is " + str(score))
                answer = input(""" Press 'QUIT' """)      
    else:
        print(" Quiz ain't here fam or missin' ")                                      
def welcome():
    print("Welcome to the State and Capitals Quiz.")
    print("""Enter the answer to the question or type 'quit' anytime to quir the program.""")
def request():
    filename = input("What is the name of the file to read from?: ")
    return filename
def newdic(filename):   
    mydic = {}
    try:
        y = open( filename,'r' )
        for line in y:
            line_list = line.rstrip('\n').split(',')
            state = line_list[0]
            capital = line_list[1]
            mydic[state] = capital 
    except:
        print("The file was not found.")  
    return mydic
main()


