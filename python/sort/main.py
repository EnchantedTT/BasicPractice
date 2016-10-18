from quick import Quicksort
from bubble import BubbleSort

def is_sorted(numbers):
    last_num = float("-inf")

    for num in numbers:
        if num < last_num:
            return False
        else:
            last_num = num

    return True

def contain_same_ints(arr1, arr2):
    for i in arr1:
        found = False
        for j in arr2:
            if i == j:
                found = True
        if not found:
            return False

    return True

def main():
    original = [11, 2131, -123, 65, -35, 657, -2434]

    numbers = original[:]

    qs = Quicksort(numbers)
    output = qs.sort()

    bs = BubbleSort(numbers)
    output_bs = bs.sort()

    if is_sorted(output):
        print("** SUCCESS! **")
    else:
        print("Uh oh - not in order.")

    if contain_same_ints(original, numbers):
        print("** Contain the same elements! **")
    else:
        print("Uh oh - something is missing.")

    print(output)

    if is_sorted(output_bs):
        print("** SUCCESS! **")
    else:
        print("Uh oh - not in order.")

    if contain_same_ints(original, numbers):
        print("** Contain the same elements! **")
    else:
        print("Uh oh - something is missing.")

    print(output_bs)


if __name__ == "__main__":
    main()