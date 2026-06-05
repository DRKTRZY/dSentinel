from app.docker_manager import DockerManager

docker = DockerManager()

for container in docker.get_containers():
    print(container)
