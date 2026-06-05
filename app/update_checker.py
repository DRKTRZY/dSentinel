from app.models import UpdateInfo


class UpdateChecker:
    def check_stack(self, stack) -> UpdateInfo:
        return UpdateInfo(
            stack=stack.project,
            has_updates=False,
            containers=[
                container.name
                for container in stack.containers
            ],
        )
