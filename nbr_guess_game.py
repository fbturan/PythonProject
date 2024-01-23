import random

def random_nbr_generate():
    while True:
        four_digit_nbr = random.randint(1000, 9999)
        if(len(set(str(four_digit_nbr)))) == 4:
            return four_digit_nbr

def nbr_guess_game(number1, number2):
    res_one = 0
    res_two = 0
    digit = 0
    nbr1_digits = [int(d) for d in str(number1)]

    while (digit < 4):
        if (int(str(number1)[digit])) == (int(str(number2)[digit])):
            res_one += 1
        elif (int(str(number2)[digit]) in nbr1_digits):
            res_two += 1
        digit += 1
    return res_one, res_two

random_nbr = random_nbr_generate()
counter = 0
print("sayiyi gormek icin pas yazabilirsiniz : ")
while True:
    user_input = input("4 basamakli bir sayi giriniz... : ")
    if ("pas" in user_input):
        print(random_nbr)
        break
    input_nbr = int(user_input)
    if(len(set(str(input_nbr)))) < 4:
        print("girilen sayinin rakamlari birbirinden farkli olmalidir!")
    elif (not(1000 <= input_nbr < 10000)):
        print("girilen sayi dört basamakli olmalidir!")
    else:
        if (random_nbr == input_nbr):
            print("Tebrikler, sayiyi", counter, "adimla doğru tahmin ettiniz...")
            break
        else:
            print(nbr_guess_game(random_nbr, input_nbr))
            counter += 1
