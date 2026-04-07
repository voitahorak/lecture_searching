import os
import json

# get current working directory path
cwd_path = os.getcwd()

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: list or None
    """

    file_path = os.path.join(cwd_path, file_name)

    # načtení JSON souboru
    with open(file_path, "r") as fileseq:
        data = json.load(fileseq)

    # ověření, že klíč existuje
    if field not in data:
        return None

    return data[field]

def linear_search(sequence, target):
    """
    Performs linear search in an unordered list.
    :param sequence: (list), list of numbers
    :param target: (int), searched number
    :return: dict with positions and count
    """

    positions = []

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)

    return {
        "positions": positions,
        "count": len(positions)
    }

def binary_search(sequence, target):
    """
    Performs binary search in a sorted list.
    :param sequence: (list), sorted list of numbers
    :param target: (int), searched number
    :return: index or None
    """

    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def pattern_search(sequence, pattern):
    """
    Searches for all occurrences of a pattern in a sequence.
    :param sequence: (str), DNA sequence
    :param pattern: (str), searched pattern
    :return: set of positions (indices)
    """

    positions = set()
    seq_len = len(sequence)
    pat_len = len(pattern)

    for i in range(seq_len - pat_len + 1):
        if sequence[i:i + pat_len] == pattern:
            positions.add(i)

    return positions


def main():
    dna_sequence = read_data("sequential.json", "dna_sequence")

    if dna_sequence is None:
        print("Neplatný klíč.")
        return

    pattern = "ATA"  # hledaný vzor

    result = pattern_search(dna_sequence, pattern)

    print("DNA sekvence:", dna_sequence)
    print("Hledaný vzor:", pattern)
    print("Pozice výskytu:", result)

if __name__ == "__main__":
    main()