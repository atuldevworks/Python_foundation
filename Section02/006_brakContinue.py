cars=["1","32","faulty","83"]
for status in cars:
    if status=="faulty":
        print("Stopping Production line")
        break
    
    print("This car is of status {}".format(status))
    
else:
    print("production done successfully")
    
    
for status in cars:
    if status=="faulty":
        print("Stopping Production line")
        continue
    else:
        print("This car is of status {}".format(status))
        
else:
    print("production done successfully")