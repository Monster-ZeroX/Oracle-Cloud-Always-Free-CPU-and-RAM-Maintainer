#!/usr/bin/env python3

import psutil
import threading
import time
import logging
import configparser

# Initialize logging
logging.basicConfig(
    filename='/var/log/cpu_maintainer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Read configuration
CONFIG_FILE = '/root/cpu_maintainer.conf'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

TARGET_CPU_MIN = int(config['CPU_SETTINGS']['TARGET_CPU_MIN'])  # Minimum CPU threshold
TARGET_CPU_MAX = int(config['CPU_SETTINGS']['TARGET_CPU_MAX'])  # Maximum CPU threshold
TARGET_RAM_USAGE = int(config['RAM_SETTINGS']['TARGET_RAM_USAGE'])  # Target RAM usage
CHECK_INTERVAL = int(config['SETTINGS']['CHECK_INTERVAL'])  # Interval in seconds

# Function to create adjustable CPU load
def create_cpu_load(stop_event):
    while not stop_event.is_set():
        # Busy work with short sleep to control load
        for _ in range(1000000):
            if stop_event.is_set():
                break
        time.sleep(0.01)  # Adjust sleep duration to fine-tune CPU usage

# Function to create artificial RAM load
def create_ram_load(ram_blocks):
    block_size = 10 * 1024 * 1024  # Each block is 10MB
    while len(ram_blocks) * block_size / (1024 ** 3) < TARGET_RAM_USAGE / 100 * psutil.virtual_memory().total / (1024 ** 3):
        ram_blocks.append(bytearray(block_size))  # Allocate memory
        time.sleep(0.1)

# Monitor and manage CPU and RAM usage
def maintain_resources():
    cpu_threads = []
    ram_blocks = []
    stop_events = []

    logging.info("Resource Maintainer Started")
    
    while True:
        # CPU monitoring
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"Current CPU Usage: {cpu_usage}%")
        
        if cpu_usage < TARGET_CPU_MIN and len(cpu_threads) < 5:  # Limit the number of threads
            logging.info("CPU usage below minimum. Adding CPU load...")
            stop_event = threading.Event()
            load_thread = threading.Thread(target=create_cpu_load, args=(stop_event,))
            load_thread.daemon = True
            load_thread.start()
            cpu_threads.append(load_thread)
            stop_events.append(stop_event)
        elif cpu_usage > TARGET_CPU_MAX and cpu_threads:
            logging.info("CPU usage above maximum. Reducing CPU load...")
            stop_event = stop_events.pop()
            stop_event.set()  # Stop the thread
            cpu_threads.pop()

        # RAM monitoring
        ram_usage = psutil.virtual_memory().percent
        logging.info(f"Current RAM Usage: {ram_usage}%")
        
        if ram_usage < TARGET_RAM_USAGE:
            logging.info("RAM usage below target. Adding RAM load...")
            create_ram_load(ram_blocks)
        elif ram_usage > TARGET_RAM_USAGE + 5:
            logging.info("RAM usage above target. Reducing RAM load...")
            if ram_blocks:
                ram_blocks.pop()  # Deallocate some memory
        
        # Sleep before next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    logging.info("Starting Resource Maintainer...")
    maintain_resources()
