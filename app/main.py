import sys

from app.docker_manager import DockerManager
from app.stack_manager import StackManager
from app.update_manager import UpdateManager


def main():
    docker = DockerManager()
    stack_manager = StackManager()
    updater = UpdateManager()

    containers = docker.get_containers()
    stacks = stack_manager.group_containers(containers)

    # Update Command
    if len(sys.argv) == 3 and sys.argv[1] == "update":
        stack_name = sys.argv[2]

        for stack in stacks:
            if stack.project == stack_name:
                updater.update_stack(stack)
                return

        print(f"Stack '{stack_name}' not found")
        return

    print("\nDetected stacks:\n")

    for stack in stacks:
        print(f"Stack: {stack.project}")

        for container in stack.containers:
            print(f"  - {container.name}")
            print(f"    Image: {container.image}")
            print(f"    Image ID: {container.image_id}")

        print()


if __name__ == "__main__":
    main()
