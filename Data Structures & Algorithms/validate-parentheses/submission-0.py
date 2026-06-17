class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            elif char == ')' or char == ']' or char == '}':

                 if not stack: return False
            #no opening bracket
                 top = stack[-1]
                 if ((char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '[')):
                    return False
                
            # Pop matching opening bracket
                 stack.pop() 
            
    # Balanced if stack is empty
        return not stack
            
            

        