import docker
import json

client = docker.from_env()

containers = client.containers.list()

for container in containers:
    print("=" * 50)
    print(f"Name: {container.name}")
    print(f"Image: {container.image.tags}")
    print(f"Status: {container.status}")

    print("\nLabels:")
    print(json.dumps(container.labels, indent=2))
