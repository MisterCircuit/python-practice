speed = int(input("Enter speed: "))
if speed <= 70:
    print("OK")
diff = speed -70
while diff >=5:
    div=int(diff/5)
    if div>12:
        print(f"Points: {div}")
        print("License suspended")
        break
    print(f"Points: {div}")
    break
    
    
