import docker

client = docker.from_env()

containers = client.containers.list()

print(f"Found {len(containers)} containers\n")

for container in containers:
    print(f"Name:   {container.name}")
    print(f"Image:  {container.image.tags}")
    print(f"Status: {container.status}")
    print("-" * 40)
