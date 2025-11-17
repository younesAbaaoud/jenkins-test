from pathlib import Path

def load_numbers(path):
    with open(path, "r", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]

def sum_numbers(nums):
    return sum(nums)

script_dir = Path(__file__).parent

file_path = script_dir / "numbers.txt"

numbers  =load_numbers(file_path)

print(sum_numbers(numbers))

