import torch 

#empty tensor
x = torch.empty(2,3)

# 1D tensor
y = torch.rand(1)

# 2D tensor
z = torch.rand(2,3)

#type of tensor
print(x.dtype)
print(y.dtype)
print(z.dtype)


a=torch.rand(2,3)
b=torch.rand(2,3)

#element wise addition
sum=torch.add(a,b)
print(sum)

#subtraction
sub = torch.sub(a,b)
print(sub)

#multiplacation
mul = torch.mul(a,b)
print(mul)

#division
div = torch.div(a,b)