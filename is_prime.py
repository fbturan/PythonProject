def is_prime(sayi):
    if number<=1:
        print("girilen number asal değildir.")
        return
    i = 2
    while i <= number // 2:
        if (number % i == 0):
            print("girilen number asal değildir.")
            return
        i += 1
    print("girilen sayi asaldir.")
number = int(input("bir asal number giriniz: "))
is_prime(number)
