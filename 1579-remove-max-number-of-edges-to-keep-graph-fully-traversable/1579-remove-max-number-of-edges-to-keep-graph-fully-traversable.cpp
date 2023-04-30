class Solution {
public:
    int a[100001];
    int b[100001];
    int finda(int x)
    {
        if (x!=a[x] &&x!=0)
        {
            a[x]=finda(a[x]);
        }
        return a[x];
    }
    int findb(int x)
    {
        if (x!=b[x]&&x!=0)
        {
            b[x]=findb(b[x]);
        }
        return b[x];
    }
    bool uniona(int x, int y)
    {
        x=finda(x);
        y=finda(y);
        //printf("%d %d\n",x,y);
        if (x==y && x!=0)
        {
            return 0;
        }
        a[x]=y;
        return 1;
    }
    bool unionb(int x, int y)
    {
        x=findb(x);
        y=findb(y);
        if (x==y && x!=0)
        {
            return 0;
        }
        b[x]=y;
        return 1;
    }
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        int ac=n;
        int bc=n;
        int m=edges.size();
        int out=0;
        for (int i=0;i<=n;i++)
        {
            a[i]=i;
            b[i]=i;
        }
        for (int i=0;i<m;i++)
        {
            if (edges[i][0]==3)
            {
                int val=0;
                if (uniona(edges[i][1],edges[i][2])==0)
                {
                    //printf("1:%d %d %d\n",ac,bc,out);
                    val=1;
                }
                else
                {
                    //printf("2:%d %d %d\n",ac,bc,out);
                    ac--;
                }
                if (unionb(edges[i][1],edges[i][2])==0)
                {
                    //printf("3:%d %d %d\n",ac,bc,out);
                    val=1;
                }
                else
                {
                    //printf("4:%d %d %d\n",ac,bc,out);
                    bc--;
                }
                out=out+val;
            }
        }
        for (int i=0;i<m;i++)
        {
            int val=0;
            if (edges[i][0]==1)
            {
                if (uniona(edges[i][1],edges[i][2])==0)
                {
                    //printf("5:%d %d %d\n",ac,bc,out);
                    val=1;
                }
                else
                {
                    //printf("6:%d %d %d\n",ac,bc,out);
                    ac--;
                }
            }
            if (edges[i][0]==2)
            {
                if (unionb(edges[i][1],edges[i][2])==0)
                {
                    //printf("7:%d %d %d\n",ac,bc,out);
                    val=1;
                }
                else
                {
                    //printf("8:%d %d %d\n",ac,bc,out);
                    bc--;
                }
            }
            out=out+val;
        }
        //printf("%d %d %d",ac,bc,out);
        if (ac!=1 || bc!=1)
        {
            return -1;
        }
        return out;
    }
};