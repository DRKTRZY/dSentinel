from dataclasses import dataclass

@dataclass
class ContainerInfo:
    name: str
    image: str
    status: str

    compose_project: str | None = None
    compose_service: str | None = None
    working_dir: str | None = None
    compose_file: str | None = None
