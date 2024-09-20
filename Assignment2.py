# Question 1:
# Give an algorithm to solve this problem: https://leetcode.com/problems/insertion-sort-list/
# Determine your algorithm's worst-case asymptotic running time.
# Describe a class of lists that realize this worst-case running time.

class Solution1:
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyStart = ListNode(0, head) #Define a dummy node to point to the head of the original list
        previous, current = head, head.next #Initialize previous and current pointers

        #Iterate through the list
        while current:
            if current.val >= previous.val: #If the current node is greater than or equal to the previous node, move to the next node
                previous, current = current, current.next
                continue

            i = dummyStart
            while current.val > i.next.val: #Find the correct position to insert the current node
                i = i.next

            previous.next = current.next
            current.next = i.next #Insert the current node
            i.next = current #Update the next pointer of the previous node to point to the current node
            current = previous.next #Move to the next node

        return dummyStart.next

# Worst-Case Asymptotic Running Time: O(n^2)
# Explanation: The outer while loop runs n times. The inner while loop iterates through the list 1+2+3+...+n-1 = n(n-1)/2 times.
# Which would sum up to O(n^2) in the worst-case scenario.

# Class of lists that realize this worst-case running time:
#   Lists that are sorted in descending order, as each new element must be compared with all previously sorted elements,
#   resulting in the algorithm taking the maximum number of comparisons and insertions.

# Question 2:
# Give an algorithm to solve this problem in O (lg n) time:
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Prove that your algorithm is correct with a loop invariant, showing initialization, maintenance, and termination.

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

# Loop Invariant:
#   If the minimum element is in nums, it will always be in num[left:right+1].

# Initialization:
#   At the start, nums[left:right+1] is the entire array. Trivial

# Maintenance:
#   Case 1: nums[mid] > nums[right]
#   We will search the right half of the array. This is because when rotating the array, the values on the left are greater than the values on the right.
#   If the min is in nums, it will be in nums[mid+1:] as nums[mid] is greater than nums[right].
#   By induction hypothesis, the minimum element is in nums[mid+1:].

#   Case 2: nums[mid] <= nums[right]
#   We will search the left half of the array. This is because since the middle value is less than or equal to the right value, the minimum value must be in the left half.
#   If the min is in nums, it will be in nums[left:mid] as nums[mid] is less than or equal to nums[right].
#   By induction hypothesis, the minimum element is in nums[left:mid].

# Termination:
#   Algorithm terminates when left == right, which will happen since search space is strictly decreasing in size.