import subprocess

K8S_DIR = "./k8s/manifest"

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def deploy_k8s():
    print("\nDeploying Kubernetes Resources...\n")

    run(f"kubectl apply -f {K8S_DIR}/namespace.yml")
    run(f"kubectl apply -f {K8S_DIR}/configmap.yml")
    run(f"kubectl apply -f {K8S_DIR}/postgres.yml")
    run(f"kubectl apply -f {K8S_DIR}/redis.yml")
    run(f"kubectl apply -f {K8S_DIR}/deployment.yml")
    run(f"kubectl apply -f {K8S_DIR}/services.yml")

    print("\nChecking status...\n")
    run("kubectl get pods -n dev")
    run("kubectl get svc -n dev")

    print("\nKubernetes Deployment Done\n")
