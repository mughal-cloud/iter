from unittest import TestCase
from iter import iter_commands

class IterTestCase(TestCase):

    def setUp(self):
        self.example_script = '''
# Get all users
SELECT * FROM users;

# Get all users with similar interests
SELECT * FROM
    users
WHERE interest IN ("robotics", "jui jitsu", "music");
        '''
        self.expected_line_numbers = [3, 8]
        self.expected_command_start_lines = [1, 4]
        self.expected_command_numbers = [1, 2]
        self.expected_commands = [
            '\nSELECT * FROM users;',
            '\nSELECT * FROM\n    users\nWHERE interest IN ("robotics", "jui jitsu", "music");'
        ]

    def tearDown(self):
        pass

    def test_line_numbers(self):
        zipped_object = zip(iter_commands(self.example_script), self.expected_line_numbers)
        for item, expected_line_number in zipped_object:
            line_number = item[0]
            self.assertEqual(line_number, expected_line_number)

    def test_command_start_lines(self):
        zipped_object = zip(iter_commands(self.example_script), self.expected_command_start_lines)
        for item, expected_command_start_line in zipped_object:
            command_start_line = item[1]
            self.assertEqual(command_start_line, expected_command_start_line)

    def test_command_numbers(self):
        zipped_object = zip(iter_commands(self.example_script), self.expected_command_numbers)
        for item, expected_command_number in zipped_object:
            command_number = item[2]
            self.assertEqual(command_number, expected_command_number)

    def test_commands(self):
        zipped_object = zip(iter_commands(self.example_script), self.expected_commands)
        for item, expected_command in zipped_object:
            command = item[3]
            self.assertEqual(command, expected_command)
