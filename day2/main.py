from utils import get_input_file_lines, get_input_file_path


def check_report_safety(report: list[int]) -> bool:
    first = report[0]
    second = report[1]
    if first == second:
        return False

    incresing_flag = first < second
    safe_diffs = [1, 2, 3] if incresing_flag else [-1, -2, -3]

    for i in range(len(report) - 1):
        first = report[i]
        second = report[i + 1]
        if first == second:
            return False

        pattern_check = first < second
        diff = second - first
        if not (pattern_check == incresing_flag and diff in safe_diffs):
            return False

    return True


def get_safe_reports_count(input_file_path: str) -> int:
    lines = get_input_file_lines(input_file_path)
    safety_flags: list[bool] = []
    for line in lines:
        sep = " "
        levels = line.split(sep)
        levels = list(map(lambda x: int(x), levels))
        safe_report = check_report_safety(report=levels)
        safety_flags.append(safe_report)

    return sum(safety_flags)


if __name__ == "__main__":
    in_file_path = get_input_file_path(module_file=__file__)
    result = get_safe_reports_count(input_file_path=in_file_path)
    print(f"Safe reports count: {result}")
