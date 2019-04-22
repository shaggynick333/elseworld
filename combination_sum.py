class CombinationSum:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        res=set()
        intermedia=[]
        self.recursion(candidates,target,res,intermedia)
        return [list(i) for i in res]
 
    def recursion(self,candidates,target,res,intermedia):
        for i in candidates:
            if target==i:
                temp=intermedia+[i]
                temp.sort()
                if temp is not None:
                    res.add(tuple(temp))
                return
            elif target>i:
                self.recursion(candidates,target-i,res,intermedia+[i])
            else:
                return

def main():
    test=CombinationSum()
    print(test.combinationSum([2,3,4,3,6,6,7],7))

if __name__ == "__main__":
    main()