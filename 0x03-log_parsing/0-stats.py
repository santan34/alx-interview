#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display stats.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regex pattern to match the log format
    regex = re.compile(
        r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [
                200,
                301,
                400,
                401,
                403,
                404,
                405,
                500]}}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(2)
                file_size = int(match.group(3))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency if it's a recognized status code
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Output every 10 lines
                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        pass
    finally:
        output(log)
