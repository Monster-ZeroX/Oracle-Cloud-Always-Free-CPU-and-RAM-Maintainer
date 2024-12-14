#!/bin/bash

# Auto Installer for Resource Maintainer

echo "Installing dependencies and setting up the Resource Maintainer..."

# Update and install Python3 if not available
if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Installing Python3..."
    sudo apt update && sudo apt install -y python3 python3-pip
else
    echo "Python3 is already installed."
fi

# Install psutil
echo "Installing Python dependency: psutil..."
pip3 install psutil

# Copy script and configuration files to /root
echo "Copying script and configuration files..."
sudo cp cpu_maintainer.py /root/cpu_maintainer.py
sudo cp cpu_maintainer.conf /root/cpu_maintainer.conf
sudo chmod +x /root/cpu_maintainer.py

# Create systemd service file
SERVICE_FILE="/etc/systemd/system/cpu_maintainer.service"
echo "Creating systemd service file..."
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=CPU and RAM Resource Maintainer
After=network.target

[Service]
ExecStart=/usr/bin/python3 /root/cpu_maintainer.py
Restart=always
User=root
WorkingDirectory=/root

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd and enable the service
echo "Enabling and starting the cpu_maintainer service..."
sudo systemctl daemon-reload
sudo systemctl enable cpu_maintainer
sudo systemctl start cpu_maintainer

# Check the status of the service
echo "Installation complete. Checking service status..."
sudo systemctl status cpu_maintainer
