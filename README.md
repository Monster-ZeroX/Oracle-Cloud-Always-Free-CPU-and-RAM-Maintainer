# Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer
This script ensures your Oracle Cloud Always Free instance maintains a minimum CPU and RAM usage to avoid deactivation due to inactivity.
## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🔧 How It Works](#🤖-usage)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)

---

## 📍 Overview

❯ The **Oracle Cloud Always Free CPU and RAM Maintainer** is a lightweight utility designed to help users maintain their Always Free Oracle Cloud VPS by ensuring consistent resource usage. Oracle requires a minimum level of CPU and RAM utilization to keep the free tier instances active, and this project automates the process.

---

## 👾 Features

- Keeps CPU usage between 10-15%.
- Maintains RAM usage around 10%.
- Automatic setup and service management using `systemd`.

---

## 📁 Project Structure

```sh
└── Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/
    ├── LICENSE
    ├── README.md
    ├── cpu_maintainer.conf
    ├── cpu_maintainer.py
    └── install.sh
```
---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python, Shell


### ⚙️ Installation

Install Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer using one of the following methods:

### 🖥Automatic Installation 

1. Clone the Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer repository:
```sh
git clone https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer
```

2. Navigate to the project directory:
```sh
cd Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer
```

3. Run the installer:
```sh
sudo ./install.sh
```
4. Monitor the service:
```sh
sudo systemctl status cpu_maintainer
```
5. Check the logs for usage information:
```sh
tail -f /var/log/cpu_maintainer.log
```

### 🧩Manual Installation 

1. Install the Python dependency psutil:

```sh
pip3 install psutil
```
2. Copy the script and configuration file to the /root directory:

```sh
sudo cp cpu_maintainer.py /root/cpu_maintainer.py
sudo cp cpu_maintainer.conf /root/cpu_maintainer.conf
sudo chmod +x /root/cpu_maintainer.py
```
3. Run the script manually:

```sh
sudo python3 /root/cpu_maintainer.py
Stop the script by terminating the process manually:
```
4. Stop the script by terminating the process manually:
```sh
ps aux | grep cpu_maintainer.py
kill <PID>
```
### 🔧 How It Works
- CPU Usage Monitoring: The script dynamically spawns threads to simulate CPU activity when usage falls below the specified threshold and removes them when it exceeds the upper limit.
- RAM Usage Simulation: Allocates memory blocks to maintain a consistent RAM usage target.
- Configuration File: Users can customize thresholds and check intervals via a .conf file.
- Systemd Integration: Ensures the script runs automatically on boot and restarts if it fails.


## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/issues)**: Submit bugs found or log feature requests for the `Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer` project.
- **💡 [Submit Pull Requests](https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/pulls)**: Review open PRs, and submit your own PRs.



---

## 🎗 License

This project is protected under the [GPL-3.0 license](https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/tree/main?tab=GPL-3.0-1-ov-file#) License. For more details, refer to the [LICENSE](https://github.com/Monster-ZeroX/Oracle-Cloud-Always-Free-CPU-and-RAM-Maintainer/tree/main?tab=GPL-3.0-1-ov-file#) file.

---
