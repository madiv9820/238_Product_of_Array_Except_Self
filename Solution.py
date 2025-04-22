from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 🎯 totalProduct: holds the product of all non-zero numbers
        # 💣 zeroCount: tracks how many zero bombs we’ve got in the array
        totalProduct, zeroCount = 1, 0

        # 🔍 First loop: Find the product of all non-zero numbers and count the zeros
        for num in nums: 
            if num != 0: totalProduct *= num  # 💪 Multiply as long as the number isn’t zero
            else: zeroCount += 1  # 💥 Count that sneaky zero

        # 🛠️ Second loop: Construct the result array based on zero logic
        for index in range(len(nums)):
            if nums[index] == 0:
                # 💡 If we have exactly one zero, that index gets the product of the non-zeros
                # 🚫 More than one zero? Everyone gets a big fat zero.
                nums[index] = totalProduct if zeroCount < 2 else 0
            else:
                # 🙅 If there's any zero in the array, all non-zero elements become 0
                # ✅ If not, divide the total product by the current value
                nums[index] = totalProduct // nums[index] if not zeroCount else 0

        return nums  # 🚀 Return the transformed array, mission complete!
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([-1,1,0,3,3]))