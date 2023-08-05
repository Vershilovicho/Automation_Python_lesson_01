# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def getting_numbers(string): # Получение числителя и знаменателя
    numerator, denominator = map(int, string.split('/'))
    return numerator, denominator

def addition_fractions(fraction_1, fraction_2): # Сложение двух дробей
    numerator_1, denominator_1 = fraction_1
    numerator_2, denominator_2 = fraction_2
    res_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    res_denominator = denominator_1 * denominator_2
    return res_numerator, res_denominator


def product_fractions(fraction_1, fraction_2): # Перемножение двух дробей
    numerator_1, denominator_1 = fraction_1
    numerator_2, denominator_2 = fraction_2
    res_numerator = numerator_1 * numerator_2
    res_denominator = denominator_1 * denominator_2
    return res_numerator, res_denominator

def greatest_common_divisor(a, b): # наибольший общий делитель
    while b != 0:
        a, b = b, a % b
    return a


def fraction_reduction(fraction): 
    numerator, denominator = fraction
    common_divisor = greatest_common_divisor(numerator, denominator)
    new_numerator = numerator // common_divisor
    new_denominator = denominator // common_divisor
    return new_numerator, new_denominator


string_1 = input("Введите первую дробь в виде a/b: ")
string_2 = input("Введите вторую дробь в виде a/b: ")

number_1 = getting_numbers(string_1)
number_2 = getting_numbers(string_2)

add_fractions = addition_fractions(number_1, number_2)
reduced_add_fractions = fraction_reduction(add_fractions)
print("\nСумма дробей:", '/'.join(map(str, reduced_add_fractions)))

mult_fractions = product_fractions(number_1, number_2)
reduced_mult_fractions = fraction_reduction(mult_fractions)
print("Произведение дробей:", '/'.join(map(str, reduced_mult_fractions)))

print(f'\nПроверка первой дроби при помощи fractions: {Fraction(string_1) + Fraction(string_2)}')
print(f'Проверка второй дроби при помощи fractions: {Fraction(string_1) * Fraction(string_2)}')


