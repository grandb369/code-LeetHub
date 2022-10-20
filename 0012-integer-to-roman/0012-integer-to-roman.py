class Solution:
    def intToRoman(self, n: int) -> str:
        out=''
        while n>=1000:
            out+='M'
            n-=1000
        while n>=900:
            out+='CM'
            n-=900
        while n>=500:
            out+='D'
            n-=500
        while n>=400:
            out+='CD'
            n-=400
        while n>=100:
            out+='C'
            n-=100
        while n>=90:
            out+='XC'
            n-=90
        while n>=50:
            out+='L'
            n-=50
        while n>=40:
            out+='XL'
            n-=40
        while n>=10:
            out+='X'
            n-=10
        while n>=9:
            out+='IX'
            n-=9
        while n>=5:
            out+='V'
            n-=5
        while n>=4:
            out+='IV'
            n-=4
        while n>0:
            out+='I'
            n-=1
        return out