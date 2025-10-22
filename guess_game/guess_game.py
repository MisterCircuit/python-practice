var = 13
count=0
while count !=7:
    guess=int(input("Guess my number: "))
    count+=1
    if count==6:
        print("You have exhausted your count")
        break
    if guess<var:
        print("Wrong! Less than")
    elif guess>var:
        print("Wrong! Greater than")
    elif guess==var:
        print(f"You are correct after {count} trial")
        break

        
    
