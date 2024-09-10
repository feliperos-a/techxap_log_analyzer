import re

def analyze_logs(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return
    
    errors = [log for log in logs if "ERROR" in log]
    
    print(f"Total logs: {len(logs)}")
    print(f"Total errors: {len(errors)}")
    for error in errors:
        print(error.strip())

if __name__ == "__main__":
    log_file = "security_logs.txt"
    analyze_logs(log_file)
