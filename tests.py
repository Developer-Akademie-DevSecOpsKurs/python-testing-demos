# print(calculate_days(None))
# print(calculate_days(False))
# print(calculate_days("2026-04-20"))
# print(calculate_days("2025-04-20"))
# print(calculate_days("2027-02-30"))
import datetime
import unittest

from app import calculate_days


class TestTimeCalculation(unittest.TestCase):

    def test_failure_calculate_days_with_missing_input(self):
        # AAA Pattern => Arrange, Act, Assert
        # Arrange
        test_input = None
        expected_result = False

        # Act
        result = calculate_days(test_input)

        # Assert
        self.assertEqual(result, expected_result)
        self.assertFalse(result)

    def test_failure_calculate_days_with_wrong_input_type(self):
        # Arrange
        test_input = False
        expected_result = False
        # Act
        result = calculate_days(test_input)
        # Assert
        self.assertEqual(result, expected_result)
        self.assertFalse(result)
    
    def test_failure_calculate_days_with_date_from_past(self):
        # Arrange
        test_input = "2026-04-20"
        expected_result = False
        # Act
        result = calculate_days(test_input)
        # Assert
        self.assertEqual(result, expected_result)
        self.assertFalse(result)

    def test_success_calculate_days_with_three_days_remaining(self):
        # Arrange
        current_date = datetime.datetime.now()
        time_delta_in_days = 3

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