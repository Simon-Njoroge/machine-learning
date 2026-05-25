import torch

x = torch.rand(2,3)

y= torch.cuda.is_available()

print(x)
print(y)
print(f"torch version:{torch.__version__}")

def __init__():
    print("Hello world")

__init__()