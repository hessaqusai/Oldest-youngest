while True:
    print("")
    Name1=input("Enter the name of person 1:")
    Age1=int(input("Enter the age of person 1:"))
    Name2=input("Enter the name of person 2:")
    Age2=int(input("Enter the age of person 2:"))
    Name3=input("Enter the name of person 3:")
    Age3=int(input("Enter the age of person 3:"))
    Name4=input("Enter the name of person 4:")
    Age4=int(input("Enter the age of person 4:"))
    if Age1>Age2 and Age1>Age3 and Age1>Age4:
        print("The oldest person is", Name1,"with", Age1,"years")
    elif Age2>Age1 and Age2>Age3 and Age2>Age4:
        print("The oldest person is", Name2,"with", Age2,"years")
    elif Age3>Age1 and Age3>Age2 and Age3>Age4:
        print("The oldest person is", Name3,"with", Age3,"years")
    else:
        print("The oldest person is", Name4,"with", Age4,"years")
    if Age1<Age2 and Age1<Age3 and Age1<Age4:
        print("The youngest person is", Name1,"with", Age1,"years")
    elif Age2<Age1 and Age2<Age3 and Age2<Age4:
        print("The youngest person is", Name2,"with", Age2,"years")
    elif Age3<Age1 and Age3<Age2 and Age3<Age4:
        print("The youngest person is", Name3,"with", Age3,"years")
    else:
        print("The youngest person is", Name4,"with", Age4,"years")
  
