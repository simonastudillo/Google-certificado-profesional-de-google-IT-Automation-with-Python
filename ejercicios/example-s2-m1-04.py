#!/usr/bin/env python3
import shutil
import psutil

du = shutil.disk_usage("/")
print("Total: %d GiB" % (du.total / (2**30)))
print("Used: %d GiB" % (du.used / (2**30)))
print("Free: %d GiB" % (du.free / (2**30)))

cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage: %d%%" % cpu_usage)