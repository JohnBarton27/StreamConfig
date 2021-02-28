# -*- coding: utf-8 -*-
# To run automatically, add a cron job by running 'crontab -e' and adding the following line:
#    @reboot <PATH_TO_STREAMCONFIG>/python/log_resources.py &
import datetime
import logging
from logging.handlers import RotatingFileHandler
import psutil

logger = logging.getLogger('Rotating Resource Log')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('/var/log/resources.log', maxBytes=50000, backupCount=5)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('================RESTART================')

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
    for i in range(0,6):
        cpus_strs.append(f'{cpu_percents[i]}% - {cpu_temps[i]}°C')

    cpus_str = " | ".join(cpus_strs)

    logger.info(f'CPU: {cpus_str} || CPU FREQ: {cpu_freq}MHz || MEMORY: {memory_usage}%')
