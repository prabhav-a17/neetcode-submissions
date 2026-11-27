class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Ok so here we can use a stack add to the stack until we hit a "+", and then keep a running total 

        stack=[]
        
     

        for i in range(len(tokens)):
            if tokens[i]=="+":
                x=stack.pop()
                y=stack.pop()
                stack.append(x+y)

            elif tokens[i]=="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)

            elif tokens[i]=="/":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y/x))
            elif tokens[i]=="*":
                x=stack.pop()
                y=stack.pop()
                stack.append(x*y)
            else:
                stack.append(int(tokens[i]))

        return int(stack[-1])