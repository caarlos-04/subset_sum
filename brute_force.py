import sys


def findSubsets(arr, n, target, current, result):
    # Base case
    if target == 0:
        result.append(current[:])
        return

    # If tere are no elements left or the result is different return false
    if n == 0 or target < 0:
        return

    # Exlude last element
    findSubsets(arr, n - 1, target, current, result)

    # Include last element
    current.append(arr[n - 1])
    findSubsets(arr, n - 1, target - arr[n - 1], current, result)
    current.pop()


def getSubsetsWithSum(arr, target):
    result = []
    findSubsets(arr, len(arr), target, [], result)
    return result


def read_input_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

        target = int(lines[0].strip())

        nums = []
        for line in lines[1:]:
            nums += list(map(int, line.strip().split()))

        return target, nums

if __name__ == "__main__":

    target, nums = read_input_file(sys.argv[1])

    subsets = getSubsetsWithSum(nums, target)

    if subsets:
        print("There are", len(subsets), "subsets")
    else:
        print("No solutions found")

