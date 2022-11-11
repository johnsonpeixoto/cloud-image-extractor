#!/bin/bash

echo "Setting system environment..."
sudo apt update

echo "Install system requirements..."
sudo apt install python3 unzip python3-flask make 

echo "Install poetry..."
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/ubuntu/.local/bin:$PATH"
poetry --version

echo "Install AWS CLI..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

echo "Install Exiftool"
curl -L https://exiftool.org/Image-ExifTool-12.50.tar.gz > Image-ExifTool-12.50.tar.gz
gzip -dc Image-ExifTool-12.50.tar.gz | tar -xf -
cd Image-ExifTool-12.50
perl Makefile.PL
sudo make install
