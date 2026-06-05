import docker

from app.models import ContainerInfo


class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def get_containers(self) -> list[ContainerInfo]:
        result = []

        for container in self.client.containers.list():
            labels = container.labels

            result.append(
                ContainerInfo(
                    name=container.name,
                    image=container.image.tags[0]
                    if container.image.tags
                    else "<unknown>",
                    status=container.status,
                    compose_project=labels.get(
                        "com.docker.compose.project"
                    ),
                    compose_service=labels.get(
                        "com.docker.compose.service"
                    ),
                    compose_file=labels.get(
                        "com.docker.compose.project.config_files"
                    ),
                    working_dir=labels.get(
                        "com.docker.compose.project.working_dir"
                    ),
                )
            )

        return result
