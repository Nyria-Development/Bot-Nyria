import subprocess


class ApiServer:
    @staticmethod
    def run_server():
        try:
            subprocess.run(["uvicorn", "api.api:Api", "--reload", "--log-level", "critical"])
        except KeyboardInterrupt:
            return
