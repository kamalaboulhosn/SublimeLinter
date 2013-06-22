import re

from base_linter import BaseLinter, INPUT_METHOD_FILE

CONFIG = {
    'language': 'csharp',
    'executable': 'mcs',
    'test_existence_args': ['--help'],
    'lint_args': ['--parse', '{filename}'],
    'input_method': INPUT_METHOD_FILE,
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match('^.+\((?P<line>\d+),\d+\): error .+: (?P<error>.+)', line)
            print line
            if match:
                error, line = match.group('error'), match.group('line')
                self.add_message(int(line), lines, error, errorMessages)
