class employee:
    
    # initializing
    def __init__(self):
        print("Employee created")

    #Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_obj():
    print("Making Object....")
    obj = employee()
    print("Function end....")
    return obj

print('Calling Creat_obj() function...')
obj = Create_obj()
print('Progress End...')
