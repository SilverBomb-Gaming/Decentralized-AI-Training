import torch

torch.distributed.init_process_group(
    backend="gloo",
    init_method="tcp://127.0.0.1:29500",  # Ensure this is the correct address
    rank=0,
    world_size=1  # Change this based on the number of nodes
)

def train():
    model = torch.nn.Linear(10, 2)  # Simple model
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    for _ in range(100):
        optimizer.zero_grad()
        output = model(torch.randn(10))
        loss = output.sum()
        loss.backward()
        optimizer.step()
    print("Training complete.")

train()
