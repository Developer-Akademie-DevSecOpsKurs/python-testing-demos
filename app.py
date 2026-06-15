import argparse
import datetime
import re


def _validate_date_inputs(target_date: str | None):
    assert isinstance(target_date, str), "Invalid input type"
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", target_date), "Invalid date format"


def calculate_weeks(target_date: str) -> float:
    # TODO: implement this
    _validate_date_inputs(target_date)

    current_date: datetime.date = datetime.date.today()
    target_date: datetime.date = datetime.date.fromisoformat(target_date)

    remaining_time_in_days = (target_date - current_date)

    remaining_time_weeks = remaining_time_in_days.total_seconds() / 60 / 60 / 24 / 7

    return normalize_time_output(remaining_time_weeks)


def calculate_days(target_date: str) -> int:
    _validate_date_inputs(target_date)

    current_date: datetime.date = datetime.date.today()
    target_date: datetime.date = datetime.date.fromisoformat(target_date)

    if target_date < current_date:
        raise ValueError("Date cannot be in the past")

    remaining_time = target_date - current_date

    return remaining_time.days


def calculate_hours(target_date: str) -> float:
    _validate_date_inputs(target_date)

    current_date: datetime.date = datetime.date.today()
    target_date: datetime.date = datetime.date.fromisoformat(target_date)

    remaining_time_in_days = (target_date - current_date)

    remaining_time_hours = remaining_time_in_days.total_seconds() / 60 / 60

    return normalize_time_output(remaining_time_hours)


def calculate_seconds(target_date: str) -> float:
    _validate_date_inputs(target_date)

    current_date: datetime.date = datetime.date.today()
    target_date: datetime.date = datetime.date.fromisoformat(target_date)

    remaining_time_in_days = (target_date - current_date)

    return normalize_time_output(remaining_time_in_days.total_seconds())


def normalize_time_output(raw_time: float) -> str:
    return "{:.2f}".format(round(raw_time, 2))


def cli_entrypoint():
    parser = argparse.ArgumentParser(
        description="Calculate remaining days until a target date."
    )
    parser.add_argument(
        "target_date",
        help="Target date in ISO format, e.g. 2026-04-20",
    )
    parser.add_argument(
        "-o",
        "--output-format",
        choices=["seconds", "hours", "weeks"],
        help="Can be used to specify time output format. Defaults to full days"
    )

    args = parser.parse_args()

    try:
        unit = "days"
        if args.output_format:
            if args.output_format == "seconds":
                result = calculate_seconds(args.target_date)
                unit = "seconds"
            if args.output_format == "hours":
                result = calculate_hours(args.target_date)
                unit = "hours"

            if args.output_format == "weeks":
                result = calculate_weeks(args.target_date)
                unit = "weeks"
        else:
            result = calculate_days(args.target_date)

        print(f"From today to {args.target_date} it is {result} {unit} remaining")  # noqa: E501
    except AssertionError:
        print("Invalid date format. Use YYYY-MM-DD (example: 2026-04-20).")
    except ValueError:
        print("Date cannot be in the past")
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)


if __name__ == "__main__":
    cli_entrypoint()
