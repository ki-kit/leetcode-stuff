class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """   
        # find how many digits there are in the original array
        lenght=len(digits)
        
        #print(lenght)

        # +1 calculator - cycle goes from the last element to the 1st one
        for i in range(lenght-1,-1,-1):
            
            # if the integer doesnt contain 9
            if digits[i]<9: # if the current digit is less then9 we will increment it by 1
                digits[i]+=1 
                return digits
            digits[i] = 0   # else the digit will be set to 0
         
        # boundary conditions for when the integer consists of only 9s
        return [1] + digits        

#initialise the class
solution = Solution()

# original array
digits=[5,8,1,0]

# result
print(solution.plusOne(digits))


