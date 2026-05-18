
import argparse
import datetime
import re


def calculate_days(target_date: str) -> int:
    # calc target_date - current_date
    assert isinstance(target_date, str), "Invalid input type"
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", target_date), "Invalid date format"

    # do not calculate day here,
    # pass it as an argument to this function instead.
    current_date: datetime = datetime.date.today()
    target_date: datetime = datetime.date.fromisoformat(target_date)

    if target_date < current_date:
        raise ValueError("Date cannot be in the past")

    remaining_time = target_date - current_date

    return remaining_time.days



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
    except (AssertionError):
        print("Invalid date format. Use YYYY-MM-DD (example: 2026-04-20).")
    except (ValueError):
        print("Date cannot be in the past")
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)


if __name__ == "__main__":
    cli_entrypoint()
