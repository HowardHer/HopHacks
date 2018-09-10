"""
name = input("yourname: ")
print(f"hello, {name}!")

x = input()

if x>0:
	print("x is positive")
elif x<0:
	print("x is negative")
else:
	print("x is zero")
	"""
def squared(x):
	return x*x
def main():
	for i in range(10):
		print("{} squared is {}".format(i, squared(i)))	
		
if __name__ == "__main__":
	main()