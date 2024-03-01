import subprocess

from fastapi import FastAPI

app = FastAPI()


def execute(command):
    return subprocess.run(command.split(" "), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@app.get("/docker")
def docker_status():
    result = execute("sh /etc/rc.d/rc.docker status")
    return {"stdout": result.stdout.decode("utf-8"), "stderr": result.stderr.decode("utf-8")}
