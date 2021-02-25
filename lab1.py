# Поле (простое число)
nepr = [[], [], [1, 1, 0, 1, 0], []]
class Field:

    def __init__(self, digit, flag):
        self.digit = digit
        self.flag = flag

    def elemsOfField(self):
        if flag:
            elems = [i for i in range(0, digit)]
            return elems
        else:
            self.pow_of_digit = 0
            digit1 = digit
            while True:
                if digit1 == 1:
                    break
                digit1 = digit1 / 2
                self.pow_of_digit = self.pow_of_digit + 1
            return self.pow_of_digit

        #else: если 2^n

    def sum(self):
        sum_of_el = 0
        if flag:
            while True:
                print('Введите число(Для конца ввода введите 0)')
                el = int(input())
                if el == 0:
                    break
                sum_of_el = sum_of_el + el
                sum_of_el = sum_of_el % digit
            return sum_of_el
        else:
            sum_of_el = [0 for i in range(0, self.pow_of_digit + 1)]
            while True:
                el_in_list = []
                print('Введите коэфриценты многочлена до ', self.pow_of_digit - 1, ' степени')
                el = str(input())
                if el == '0':
                    break
                for i in range(0, len(el)):
                    el_in_list.append(int(el[i]))
                for i in range(0, len(el)):
                    sum_of_el[i] = sum_of_el[i] ^ el_in_list[i]
            sum_of_el_str = ''
            for i in range(0, len(sum_of_el)):
                if sum_of_el[i] == 1:
                    sum_of_el_str = sum_of_el_str + 'x^' + str(i) + ' + '
            sum_of_el_str = sum_of_el_str[:-3]
            return sum_of_el_str


    def mul(self):
        mul_of_el = 1
        if flag:
            while True:
                print('Введите число(для конца ввода введите 1)')
                el = int(input())
                if el == 1:
                    break
                mul_of_el = mul_of_el * el
                mul_of_el = mul_of_el % digit
            return mul_of_el
        else:
            el1 = str(input())
            el2 = str(input())
            el1_list = []
            el2_list = []
            for i in range(0,len(el1)):
                el1_list.append(int(el1[i]))
                el2_list.append(int(el2[i]))
            result_list = [0 for i in range(0, (len(el1)-1)*2 + 1)]
            for i in range(0, len(el1)):
                for j in range(0, len(el2)):
                    el = el1_list[i] * el2_list[j]
                    if el != 0:
                        result_list[i+j] = result_list[i+j] + 1

            for i in range(0,len(result_list)):
                if result_list[i] > 1:
                    result_list[i] = result_list[i] % 2

            # print(result_list) #умножили 2 многочлена
            global nepr
            our_nepr = nepr[self.pow_of_digit - 1]
            max_of_result = 0
            max_of_our_nepr = 0
            for i in range(0, len(result_list)):
                if result_list[i] == 1:
                    max_of_result = i
            for i in range(0, len(our_nepr)):
                if our_nepr[i] == 1:
                    max_of_our_nepr = i
            tmp_list_for_nepr = [0 for i in range(0, (len(el1)-1)*2 + 1)]
            tmp_list = [0 for i in range(0, (len(el1)-1)*2 + 1)]
            res_of_nepr = [0 for i in range(0, (len(el1)-1)*2 + 1)]
            while True:
                if max_of_result < max_of_our_nepr:
                    break
                else:
                    tmp_list_for_nepr[max_of_result - max_of_our_nepr] = 1
                    for i in range(0,len(our_nepr)):
                        for j in range(0, len(tmp_list_for_nepr)):
                            el = our_nepr[i] * tmp_list_for_nepr[j]
                            if el != 0:
                                res_of_nepr[i+j] = res_of_nepr[i+j] + 1
                    for i in range(0, len(res_of_nepr)):
                        if res_of_nepr[i] > 1:
                            res_of_nepr[i] = res_of_nepr[i] % 2
                    for i in range(0, len(res_of_nepr)):
                        result_list[i] = result_list[i] ^ res_of_nepr[i]
                    for i in range(0, len(result_list)):
                        if result_list[i] == 1:
                            max_of_result = i
            result_list = result_list[:self.pow_of_digit]
            mul_of_el_str = ''
            for i in range(0, len(result_list)):
                if result_list[i] == 1:
                    mul_of_el_str = mul_of_el_str + 'x^' + str(i) + ' + '  # вынести вывод полинома в отдельную функцию
            mul_of_el_str = mul_of_el_str[:-3]
            return mul_of_el_str


digit = int(input())
flag = True
for i in range(2, digit):
    if digit % i == 0:
        flag = False
        break
field_one = Field(digit, flag)

print(field_one.elemsOfField())
# print(field_one.sum())
print(field_one.mul())










