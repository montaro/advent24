from typing import TypeAlias

from utils import get_input_file_lines, get_input_file_path

Level: TypeAlias = int
Report: TypeAlias = list[Level]


def check_report_safety(report: Report) -> bool:
    first = report[0]
    second = report[1]
    if first == second:
        return False

    increasing_flag = first < second
    safe_diffs = [1, 2, 3] if increasing_flag else [-1, -2, -3]

    for i in range(len(report) - 1):
        first = report[i]
        second = report[i + 1]
        if first == second:
            return False

        pattern_check = first < second
        diff = second - first
        if not (pattern_check == increasing_flag and diff in safe_diffs):
            return False

    return True


def get_all_reports(input_file_path: str) -> list[Report]:
    lines = get_input_file_lines(input_file_path)
    reports: list[Report] = []
    for line in lines:
        sep = " "
        levels = line.split(sep)
        levels = list(map(lambda x: int(x), levels))
        reports.append(levels)
    return reports


def get_safe_reports_count(input_file_path: str) -> int:
    reports = get_all_reports(input_file_path)
    safety_flags = list(map(check_report_safety, reports))
    return sum(safety_flags)


def get_report_variants(report: Report) -> list[Report]:
    """
    Get n report variants of the report, where each is the same report after removing one level
    """
    report_variants: list[Report] = []
    for i in range(len(report)):
        report_variant = report[:i] + report[i + 1 :]
        report_variants.append(report_variant)
    return report_variants


def get_safe_reports_count_with_dampener(input_file_path: str):
    reports = get_all_reports(input_file_path)
    safe_reports_count = 0
    for report in reports:
        if check_report_safety(report):
            safe_reports_count += 1
        else:
            # Get all report variants and check if any of them is a safe report
            report_variants = get_report_variants(report)
            for report_variant in report_variants:
                if check_report_safety(report=report_variant):
                    safe_reports_count += 1
                    break
    return safe_reports_count


if __name__ == "__main__":
    in_file_path = get_input_file_path(module_file=__file__)
    result = get_safe_reports_count(input_file_path=in_file_path)
    print(f"Safe reports count: {result}")
    print("------------------------------------")
    result_with_dampener = get_safe_reports_count_with_dampener(input_file_path=in_file_path)
    print(f"Safe reports count after the Problem Dampener : {result_with_dampener}")
