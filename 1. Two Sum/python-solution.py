# Solution
def two_sum(nums: list[int], target: int) -> list[int]:
	complements: dict[int, int] = {}
	for i, num in enumerate(nums):
		complement: int = target - num
		if complement in complements:
			return [complements[complement], i]
		complements[num] = i


# Tests
assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Failed Example-1"
assert two_sum([3, 2, 4], 6) == [1, 2], "Failed Example-2"
assert two_sum([3, 3], 6) == [0, 1], "Failed Example-3"
