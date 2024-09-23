

print("Welcome to the Treasure Island.\ YOur mission is to find the treasure.")

direction = input("YOu're at a cross road. Where do you want to go? Type 'left' or 'right'")



if direction == "left":
    swim = input("You come to a lake. THere is an island in the middle of the lacke. Type 'wait' to wait for a boat. Type 'swim' to swim across")
    if swim == "wait":
        color = input("choose from red, yellow or blue")
        if color == "red":
            print("red")
        elif color == "yellow":
            print("yellow")
        else:
            print("blue")
    else:
        print("game over")
else:
    print("game over")





