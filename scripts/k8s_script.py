import subprocess

K8S_DIR = "./k8s"

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def deploy_k8s():
    print("\nDeploying Kubernetes Resources...\n")

    run(f"kubectl apply -f {K8S_DIR}/namespace.yaml")
    run(f"kubectl apply -f {K8S_DIR}/configmap.yaml")
    run(f"kubectl apply -f {K8S_DIR}/secret.yaml")
    run(f"kubectl apply -f {K8S_DIR}/deployment.yaml")
    run(f"kubectl apply -f {K8S_DIR}/service.yaml")
    run(f"kubectl apply -f {K8S_DIR}/hpa.yaml")

    print("\nChecking status...\n")
    run("kubectl get pods -n dev")
    run("kubectl get svc -n dev")

    print("\nKubernetes Deployment Done\n")