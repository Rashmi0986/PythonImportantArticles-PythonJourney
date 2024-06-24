def add_one_decorator(func):
	def add_one():
	    value = func()
	    return value + 1
	return add_one
	
def example_function():
	return 1
    
final_value = add_one_decorator(example_function)
print(final_value()) # 2
