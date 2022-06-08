def say_hello(name):
    # You can print to STDOUT for debugging like you normally would:
    name = str(input("Qual é o seu nome ? "))
    if name == "" or " ":
        print("Hello, there!")
    else:
        print("Hello, " + name)
    # but you need to return the value in order to complete the challenge
    return ""  #TODO: return the correct value

say_hello("name")
