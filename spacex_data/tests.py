from datetime import datetime
from django.test import TestCase
from .utils import fetch_spacex_launches, categorize_launches, convert_unix_to_ymd

class SpaceXTests(TestCase):
    def test_fetch_spacex_launches(self):
        # Test whether fetch_spacex_launches returns a valid response
        response = fetch_spacex_launches()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)

    def test_categorize_launches(self):
        # Prepare test data
        test_launches = [
            {'success': True, 'upcoming': False},
            {'success': False, 'upcoming': False},
            {'success': True, 'upcoming': True},
        ]
        categorized = categorize_launches(test_launches)

        # Check if categorization is done correctly
        self.assertIn('successful', categorized)
        self.assertIn('failed', categorized)
        self.assertIn('upcoming', categorized)
        self.assertIsInstance(categorized['successful'], list)
        self.assertIsInstance(categorized['failed'], list)
        self.assertIsInstance(categorized['upcoming'], list)

    def test_convert_unix_to_ymd(self):
        # Prepare test data
        test_launches = {
            'successful': [
                {'date_unix': 1640995200},
            ]
        }
        convert_unix_to_ymd(test_launches)

        # Check if conversion is done correctly
        for launch in test_launches.values():
            for launch_detail in launch:
                self.assertIsInstance(launch_detail['date_unix'], datetime)
