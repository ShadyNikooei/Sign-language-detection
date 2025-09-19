from datetime import datetime

def log_action(sign):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - Detected: {sign}\n")