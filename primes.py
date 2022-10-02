
def primes(number_of_primes):
    list = []
    current_num = 2
    current_index = 0
    flag = True
    while(flag):

        for i in range(2, current_num + 1):
            if current_num % i == 0 and current_num == i:
                list.append(current_num)
                current_num += 1
                current_index += 1
                break
            elif current_num % i == 0:
                current_num += 1
                break
        if current_index == number_of_primes:
            flag = False
            

    return list

