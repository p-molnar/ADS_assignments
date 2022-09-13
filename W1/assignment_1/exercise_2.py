# first n prime numbers

def is_prime(num):
	for i in range(2, num):
		if (num % i) == 0:
			return False
	return True

input_text = int(input("please give a sequence lenght: "))

n = input_text
i = 2
len = 0
prime_list = []

while 1:
	if is_prime(i):
		prime_list.append(i)
		len += 1
	if len == n:
		break
	i += 1

for counter, num in enumerate(prime_list, start=1):
	print(f"{counter}. {num}")