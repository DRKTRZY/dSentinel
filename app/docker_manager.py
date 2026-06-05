import docker

from app.models import ContainerInfo


class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def get_containers(self) -> list[ContainerInfo]:
        containers = []

        for container in self.client.containers.list():
            labels = container.labels

            containers.append(
                ContainerInfo(
                    name=container.name,
                    image=container.image.tags[0]
                    if container.image.tags
                    else "<unknown>",
                    image_id=container.image.id,
                    status=container.status,
                    compose_project=labels.get(
                        "com.docker.compose.project"
                    ),
                    compose_service=labels.get(
                        "com.docker.compose.service"
                    ),
                    working_dir=labels.get(
                        "com.docker.compose.project.working_dir"
                    ),
                    compose_file=labels.get(
                        "com.docker.compose.project.config_files"
                    ),
                )
            )

        return containers
