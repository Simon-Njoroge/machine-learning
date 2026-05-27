import torch
import torch_directml

device=torch_directml.device()

x = torch.rand(2,3).to(device)

y= torch.cuda.is_available()




print(x.device)
print(y)
print(device)
print(f"torch version:{torch.__version__}")

def __init__():
    print("Hello world")

__init__()