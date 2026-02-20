# Starter file for Exercise 4: Copilot Chat Skills
# Use this file to practice slash commands and chat variables.
# Run this file with: python3 exercises/04-copilot-chat-skills/starter.py


def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(calculate_average([10, 20, 30, 40]))
    print(find_duplicates([1, 2, 3, 2, 4, 3]))
    print(flatten([1, [2, 3], [4, [5, 6]]]))
