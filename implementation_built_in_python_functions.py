# 18/04/25, 24/04/25 | "Implementation built-in Python functions"

# Notes:

"""
	Brief information about the functions is taken through the help() function call,
	partially paraphrased somewhere, full information can be found in the official documentation.

	Python 3.13.3 documentation - https://docs.python.org/3/index.html
"""

import math, typing, collections.abc, functools

# Implementation built-in functions

"""
	---------- Implementing range ----------

	class range(object)
		range(stop) -> range object
		range(start, stop[, step]) -> range object

	Return an object that produces a sequence of integers from start (inclusive)
	to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
	start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
	These are exactly the valid indices for a list of 4 elements.
	When step is given, it specifies the increment (or decrement).
"""

def custom_range_generator(start: int = 0, stop: typing.Optional[int] = None, step: int = 1) -> typing.Generator[int, None, None]:
	""" Implementation built-in range generator function through use yield """

	if not isinstance(start, int) or not isinstance(step, int):
		raise TypeError("\nTypeError: expected int object")

	if stop is not None and not isinstance(stop, int):
		raise TypeError("\nTypeError: expected int object")

	if step == 0:
		raise ValueError("\nValueError: expected not zero value")

	if stop is None:
		stop = start
		start = 0

	if step > 0:
		while start < stop:
			yield start
			start += step
	else:
		while start > stop:
			yield start
			start += step

	return None

"""
	---------- Implementing filter ----------

	class filter(object)
		filter(function or None, iterable) --> filter object

	Return an iterator yielding those items of iterable for which function(item)
	is true. If function is None, return the items that are true.

	----------------------------------------------------------------------------------------------------

	Function named custom_filter that replicates the behavior
	of the built-in filter function. Implementation should take two arguments:

	1. A function that returns a boolean value.
	2. An iterable.

	The function should return a list of all items in the iterable for which the function returns True.

	Requirements:

	* Use a loop to iterate through the items in the iterable.
	* Apply the provided function to each item.
	* Append items that meet the condition to a new list.
	* Return the new list.

	Example:

	# Example usage of custom_filter

	def is_even(x):
		return x % 2 == 0

	numbers = [1, 2, 3, 4, 5, 6]
	result = custom_filter(is_even, numbers)

	print(result)  # Output: [2, 4, 6]
"""

def is_even(num: int) -> bool:
	""" Check number is even or not """

	if not isinstance(num, int):
		print("\nInvalid value type: expected int")
		return False

	return not (abs(num) & 1) # abs(num) % 2 == 0

