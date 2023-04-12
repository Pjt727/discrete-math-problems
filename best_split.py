from itertools import combinations
from itertools import chain, combinations

# itertools recipe to get the powerset
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# This is a brute force algorithm which generates all possible combinations of the nums in nums.
#   - I think the complexity of this algorithm is O(n * 2^n) for generating the powset and adding all the subsets
# This is already a little wasteful because we do not really need to consider a subset if we already considered
#   the subset which forms a partition with the considered subset...
#   For instance if the original nums is {1,2,3} then two subsets would be {1} and {2, 3},
#   if we already considered {1} we would not need to consider {2, 3} because we already know they both have the
#   same difference from the half the sum  (1+2+3 = 6 // 3 | 3-(1) = 2 and abs(3 - (3+2))= 2)
#   There might be an an easy way to change the powerset implementation to eliminate these duplications, but
#   to eliminate all of these subsets that sum to the same difference would probably be more work than what its worth
#   Therefore, we might be able to change the time complexity to O( n*2^(n-1) )
# Finally, there might be a greedy solution which preforms better
def split_to_minimize_difference( nums: list[int]) -> tuple[tuple[int], tuple[int]]:
    powset: list[list[int]] = powerset(nums)
    target: int = sum(nums) // 2
    best_subset_score: float = float('inf') #we want to minimize score
    best_subset: tuple[int] = ()

    for subset in powset:
        score = abs(sum(subset) - target)
        if score < best_subset_score:
            best_subset_score = score
            best_subset = subset
            if best_subset_score == 0:
                break
    
    # copying the list so the deletion does not happen to the original list
    c_nums = nums.copy()
    for num in best_subset:
        c_nums.remove(num)

    return best_subset, tuple(c_nums)


if __name__ == "__main__":
    school_counts: list[int] = [100,500,200,300,700,200]
    print(split_to_minimize_difference(school_counts))
    