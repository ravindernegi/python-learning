from functools import reduce

num = [78,878,45,93]


# filter fucntion 
event = list(filter(lambda n: n % 2==0,num))

print(event)



# map fucntion 
double  = list(map(lambda n: n * 2,num))

print(double )




# reduce fucntion 
sum  = reduce(lambda a,b: a + b,double)

print(sum )