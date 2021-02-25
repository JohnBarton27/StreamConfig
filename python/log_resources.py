# -*- coding: utf-8 -*-
import datetime
import logging
import psutil

logging.basicConfig(filename='resources.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

while True:
    # CPU % Utilization (by core)
    cpu_percents = psutil.cpu_percent(percpu=True, interval=1)

    # CPU temperature (by core)
    sensors_temps = psutil.sensors_temperatures()['coretemp'][1:]
    cpu_temps = []
    for sensor_temp in sensors_temps:
        cpu_temps.append(sensor_temp.current)

    # CPU Frequency (total)
    cpu_freq = int(psutil.cpu_freq().current)

    # % Memory usage
    memory_usage = psutil.virtual_memory().percent

    cpus_strs = []
    for i in range(0,5):
        cpus_strs.append(f'{cpu_percents[i]}% - {cpu_temps[i]}°C')

    cpus_str = " | ".join(cpus_strs)

    logging.info(f'CPU: {cpus_str} || CPU FREQ: {cpu_freq}MHz || MEMORY: {memory_usage}%')
