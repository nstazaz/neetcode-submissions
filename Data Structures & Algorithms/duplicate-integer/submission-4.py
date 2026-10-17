class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
      t=len(nums)
      x=0
      h=1
      h0=0
      h2=t-1
      while h<t :
       if nums[x]==nums[h] :
          return True
       if x>0 and nums[x]==nums[h0]:
        return True
       if nums[x]==nums[h2]:
        return True
       else :
            x+=1
            h+=1
         
         
      return False
      
        

        