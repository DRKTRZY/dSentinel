import subprocess


class UpdateChecker:
    def check_stack(self, stack):
        result = subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                stack.compose_file,
                "pull",
                "--quiet",
            ],
            capture_output=True,
            text=True,
        )

        return result.returncode == 0
