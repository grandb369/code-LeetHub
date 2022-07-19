class TimeMap {
public:
    map<string,deque<string>>data;
    map<string,deque<int>>time;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        data[key].push_back(value);
        time[key].push_back(timestamp);
    }
    
    string get(string key, int timestamp) {
        if(time.find(key)==time.end())return "";
        while(time[key].size()>1 && timestamp>=time[key][1])
        {
            data[key].pop_front();
            time[key].pop_front();
        }
        return timestamp>=time[key][0]?data[key][0]:"";
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */