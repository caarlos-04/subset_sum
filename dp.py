import sys


def isSubsetSumRec(arr, n, sum, memo):
    if sum == 0:
        return True
    if n <= 0:
        return False
    if memo[n][sum] != -1:
        return memo[n][sum]
    if arr[n - 1] > sum:
        memo[n][sum] = isSubsetSumRec(arr, n - 1, sum, memo)
    else:
        memo[n][sum] = (isSubsetSumRec(arr, n - 1, sum, memo)
                        or isSubsetSumRec(arr, n - 1, sum - arr[n - 1], memo))
    return memo[n][sum]


def buildSubsets(arr, n, sum, memo, path, result):
    if sum == 0:
        result.append(path[:])
        return
    if n == 0 or sum < 0:
        return

    # Exclude current element
    if memo[n - 1][sum]:
        buildSubsets(arr, n - 1, sum, memo, path, result)

    # Include last element if possible
    if sum - arr[n - 1] >= 0 and memo[n - 1][sum - arr[n - 1]]:
        path.append(arr[n - 1])
        buildSubsets(arr, n - 1, sum - arr[n - 1], memo, path, result)
        path.pop()


def isSubsetSum(arr, sum):
    n = len(arr)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]

    exists = isSubsetSumRec(arr, n, sum, memo)

    subsets = []
    if exists:
        buildSubsets(arr, n, sum, memo, [], subsets)
    return subsets



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

    subsets = isSubsetSum(nums, target)

    if subsets:
        print("There are", len(subsets), "subsets")
    else:
        print("No solutions found")
