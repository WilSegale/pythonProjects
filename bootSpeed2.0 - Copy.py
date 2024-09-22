import time

def boot_speed_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        boot_speed = end_time - start_time
        print(f"Boot speed: {boot_speed} seconds")
        return result
    return wrapper

@boot_speed_decorator
def main():
    # Your program code goes here
    time.sleep(2)  # Simulating a delay of 2 seconds for demonstration purposes

if __name__ == "__main__":
    main()


