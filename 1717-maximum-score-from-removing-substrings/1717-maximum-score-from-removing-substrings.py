class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def checkab(s):
            out=0
            while 'ab'in s or 'ba'in s:
                temp=[]
                if 'ab' in s:
                    for i in s:
                        if i=='b' and temp and temp[-1]=='a':
                            temp.pop()
                            out+=x
                        else:
                            temp.append(i)
                else:
                    for i in s:
                        if i=='b' and temp and temp[-1]=='a':
                            temp.pop()
                            out+=x
                        elif i=='a'and temp and temp[-1]=='b':
                            temp.pop()
                            out+=y
                        else:
                            temp.append(i)
                s=''.join(temp)
            return out
        def checkba(s):
            out=0
            while 'ab'in s or 'ba'in s:
                temp=[]
                if 'ba' in s:
                    for i in s:
                        if i=='a' and temp and temp[-1]=='b':
                            temp.pop()
                            out+=y
                        else:
                            temp.append(i)
                else:
                    for i in s:
                        if i=='a' and temp and temp[-1]=='b':
                            temp.pop()
                            out+=y
                        elif i=='b'and temp and temp[-1]=='a':
                            temp.pop()
                            out+=x
                        else:
                            temp.append(i)
                s=''.join(temp)
            return out
        return max(checkba(s),checkab(s))