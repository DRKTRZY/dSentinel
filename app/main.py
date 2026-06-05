from app.docker_manager import DockerManager
from app.stack_manager import StackManager
from app.update_manager import UpdateManager


def main():
    docker = DockerManager()
    stack_manager = StackManager()
    updater = UpdateManager()

    containers = docker.get_containers()
    stacks = stack_manager.group_containers(containers)

    print("\nDetected stacks:\n")

    for stack in stacks:
        print(f"Stack: {stack.project}")
        print(f"Compose: {stack.compose_file}")

        for container in stack.containers:
            print(f"  - {container.name}")

        print()

    # TEST: nginx Stack aktualisieren
    for stack in stacks:
        if stack.project == "nginx":
            print("\n=== TEST UPDATE ===\n")
            updater.update_stack(stack)


if __name__ == "__main__":
    main()
