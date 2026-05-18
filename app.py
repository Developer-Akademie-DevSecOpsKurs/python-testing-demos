import argparse
import datetime


def calculate_days(target_date: str):
    # calc target_date - current_date
    try:
        # do not calculate day here,
        # pass it as an argument to this function instead.
        current_date = datetime.datetime.now()
        target_date: datetime = datetime.datetime.fromisoformat(target_date)

        if target_date < current_date:
            print("Date cannot be in the past")
            return False

        remaining_time = target_date - current_date

        return remaining_time.days
    except:
        print("Oh no something went wrong")
        return False
        # exit(1)


def cli_entrypoint():
    parser = argparse.ArgumentParser(
        description="Calculate remaining days until a target date."
    )
    parser.add_argument(
        "target_date",
        help="Target date in ISO format, e.g. 2026-04-20",
    )

    args = parser.parse_args()

    try:
        days = calculate_days(args.target_date)
        print(f"From today to {args.target_date} it is {days} full days remaining")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD (example: 2026-04-20).")


if __name__ == "__main__":
    cli_entrypoint()
