def max_value(nums: list[float]) -> float:
    """ Return the larget value in nums. 0(n) time, O(1) space"""
    if not nums:
        raise ValueError("max_value() arg is an empty list")
    
    maximum = float("-inf")
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum


if __name__ == "__main__":
    print(max_value([2,-33,11,1000]))