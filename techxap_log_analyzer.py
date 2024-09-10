# techxap_log_analyzer.py
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
    print("Error details:")
    for error in errors:
        print(error.strip())

    # Additional summary functionality
    error_summary = {}
    for log in errors:
        error_type = re.search(r"ERROR: (.*)", log)
        if error_type:
            error_type = error_type.group(1)
            error_summary[error_type] = error_summary.get(error_type, 0) + 1
    
    print("Error summary:")
    for error_type, count in error_summary.items():
        print(f"{error_type}: {count} times")

if __name__ == "__main__":
    log_file = "security_logs.txt"  # Path to the log file
    analyze_logs(log_file)
