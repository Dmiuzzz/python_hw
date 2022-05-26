from sys import argv

script_name, virobotka, stavka, premiy = argv

def my_func(p_1, p_2, p_3):
    return (int(p_1) * int(p_2) + int(p_3))

print(my_func(virobotka, stavka, premiy))