
direction = input("You arrive at a fork in the path. Do you go 'left' or 'right'? ").lower()

if direction == "left":
    action = input("You see a river. Do you 'swim' or 'wait'? ").lower()
    
    if action == "swim":
        print("You bravely swim across and find hidden treasure! ")
    else:
        print("You wait too long. Night falls and you are attacked by wolves. ")
        
else:
    print("You walk right into a trap and fall into a pit! ")