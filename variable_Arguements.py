def add(*args):
	sum = 0
	for i in args:
		sum+=i
	return sum


def key_value(**kwargs):
	for key,value in kwargs.items():
		print(f"{key}, {value}")

sum1 = add(1,2)
sum2 = add(1,2,3)

print(f"sum1 : {sum1} , sum2 : {sum2}")


key_value(name = "krish", age = 13, city ="BBS")
key_value(name = "krish", age = 13)
key_value(name = "krish")






