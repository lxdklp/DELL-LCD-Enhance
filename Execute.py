import subprocess

def execute(cmd):
    info = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    info = info.stdout
    info = info.rstrip()
    return info