def custom_filter(function: typing.Callable[[int], bool], iterable: typing.Iterable[int]) -> typing.Iterable[int]:
	""" Implementing built-in filter function """

	if not callable(function) and function is not None:
		# Version I
		"""
		print("\nInvalid value type: expected function(int) -> bool or None")
		return None
		"""

		# Version II
		raise TypeError("\nTypeError: expected function(int) -> bool or None")

	if not isinstance(iterable, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable object with int values")

	filter_iterable = []

	if function is None: # not function, function == None
		# Version I
		"""
		for i in iterable:
			if i:
				filter_iterable.append(i)
		"""

		# Version II
		function = lambda x : x

	for i in iterable:
		if function(i): # function(i) == True
			filter_iterable.append(i)

	return filter_iterable

def custom_filter_generator(function: typing.Callable[[int], bool], iterable: typing.Iterable[int]) -> typing.Iterable[int]:
	""" Implementing built-in filter generator function through using yield """

	if not callable(function) and function is not None:
		raise TypeError("\nTypeError: expected function(int) -> bool or None")

	if not isinstance(iterable, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable object with int values")

	filter_iterable = []

	if function is None:
		function = lambda x : x

	j = 0

	for i in iterable:
		if function(i):
			filter_iterable.append(i)

			yield filter_iterable[j]

			j += 1

	return None

"""
	---------- Implementing map ----------

	class map(object)
		map(func, *iterables) --> map object

	Make an iterator that computes the function using arguments from
	each of the iterables.  Stops when the shortest iterable is exhausted.

	----------------------------------------------------------------------------------------------------

	Function named custom_map that replicates the behavior
	of the built-in map function. Implementation should take two arguments:

	1. A function that transforms an input.
	2. An iterable.

	The function should return a list where each item is the result of
	applying the function to the corresponding item in the iterable.

	Requirements:

	* Use a loop to apply the function to each item in the iterable.
	* Store the results in a new list.
	* Return the new list.

	Example:

	# Example usage of custom_map

	def square(x):
		return x ** 2

	numbers = [1, 2, 3, 4]
	result = custom_map(square, numbers)

	print(result)  # Output: [1, 4, 9, 16]
"""

def custom_map(function: typing.Callable[[int], int], *iterables: typing.Iterable[int]) -> list:
	""" Implementing built-in map function """

	if not callable(function):
		raise TypeError("\nTypeError: expected function(int) -> int")

	if not isinstance(iterables, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable objects with int values")

	if function is None:
		raise ValueError("\nValueError: expected function(int) -> int")

	# Version I
	"""
	iterables_min_length = len(iterables[0])

	for i in iterables[1:]:
		if len(i) < iterables_min_length:
			iterables_min_length = len(i)
	"""

	# Version II
	iterables_min_length = min(len(i) for i in iterables) # iterables_min_length = len(min(*iterables, key = len))

	map_iterables = []

	for i in range(iterables_min_length):
		tmp_iterables = []

		for j in iterables:
			tmp_iterables.append(j[i])

		map_iterables.append(function(*tmp_iterables))

	return map_iterables

def custom_map_generator(function: typing.Callable[[int], int], *iterables: typing.Iterable[int]) -> typing.Generator[list, None, None]:
	""" Implementing built-in map generator function through using yield """

	if not callable(function):
		raise TypeError("\nTypeError: expected function(int) -> int")

	if not isinstance(iterables, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable objects with int values")

	if function is None:
		raise ValueError("\nValueError: expected function(int) -> int")

	iterables_min_length = min(len(i) for i in iterables) # iterables_min_length = len(min(*iterables, key = len))

	map_iterables = []

	x = 0

	for i in range(iterables_min_length):
		tmp_iterables = []

		for j in iterables:
			tmp_iterables.append(j[i])

		map_iterables.append(function(*tmp_iterables))

		yield map_iterables[x]

		x += 1

	return None

"""
	---------- Implementing zip ----------

	class zip(object)
		zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

		# >>> list(zip('abcdefg', range(3), range(4)))
		[('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]

	The zip object yields n-length tuples, where n is the number of iterables
	passed as positional arguments to zip().  The i-th element in every tuple
	comes from the i-th iterable argument to zip().  This continues until the
	shortest argument is exhausted.

	If strict is true and one of the arguments is exhausted before the others,
	raise a ValueError.

	----------------------------------------------------------------------------------------------------

	Function named custom_zip that replicates the behavior
	of the built-in zip function. Implementation should take two iterables and
	return a list of tuples, where each tuple contains
	one element from each iterable at the same position.

	Requirements:

	* Ensure the returned list is as long as the shorter of the two input iterables.
	* Use a loop to pair elements from the iterables into tuples.

	Example:

	# Example usage of custom_zip

	list1 = [1, 2, 3]
	list2 = ['a', 'b', 'c']
	result = custom_zip(list1, list2)

	print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
"""

def custom_zip(*iterables: typing.Iterable[int], strict: bool = False) -> tuple:
	""" Implementing built-in zip function """

	if not isinstance(iterables, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable objects with int values")

	if not isinstance(strict, bool):
		raise TypeError("\nTypeError: expected bool")

	zip_iterables = []

	iterables_min_length = len(iterables[0])

	for i in iterables[1:]:
		if len(i) < iterables_min_length:
			if strict:
				raise ValueError("\nValueError: expected all iterables equal length")

			iterables_min_length = len(i)

	for i in range(iterables_min_length):
		tmp_iterables = []

		for j in iterables:
			tmp_iterables.append(j[i])

		zip_iterables.append(tuple(tmp_iterables))

	return zip_iterables

def custom_zip_generator(*iterables: typing.Iterable[int], strict: bool = False) -> typing.Generator[tuple, None, None]:
	""" Implementing built-in zip generator function through using yield """

	if not all(isinstance(i, typing.Iterable) for i in iterables):
		raise TypeError("\nTypeError: expected iterable objects with int values")

	if not isinstance(strict, bool):
		raise TypeError("\nTypeError: expected bool")

	zip_iterables = []

	iterables_min_length = len(iterables[0])

	for i in iterables[1:]:
		if len(i) < iterables_min_length:
			if strict:
				raise ValueError("\nValueError: expected all iterables equal length")

			iterables_min_length = len(i)

		elif len(i) > iterables_min_length and strict:
			raise ValueError("\nValueError: expected all iterables equal length")

	for i in range(iterables_min_length):
		tmp_iterables = []

		for j in iterables:
			tmp_iterables.append(j[i])

		yield tuple(tmp_iterables)

	return None

"""
	---------- Implementing reduce ----------

	reduce(...)
		reduce(function, iterable[, initial]) -> value

	Apply a function of two arguments cumulatively to the items of a sequence
	or iterable, from left to right, so as to reduce the iterable to a single
	value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
	((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
	of the iterable in the calculation, and serves as a default when the
	iterable is empty.

	----------------------------------------------------------------------------------------------------

	Function named custom_reduce that replicates the behavior
	of the functools.reduce function. Implementation should take three arguments:

	1. A binary function (takes two inputs).
	2. An iterable.
	3. An optional initializer (default is None).

	The function should apply the binary function cumulatively to the items in the iterable,
	reducing it to a single value.

	Requirements:

	* If an initializer is provided, use it as the starting value.
	* If no initializer is provided, use the first element of the iterable as the starting value.
	* Raise an error if the iterable is empty and no initializer is provided.

	Example:

	# Example usage of custom_reduce
	def add(x, y):
		return x + y

	numbers = [1, 2, 3, 4]
	result = custom_reduce(add, numbers)
	print(result)  # Output: 10
"""

def custom_reduce(function: typing.Callable[[int, int], int], iterable: typing.Iterable[int], initial: typing.Optional[int] = None) -> int:
	""" Implementing functools.reduce function """

	if not callable(function):
		raise TypeError("\nTypeError: expected callable object(function), (int, int) -> int")

	if not isinstance(iterable, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable object")

	if not function:
		raise ValueError("\nValueError: expected function(int, int) -> int")

	if not iterable:
		raise ValueError("\nValueError: expected not empty iterable")

	if initial is None:
		value = iterable[0]
		start_i = 1
	else:
		value = initial
		start_i = 0

	for i in range(start_i, len(iterable)):
		value = function(value, iterable[i])

	return value

"""
	---------- Implementing enumerate ----------

	class enumerate(object)
		enumerate(iterable, start=0)

	Return an enumerate object.

	iterable an object supporting iteration.

	The enumerate object yields pairs containing a count (from start, which
	

	----------------------------------------------------------------------------------------------------

	Function named custom_enumerate that replicates the behavior
	of the built-in enumerate function. Implementation should take two arguments:

	1. An iterable.
	2. An optional starting index (default is 0).

	The function should return a list of tuples, where each tuple contains an index
	(starting from the given starting index) and the corresponding item from the iterable.

	Requirements:

	* Use a loop to generate the index and pair it with the corresponding item.
	* Append the index-item pairs as tuples to a new list.
	* Return the list.

	Example:

	# Example usage of custom_enumerate

	fruits = ['apple', 'banana', 'cherry']
	result = custom_enumerate(fruits, start=1)

	print(result)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
"""

def custom_enumerate(iterable: typing.Iterable[int], start: int = 0) -> enumerate:
	""" Implementing built-in enumerate function """

	if not isinstance(iterable, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable object")

	if not isinstance(start, int):
		raise TypeError("\nTypeError: expected int")

	if not iterable:
		raise ValueError("\nValueError: expected not empty object")

	result_list = []

	for i in range(len(iterable)):
		result_list.append(tuple([start, iterable[i]]))

		start += 1

	return result_list

def custom_enumerate_generator(iterable: typing.Iterable[int], start: int = 0) -> typing.Generator[list, None, None]:
	""" Implementing built-in enumerate generator function through using yield """

	if not isinstance(iterable, typing.Iterable):
		raise TypeError("\nTypeError: expected iterable object")

	if not isinstance(start, int):
		raise TypeError("\nTypeError: expected int object")

	if not iterable:
		raise ValueError("\nValueError: expected not empty object")

	result_list = []

	for i in range(len(iterable)):
		result_list.append(tuple([start, iterable[i]]))

		yield result_list[i]

		start += 1

	return None

