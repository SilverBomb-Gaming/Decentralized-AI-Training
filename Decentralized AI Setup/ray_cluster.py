import torch
print(torch.cuda.is_available())  # Should return True

def initialize_ray():
    ray.init()
    print("Ray Cluster Initialized!")
    print("Available Nodes:", ray.nodes())

if __name__ == "__main__":
    initialize_ray()