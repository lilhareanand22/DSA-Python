
def contain_duplicate(nums):
    nums_set = set()
    
    for num in nums:
        if num in nums_set:
            return True
        
        nums_set.add(num)
        
    return False

def main():
    nums = [1,2,3,4]
    print(f"Does the array contain duplicate?: {contain_duplicate(nums)}")
    
    
if __name__ == "__main__":
    main()