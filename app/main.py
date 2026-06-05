import docker

client = docker.from_env()

containers = client.containers.list()

print(f"Found {len(containers)} containers")

for container in containers:
    print(container.name)
