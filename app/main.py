import sys

from app.docker_manager import DockerManager
from app.stack_manager import StackManager
from app.update_manager import UpdateManager
from app.update_checker import UpdateChecker



def main():
    docker = DockerManager()
    stack_manager = StackManager()
    updater = UpdateManager()
    checker = UpdateChecker()

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
    	update = checker.check_stack(stack)

    	print(
            f"{update.stack}: "
            f"{'UPDATE AVAILABLE' if update.has_updates else 'UP TO DATE'}"
    	)


if __name__ == "__main__":
    main()
