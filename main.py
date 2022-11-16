with open ("input.txt") as f :
    content = f. read () . splitlines ()

my_sum = 0 
for item in content:
    my_sum = my_sum + int(item)
print(my_sum)