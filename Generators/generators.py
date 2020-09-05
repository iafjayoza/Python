# Example of Normal list
def square_numbers(num):
    result = []
    for i in num:
        result.append(i*i)
    return result

my_num = square_numbers([1,2,3,4,5])

print(my_num)

# Excample of Generator

def gen_square_number(num):
    for i in num:
        yield i*i

gen_num = gen_square_number([1,2,3,4,5])

print(gen_num)
print(next(gen_num))


# List comprehention example of generator

# Normal case
my_lnum = [i*i for i in [1,2,3,4,5]]

for num in my_lnum:
    print(num)

#Generator Case

my_gnum = (i*i for i in [1,2,3,4,5])

print(my_gnum)
print(next(my_gnum))
print(list(my_gnum))
