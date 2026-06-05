from app.docker_manager import DockerManager
from app.stack_manager import StackManager

docker = DockerManager()
stack_manager = StackManager()

containers = docker.get_containers()
stacks = stack_manager.group_containers(containers)

for stack in stacks:
    print(f"\nStack: {stack.project}")
    print(f"Compose: {stack.compose_file}")

    for container in stack.containers:
        print(f"  - {container.name}")
