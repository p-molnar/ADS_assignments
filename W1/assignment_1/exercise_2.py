def is_prime(num):
	for i in range(2, num):
		if (num % i) == 0:
			return False
	return True

input_text = input("please give a sequence lenght: ")

n = int(input_text)
i = 2
prime_list = []

while 1:
	if is_prime(i):
		prime_list.append(i)
	if len(prime_list) == n:
		break
	i += 1

for i, n in enumerate(prime_list, 1):
	print(f"{i}. {n}")