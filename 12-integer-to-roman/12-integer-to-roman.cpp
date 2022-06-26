class Solution {
public:
    string intToRoman(int n) {
        string out="";
        while(n>0)
        {
            if(n>=1000)
            {
                out+=string((int)n/1000,'M');
                n%=1000;
            }
            else if(n>=900)
            {
                n-=900;
                out+="CM";
            }
            else if(n>=500)
            {
                out+='D';
                n-=500;
            }
            else if(n>=400)
            {
                out+="CD";
                n-=400;
            }
            else if(n>=100)
            {
                out+='C';
                n-=100;
            }
            else if(n>=90)
            {
                out+="XC";
                n-=90;
            }
            else if(n>=50)
            {
                out+='L';
                n-=50;
            }
            else if(n>=40)
            {
                out+="XL";
                n-=40;
            }
            else if(n>=10)
            {
                out+='X';
                n-=10;
            }
            else if(n>=9)
            {
                out+="IX";
                n-=9;
            }
            else if(n>=5)
            {
                out+='V';
                n-=5;
            }
            else if(n>=4)
            {
                out+="IV";
                n-=4;
            }
            else
            {
                out+=string(n,'I');
                n=0;
            }
        }
        return out;
    }
};