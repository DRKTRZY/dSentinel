from collections import defaultdict

from app.models import ContainerInfo, StackInfo


class StackManager:
    def group_containers(
        self,
        containers: list[ContainerInfo]
    ) -> list[StackInfo]:

        stacks = {}

        for container in containers:
            if not container.compose_project:
                continue

            project = container.compose_project

            if project not in stacks:
                stacks[project] = StackInfo(
                    project=project,
                    working_dir=container.working_dir or "",
                    compose_file=container.compose_file or "",
                    containers=[]
                )

            stacks[project].containers.append(container)

        return list(stacks.values())
