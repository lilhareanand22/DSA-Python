

def two_sum(nums, target):
    
    num_map ={}
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
        
    return []


def main():

    nums = [2, 7, 11, 15]
    target = 26

    result = two_sum(nums, target)

    print("Two Sum Indices:", result)
    

if __name__ == "__main__":
    main()