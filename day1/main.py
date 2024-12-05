import os


def read_input(input_file_path: str) -> tuple[list[int], list[int]]:
    l1 = []
    l2 = []
    with open(input_file_path) as f:
        lines = f.readlines()
        for line in lines:
            sep = "  "
            elm1, elm2 = line.split(sep)
            l1.append(int(elm1))
            l2.append(int(elm2))
    return l1, l2


def calculate_diffs(l1: list[int], l2: list[int]) -> int:
    total_diff = 0
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    for i in range(len(l1_sorted)):
        total_diff += abs(l1_sorted[i] - l2_sorted[i])

    return total_diff


def caculate_similarity_score(l1: list[int], l2: list[int]) -> int:
    similarity_score = 0
    for elem in l1:
        similarity = l2.count(elem)
        elem_similarity_score = elem * similarity
        similarity_score += elem_similarity_score
    return similarity_score


if __name__ == "__main__":
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(current_file_path)
    list1, list2 = read_input(input_file_path=os.path.join(parent_directory, "input.txt"))
    result = calculate_diffs(l1=list1, l2=list2)
    print(f"Difference result: {result}")
    print("-------")
    total_similarity_score = caculate_similarity_score(l1=list1, l2=list2)
    print(f"Similarity score: {total_similarity_score}")
