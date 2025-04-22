from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            'test_case_basic_positive_numbers': ([1,2,3,4], [24,12,8,6]),
            'test_case_contains_zero': ([-1,1,0,3,3], [0,0,-9,0,0]),
            'test_case_all_ones': ([1,1,1,1], [1,1,1,1]),
            'test_case_all_zeros': ([0,0,0], [0,0,0]),
            'test_case_single_zero_in_array': ([2,4,0,8], [0,0,64,0]),
            'test_case_all_negative_numbers': ([-1,-2,-3,-4], [-24,-12,-8,-6]),
            'test_case_mixed_positives_and_negatives': ([3,-2,5,-1], [10,-15,6,-30]),
            'test_case_duplicates_in_array': ([2,3,2,4], [24,16,24,12]),
            'test_case_two_elements': ([5,6], [6,5])
        }
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_basic_positive_numbers(self):
        nums, output = self.__testcases['test_case_basic_positive_numbers']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_contains_zero(self):
        nums, output = self.__testcases['test_case_contains_zero']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))
    
    @timeout(0.5)
    def test_case_all_ones(self):
        nums, output = self.__testcases['test_case_all_ones']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_all_zeros(self):
        nums, output = self.__testcases['test_case_all_zeros']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_single_zero_in_array(self):
        nums, output = self.__testcases['test_case_single_zero_in_array']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_all_negative_numbers(self):
        nums, output = self.__testcases['test_case_all_negative_numbers']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_mixed_positives_and_negatives(self):
        nums, output = self.__testcases['test_case_mixed_positives_and_negatives']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_duplicates_in_array(self):
        nums, output = self.__testcases['test_case_duplicates_in_array']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_two_elements(self):
        nums, output = self.__testcases['test_case_two_elements']
        result = self.__solution.productExceptSelf(nums)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

if __name__ == '__main__': unittest.main()