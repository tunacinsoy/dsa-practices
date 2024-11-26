"""

Description:
    Determine if a given array contains a subarray of at least two elements
    whose sum is a multiple of a specified number k.

    An array is considered to have a "good subarray"
    if there exists at least one subarray (consisting of two or more elements) such that
    the sum of the elements in this subarray is a multiple of k.

    For example:
    The array [23, 2, 4, 7] with k = 6 has a "good subarray" ([2, 4]),
    as the sum 6 is a multiple of k = 6.

    The array [5, 0, 0, 0] with k = 3 does not have any "good subarray",
    as no subarray of two or more elements sums to a multiple of 3.

Known Bugs:
    Input: [4,8], 6 should give True, however results in False
Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-11-26

Version:
    1.0.0

Algorithm Implementation:
  Hash using modulo operation

  input= [5,0,0,0]    ,       k = 3
    hash_map =
  {
    # mod = index
      2 = 0,
       = 1,
       = 2
  }

  input= [4, 2]    ,       k = 6
    hash_map =
  {
    # mod = index
      4 = 0,
      0 = 1,
       = 2
  }

   input= [4, 8]    ,       k = 6
    hash_map =
  {
    # mod = index
      4 = 0,
      0 = 1,
  }


  input= [4, 1, 1]    ,       k = 6 -> TRUE
    hash_map =
  {
    # mod = index
      4 = 0,
      5 = 1,
      0 = 2
  }

  input= [6]    ,       k = 6  -> FALSE
    hash_map =
  {
    # mod = index
      0 = 0,

  }

    input= [0,1,2,3]    ,       k = 2  -> TRUE
    hash_map =
  {
    # mod = index
      1 = 1
      0 = 3

  }

Complexities:
  Time: O(n)
  Space: O(n)
"""


def has_good_subarray(inputList: list[int], k: int) -> bool:

    if inputList is None:
        return False

    current_sum = 0
    remainder_index_map = {}

    MIN_GOOD_SUBARRAY_LIMIT = 2

    for index, value in enumerate(inputList):
        current_sum += value
        remainder = current_sum % k

        # print(f"Index {index}:{len(remainder_index_map)}")
        # Value of 0 does not contribute to our algorithm, and should be skipped
        if value == 0:
            continue
        if remainder == 0 and len(remainder_index_map) >= MIN_GOOD_SUBARRAY_LIMIT:
            return True
        if remainder not in remainder_index_map:
            remainder_index_map[remainder] = index
        elif index - remainder_index_map[remainder] >= MIN_GOOD_SUBARRAY_LIMIT:
            return True

    return False


assert has_good_subarray([23, 2, 4, 7], 6) == True
assert has_good_subarray([5, 0, 0, 0], 3) == False
assert has_good_subarray([], 1) == False
assert has_good_subarray([0, 0, 0, 0], 2) == False
assert has_good_subarray([1, 1, 0, 1], 2) == True
assert has_good_subarray([1, 0, 0, 1], 2) == False
assert has_good_subarray([1, 1, 1, 2], 6) == False
assert has_good_subarray([1, 0, 2, 3], 2) == True

print("All tests passed!")
