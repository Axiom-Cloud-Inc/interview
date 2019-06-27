"""
inputs:
Follow this convention

YYYY-MM-DD-H-M-S
timestamp  -> str

Make sure that this a valid timezone --> dont do this catch the exception
timezone  -> str

output
epoch time stamp since 1970
"""

from pytz import timezone
import datetime
import sys


def create_epoch_timestamp(timestamp, given_timezone):
    pattern = "%Y-%m-%d %H:%M:%S"
    try:
        datetime_object = datetime.datetime.strptime(timestamp, pattern)
        zone = timezone(given_timezone)
    except Exception as e:
        raise ValueError(e)
    local_dt = zone.localize(datetime_object)
    return int(local_dt.timestamp())


def main():
    if len(sys.argv) > 3:
        print("Too many arguments  .py [timestamp ] [timezone]")
        sys.exit(-1)
    timestamp = sys.argv[1]
    timezone = sys.argv[2]
    print(create_epoch_timestamp(timestamp, timezone))


if __name__ == "__main__":
    main()
