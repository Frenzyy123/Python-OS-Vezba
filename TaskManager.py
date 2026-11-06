import time
import psutil

processes = list(psutil.process_iter(['name', 'memory_percent', 'cpu_percent']))

for process in processes:
    try:
        process.cpu_percent(interval=None)
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

time.sleep(2)

print(f"{'Name':<25}{'Memory':<15}{'CPU':<10}")

for process in processes:
    try:
        print(
            f"{process.name():<25}"
            f"{process.memory_percent():<15.2f}"
            f"{process.cpu_percent(interval=None):<10.2f}"
        )
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

print(f"Total CPU usage: {psutil.cpu_percent(interval=1)}")
print(f"Number of physical CPU cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical CPU cores: {psutil.cpu_count(logical=True)}")
print(f"Number of threads in current process: {psutil.Process().num_threads()}")