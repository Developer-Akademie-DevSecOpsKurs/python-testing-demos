# print(calculate_days(None))
# print(calculate_days(False))
# print(calculate_days("2026-04-20"))
# print(calculate_days("2025-04-20"))
# print(calculate_days("2027-02-30"))
import datetime
import unittest

from app import calculate_days


class TestTimeCalculation(unittest.TestCase):

    def test_failure_calculate_days_with_wrong_input_type(self):
        # Arrange
        test_inputs = [123, 12.34, [], {}, (), False, None]

        # Act
        for test_input in test_inputs:
            with self.subTest(input=test_input):
                with self.assertRaises(AssertionError) as context:
                    calculate_days(test_input)
                self.assertEqual(str(context.exception), "Invalid input type")

    def test_failure_calculate_days_with_wrong_date_format(self):
        # Arrange
        test_input = "20.04.2026"
        # Act
        with self.assertRaises(AssertionError) as context:
            calculate_days(test_input)

        self.assertEqual(
            str(context.exception),
            "Invalid date format",
        )

    def test_failure_calculate_days_with_date_from_past(self):
        # Arrange
        test_input = "2026-04-20"
        # Act
        with self.assertRaises(ValueError) as context:
            calculate_days(test_input)

        self.assertEqual(str(context.exception), "Date cannot be in the past")

    def test_success_calculate_days_with_three_days_remaining(self):
        # Arrange
        current_date: datetime.date = datetime.date.today()
        time_delta_in_days: int = 3

        valid_input_date = str(
            current_date + datetime.timedelta(days=time_delta_in_days)
        )


        expected_result = time_delta_in_days

        # Act
        actual_result = calculate_days(valid_input_date)

        # Assert
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
