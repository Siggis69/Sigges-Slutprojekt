import random

def generate_random_list(length, min_value, max_value):
    """
    Genererar en lista med slumpmässiga nummer. 
    Antal tal, min value och max value specad i parametrarna.
    """
    global random_list
    
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


if __name__ == '__main__': # kod som kör funktionen ovan, för att testa så den fungerar innan den importeras in i den andra filen.
    length = int(input("Ange längden på listan: "))
    min_value = int(input("Ange det minsta värdet: "))
    max_value = int(input("Ange det största värdet: "))
    
    random_list = generate_random_list(length, min_value, max_value)
    print(random_list)



