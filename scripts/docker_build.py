import subprocess

IMAGE = "hassanali1824/django-instagram:v3"

def run(cmd):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def build_and_push():
    print("\n🐳 Building Docker Image...\n")

    run(f"docker build -t {IMAGE} .")
    # run("docker login") # Assuming already logged in
    run(f"docker push {IMAGE}")

    print("\n✅ Docker Build & Push Done\n")
