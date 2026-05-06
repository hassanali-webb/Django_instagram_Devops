#!/bin/bash

apt update -y
apt install -y docker.io

systemctl start docker
systemctl enable docker

docker pull hassanali1824/instagram_clone:latest

docker run -d -p 8000:8000 hassanali1824/instagram_clone:latest