def fizzbuzz_dict():
    fb_dict = dict()
    for x in range(1,101):
        fb_dict[x] = "Fizz"*(x%3<1)+"Buzz"*(x%5<1) or x

    return fb_dict
# Some assertion to make sure it works correctly
assert fizzbuzz_dict()[1] == 1
assert fizzbuzz_dict()[3] == "Fizz"
assert fizzbuzz_dict()[28] == 28
assert fizzbuzz_dict()[5] == "Buzz"
assert fizzbuzz_dict()[15] == "FizzBuzz"
assert len(fizzbuzz_dict()) == 100

print "All values:"
print fizzbuzz_dict().values()

print "Each number on a new line:"
for i in range(1,101):
        print(fizzbuzz_dict().get(i,i))
    
