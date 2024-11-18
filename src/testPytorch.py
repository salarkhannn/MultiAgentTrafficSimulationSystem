import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available)

x=torch.tensor([1.0, 2.0, 3.0])
y=torch.tensor([4.0, 5.0, 6.0])

z = x + y

print("Tensor x:", x)
print("Tensor y:", y)
print("Sum of x and y:", z)