import re

from utils import get_input_file_lines, get_input_file_path


def get_all_correct_pattern_matches_results(text: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches: list[tuple[int, int]] = re.findall(pattern=pattern, string=text)
    total = 0
    for match in matches:
        arg1 = int(match[0])
        arg2 = int(match[1])
        total += arg1 * arg2
    return total


if __name__ == "__main__":
    in_file_path = get_input_file_path(module_file=__file__)
    lines = get_input_file_lines(input_file_path=in_file_path)
    input_text = "".join(lines)
    result = get_all_correct_pattern_matches_results(text=input_text)
    print(f"Total valid multiplications sum: {result}")
