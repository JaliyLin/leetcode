class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    L=[i,j]
                    print L
                    return L
        """
        k=0
        s=[]
        for i in range(len(nums)):
            if nums[i]==target/2:
                k+=1
                s.append(i)
        if k<=1:
            D={}
            for i in range(len(nums)):
                D[nums[i]]=i
            for j in range(len(nums)):
                if (target-nums[j])in D and D[target-nums[j]]>D[nums[j]]:
                    print [D[nums[j]],D[target-nums[j]]]
                    return [D[nums[j]],D[target-nums[j]]]
                    break
        else:
            print s
            return s