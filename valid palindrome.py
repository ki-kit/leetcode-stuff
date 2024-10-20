class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # turn everything to lowercase first
        s = s.lower()

        #print(s)
        
        # break the string into an array where each array element is a single letter
        # step 1 - creating the array
        y = list(s)
        
        # step 2 - remove unwanted characters (spaces and punctuation)
            # using list comprehension - output a char that doesnt have any punctuation/spaces
                # there is a function for alphanumerics so if the char is
                # alphanumeric it will be added to the cleaned_y
        cleaned_y = [char for char in y if char.isalnum() ]

        #print(cleaned_y)

        for i in range(0,len(cleaned_y)//2): # check the first half of the string if its the same as the second half
            if cleaned_y[i]!=cleaned_y[len(cleaned_y)-(1+i)]:
                return False
        return True

s = "A man, a plan, a canal: Panama"