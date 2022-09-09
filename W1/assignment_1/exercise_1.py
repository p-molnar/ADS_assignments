# temperature converter

def c_to_f(c):
	print(c * 9/5 + 32)

def c_to_k(c):
	print(c + 273.15)

def f_to_c(f):
	print(f * 9/5 + 32)

def f_to_k(f):
	print(f + 273.15)

def k_to_c(k):
	print(k - 273.15)

def k_to_f(k):
	print(k * 9/5 - 459.67)

scales = ["C", "F", "K"]
input_text = input("please give a temperature that you want to convert: ")

while input_text[-1].upper() not in scales:
	print("your input must be in Celsius, Farenheit or Kelvin")
	input_text = input("please give a temperature that you want to convert: ")

temperature = float(input_text[:-1])
input_scale = input_text[-1]

if input_scale == "C":
	c_to_f(temperature)
	c_to_k(temperature)
elif input_scale == "F":
	f_to_c(temperature)
	f_to_k(temperature)
else:
	k_to_c(temperature)
	k_to_f(temperature)