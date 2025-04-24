# 22/04/25, 24/04/25 | "Automatic/Manual Testing"

"""
	Testing custom implementations of built-in Python functions
	from a file "implementation_built_in_python_functions.py"

	Modes:
	- Without arguments: automatic testing
	- With the --interactive flag: the user inputs the data manually
"""

import sys # for get list command line arguments

# get functions names
from implementation_built_in_python_functions import (
	custom_range_generator,
	custom_filter,
	custom_filter_generator,
	custom_map,
	custom_map_generator,
	custom_zip,
	custom_zip_generator,
	custom_reduce,
	custom_enumerate,
	custom_enumerate_generator
)

def automatic_tests():
	print(f"\n{'*' * 50} AUTOMATIC TESTING {'*' * 50}")

	# ---------- custom_range ----------

	print("\n-> custom_range_generator()")

	print("\n[5] :", list(custom_range_generator(5)))
	print("[2; 6) :", list(custom_range_generator(2, 6)))
	print("[10; 2) step = -2 :", list(custom_range_generator(10, 2, -2)))

	print('\n' + '-' * 119)

	# ---------- custom_filter ----------

	print("\n-> custom_filter() / custom_filter_generator()")

	def is_even(num): return not (num & 1) # Version I
	# func = lambda x : x % 2 == 0 # Version II

	nums_ls = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

	print(f"\nList numbers values : {nums_ls}")

	print("\n\"Even\" numbers through custom_filter() :", list(custom_filter(is_even, nums_ls)))
	print("\"Even\" numbers through custom_filter_generator():", list(custom_filter_generator(is_even, nums_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_map ----------

	print("\n-> custom_map() / custom_map_generator()")

	def square(x): return x * x

	nums_ls = [-2, 7, 0, 3, 5, -5]

	print(f"\nList numbers values : {nums_ls}")

	print("\n\"Square\" numbers through custom_map() :", list(custom_map(square, nums_ls)))
	print("\"Square\" numbers through custom_map_generator() :", list(custom_map_generator(square, nums_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_zip ----------

	print("\n-> custom_zip() / custom_zip_generator()")

	f_ls = [1, 2, 3]
	s_ls = ['a', 'b', 'c']

	print(f"\nFirst list values : {f_ls}")
	print(f"Second list values : {s_ls}")

	print("\nZip first and second lists result through custom_zip() :", list(custom_zip(f_ls, s_ls)))
	print("Zip first and second lists result through custom_zip_generator() :", list(custom_zip_generator(f_ls, s_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_reduce ----------

	print("\n-> custom_reduce()")

	def multiply(x, y): return x * y

	nums_ls = [1, 2, 3, 4]
	mult_num = 2

	print(f"\nList numbers values : {nums_ls}")

	print("\ncustom_reduce() function application result :", custom_reduce(multiply, nums_ls))
	print(f"custom_reduce() function application with {mult_num} multiply number result :", custom_reduce(multiply, nums_ls, mult_num))

	print('\n' + '-' * 119)

	# ---------- custom_enumerate ----------
	print("\n-> custom_enumerate() / custom_enumerate_generator()")

	items = ['apple', 'banana', 'cherry']

	print(f"\nList values : {items}")

	print("\ncustom_enumerate() function application result :", list(custom_enumerate(items)))
	print("custom_enumerate_generator() function application result :", list(custom_enumerate_generator(items)))

	print("\nAutomatic testing is completed.\n")

def interactive_tests():
	print(f"\n{'*' * 50} INTERACTIVE MODE {'*' * 50}\n")

	# ---------- custom_range ----------

	print("\n-> custom_range_generator()")

	stop = int(input("\nInput range [stop] value(int): "))
	print(f"\nrange({stop}) object`\n{list(custom_range_generator(stop = stop))}")

	start, stop = tuple(map(int, input("\nInput range [start; end] values(int): ").split()))
	print(f"\nrange({start}, {stop}) object`\n{list(custom_range_generator(start, stop))}")

	start, stop, step = tuple(map(int, input("\nInput range [start; end; step] values(int): ").split()))
	print(f"\nrange({start}, {stop}, {step}) object`\n{list(custom_range_generator(start, stop, step))}")

	print('\n' + '-' * 119)

	# ---------- custom_filter ----------

	print("\n-> custom_filter()")

	nums_ls = list(map(int, input("\nInput list numbers(int) through spaces: ").split()))
	func = eval(input("Input lambda function, (example` lambda x : x > 0): "))

	print("\nFilter result :", list(custom_filter(func, nums_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_map ----------

	print("\n-> custom_map()")

	nums_ls = list(map(int, input("\nInput list numbers(int) through spaces: ").split()))
	func = eval(input("Input lambda function, (example` lambda x : x * 2): "))

	print("\nMap result :", list(custom_map(func, nums_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_zip ----------

	print("\n-> custom_zip()")

	f_nums_ls = list(map(int, input("\nInput first list numbers(int) through spaces: ").split()))
	s_nums_ls = list(map(int, input("Input second list numbers(int) through spaces: ").split()))

	print("\nZip result :", list(custom_zip(f_nums_ls, s_nums_ls)))

	print('\n' + '-' * 119)

	# ---------- custom_reduce ----------

	print("\n-> custom_reduce()")

	nums_ls = list(map(int, input("\nInput list numbers(int) through spaces: ").split()))
	func = eval(input("Input lambda function, (example` lambda x, y : x + y): "))

	print("\nReduce result :", custom_reduce(func, nums_ls))

	print('\n' + '-' * 119)

	# ---------- custom_enumerate ----------

	print("\n-> custom_enumerate()")

	items = input("Input items(str) through spaces: ").split()

	print("\nEnumerate result :", list(custom_enumerate(items)))

	print("\nInteractive testing is completed.\n")

if __name__ == "__main__":
	interactive_tests() if "--interactive" in sys.argv else automatic_tests()

