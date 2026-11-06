

def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
        
         nums[slow], nums[fast] = nums[fast], nums[slow]
         
         slow += 1
         
def main():

    nums = [0, 1, 0, 3, 12]

    move_zeroes(nums)

    print("Result:", nums)


if __name__ == "__main__":
    main()