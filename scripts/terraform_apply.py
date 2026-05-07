import subprocess
import os

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def run_terraform():
    print("\nRunning Terraform...\n")

    os.chdir("terraform")

    run("terraform init")
    run("terraform validate")
    run("terraform apply -auto-approve")

    os.chdir("..")

    print("\nTerraform Completed\n")