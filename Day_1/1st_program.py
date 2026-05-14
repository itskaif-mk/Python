while True:

    user = input("Enter Your name")

    if user.lower() in ['q','exit']:
        print("Exited")
        break

    print("User Name is : ", user)