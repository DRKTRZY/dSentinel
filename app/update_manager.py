import subprocess


class UpdateManager:
    def update_stack(self, stack):
        print(f"Updating {stack.project}")

        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                stack.compose_file,
                "pull",
            ]
        )

        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                stack.compose_file,
                "up",
                "-d",
            ]
        )
