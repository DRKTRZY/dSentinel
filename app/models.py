from dataclasses import dataclass


@dataclass
class ContainerInfo:
    name: str
    image: str
    image_id: str
    status: str

    compose_project: str | None = None
    compose_service: str | None = None
    working_dir: str | None = None
    compose_file: str | None = None

@dataclass
class StackInfo:
    project: str
    working_dir: str
    compose_file: str
    containers: list[ContainerInfo]

@dataclass
class UpdateInfo:
    stack: str
    has_updates: bool
    containers: list[str]
