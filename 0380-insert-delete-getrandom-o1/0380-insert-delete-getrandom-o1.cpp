class RandomizedSet {
public:
    map<int,int>temp;
    vector<int>data;
    int n;
    RandomizedSet() {
        n=0;
    }
    
    bool insert(int val) {
        if(temp.find(val)!=temp.end())return false;
        temp[val]=n;
        n++;
        data.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if(temp.find(val)==temp.end())return false;
        int index=temp[val];
        int v2=data.back();
        data[index]=v2;
        temp[v2]=index;
        temp.erase(val);
        data.pop_back();
        n--;
        return true;
    }
    
    int getRandom() {
        return data[rand()%n];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */