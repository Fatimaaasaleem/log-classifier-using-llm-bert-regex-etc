import re

def classify_with_regex(log_message):
    # Regex patterns with their labels
    regex_patterns = {
        r"User User\d+ logged (in|out)\.": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully\.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully\.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }

    # Iterate over patterns
    for pattern, label in regex_patterns.items():
        # Use re.search to match anywhere in the string and ignore case
        if re.search(pattern, log_message, re.IGNORECASE):
            return label

    # Return a string, not a tuple
    return None


if __name__ == "__main__":
    test_logs = [
        "User User123 logged in.",
        "Backup started at 12:00.",
        "Backup completed successfully.",
        "System updated to version 1.0.0.",
        "File file1.txt uploaded successfully by user user1.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user user1.",
        "Hey Bro, chill ya!"
    ]

    for log in test_logs:
        print(f"{log} → {classify_with_regex(log)}")