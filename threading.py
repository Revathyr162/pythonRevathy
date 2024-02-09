import threading
import time

# Define a function that represents a task to be performed
def task(task_name, delay):
    print(f"{task_name} started")
    time.sleep(delay)  # Simulate some time-consuming task
    print(f"{task_name} completed")

# Define a list of tasks with their corresponding delays
tasks = [("Task 1", 2),
         ("Task 2", 3),
         ("Task 3", 1),
         ("Task 4", 4)]

# Create and start a thread for each task
threads = []
for task_name, delay in tasks:
    thread = threading.Thread(target=task, args=(task_name, delay))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed")
