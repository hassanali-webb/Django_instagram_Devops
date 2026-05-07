import argparse
from scripts.docker_build import build_and_push
from scripts.terraform_apply import run_terraform
from scripts.k8s_deploy import deploy_k8s


def run_all():
    print("\nFULL PIPELINE STARTED\n")

    build_and_push()
    deploy_k8s()

    print("\nApp Deployment Completed (Docker + K8s)\n")


def run_infra():
    print("\nINFRASTRUCTURE STARTED\n")
    run_terraform()
    print("\nINFRASTRUCTURE COMPLETED\n")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--infra", action="store_true")
    parser.add_argument("--full", action="store_true")

    args = parser.parse_args()

    if not any(vars(args).values()):
        run_all()
        return

    if args.infra:
        run_infra()

    if args.full:
        run_infra()
        run_all()


if __name__ == "__main__":
    main()