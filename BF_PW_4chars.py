"""
4-Character Brute Force Password Cracker
Written by: Nicholas Drexler 

"""

# We want to time the program
from datetime import datetime    

# TO DO:
    # intermidiate version, specify more than 4 digits
    # harder version, do not specify the number of digits

breakout_flag = False           # use this to break out of nested loops
char_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n" \
              ,"o","p","q","r","s","t","u","v","w","x","y","z" \
              ,"A","B","C","D","E","F","G","H","I","J","K","L","M","N" \
              ,"O","P","Q","R","S","T","U","V","W","X","Y","Z" \
              ,"0","1","2","3","4","5","6","7","8","9" \
              ,"!","@","#","$","%","^","&","*","(",")" \
              ," ","-","_","+","=","~","`", "{", "}","[","]","<", ">", "," \
              ,".", "?", "/", "|", "'", ":", ";"] 


def passinput():
    """ 
    Allows user to imput a password. If the password is not 4 characters, 
    then the user will be prompted to try again.
    """

    print("Please enter a 4 character password.")
    print("You can use uppercase, lowercase, a space, number or symbol.")
    global password 
    password = input("Input password here: ")
  
    if len(password) != 4:
        print("Your password must be 4 characters long. Try again.")
        passinput()
    else:
        print("CRACKING YOUR PASSWORD NOW")


passinput()


# Start timing it
start_time = datetime.now()

# Iterations used to grind through all possible combos
for i in char_array:
    for j in char_array:
        for k in char_array:
            for l in char_array:

                guessA = str(i)
                guessB = str(j)
                guessC = str(k)
                guessD = str(l)
                
                attempt = guessA + guessB + guessC + guessD

                if attempt == password:
                    breakout_flag = True
                    print("Password cracked! ")
                    print("The password is: ", attempt)
                    # break out of l loop
                    break     
            # break out of k loop        
            if breakout_flag == True:
                break
        # break out of j loop        
        if breakout_flag == True:
            break
    # break out of i loop
    if breakout_flag == True:
        break

#end the timing and show how long it took
end_time = datetime.now()
print('Time for application to run {}'.format(end_time - start_time))