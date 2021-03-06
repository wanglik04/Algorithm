from typing import List
# 将字符原串分割成m份,题目让你将分割后的字符串的最大值最小,也就是max(list1,list2,list3...)最小



class Solution:
    def splitArray_BinarySearch(self, nums: List[int], m: int) -> int:
        def check(target: int) -> bool:
            """
            给你数组nums,给你目标值target
            让你按序把数组分成每个总值不超过目标值的子集,并且每个元素必须充分利用
            *子集数大于m,返回True
            """
            sum_check = 0
            num_of_subset = 1
            for i in nums:
                if sum_check + i <= target:
                    sum_check += i
                else:
                    sum_check = i
                    num_of_subset += 1
            return num_of_subset <= m

        min_result = max(nums)
        max_result = sum(nums)
        while max_result != min_result:
            mid = int((max_result - min_result) / 2 + min_result)
            if check(mid):
                max_result = mid
            else:
                min_result = mid + 1  # 或许这个+1就是二分查找的精髓所在
        return max_result

    def splitArray(self, nums: List[int], m: int) -> int:
        def rec_splitArray(nums: List[int], m: int):
            if (tuple(nums), m) in dp:
                return dp[(tuple(nums), m)]
            elif m == 1:
                dp[(tuple(nums), m)] = sum(nums)
                return sum(nums)
            elif m == len(nums):
                dp[(tuple(nums), m)] = max(nums)
                return max(nums)
            max_list = []
            for i in range(len(nums) - 1):
                if m - 1 > len(nums[i + 1:]):
                    break
                max_list.append(max(rec_splitArray(nums[:i + 1], 1), rec_splitArray(nums[i + 1:], m - 1)))
            dp[(tuple(nums), m)] = min(max_list)
            return min(max_list)

        dp = {}
        rec_splitArray(nums, m)
        return dp[(tuple(nums), m)]
        # return dp


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    m = 20  # 11
    # nums = [2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    # m = 12
    # nums = [10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    # m = 11

    nums1 = [499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479,
             478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458,
             457, 456, 455, 454, 453, 452, 451, 450, 449, 448, 447, 446, 445, 444, 443, 442, 441, 440, 439, 438, 437,
             436, 435, 434, 433, 432, 431, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 416,
             415, 414, 413, 412, 411, 410, 409, 408, 407, 406, 405, 404, 403, 402, 401, 400, 399, 398, 397, 396, 395,
             394, 393, 392, 391, 390, 389, 388, 387, 386, 385, 384, 383, 382, 381, 380, 379, 378, 377, 376, 375, 374,
             373, 372, 371, 370, 369, 368, 367, 366, 365, 364, 363, 362, 361, 360, 359, 358, 357, 356, 355, 354, 353,
             352, 351, 350, 349, 348, 347, 346, 345, 344, 343, 342, 341, 340, 339, 338, 337, 336, 335, 334, 333, 332,
             331, 330, 329, 328, 327, 326, 325, 324, 323, 322, 321, 320, 319, 318, 317, 316, 315, 314, 313, 312, 311,
             310, 309, 308, 307, 306, 305, 304, 303, 302, 301, 300, 299, 298, 297, 296, 295, 294, 293, 292, 291, 290,
             289, 288, 287, 286, 285, 284, 283, 282, 281, 280, 279, 278, 277, 276, 275, 274, 273, 272, 271, 270, 269,
             268, 267, 266, 265, 264, 263, 262, 261, 260, 259, 258, 257, 256, 255, 254, 253, 252, 251, 250, 249, 248,
             247, 246, 245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227,
             226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207, 206,
             205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185,
             184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164,
             163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143,
             142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122,
             121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101,
             100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75,
             74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48,
             47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
             20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    m1 = 50
    nums3 = [2, 16, 14, 15]
    m3 = 2  # 29
    nums2 = [1, 4, 4]
    m2 = 3  # 4
    # print(Solution().splitArray(nums,m))
    # print(Solution().splitArray(nums1, m1))
    # print(Solution().splitArray(nums3, m3))
    print(Solution().splitArray_BinarySearch(nums3, m3))
    print(Solution().splitArray_BinarySearch(nums1, m1))
    print(Solution().splitArray_BinarySearch(nums2, m2))
    # ddic=Solution().splitArray(nums,m)
    # for i,j in ddic.items():
    #     print(i,"\t\t",j)
