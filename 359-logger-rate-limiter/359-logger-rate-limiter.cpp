class Logger {
public:
    unordered_map<string, int>cache;
    Logger() {
        
    }
    
    bool shouldPrintMessage(int t, string msg) {
        if(cache.find(msg)==cache.end())
        {
            cache[msg]=t+10;
            return true;
        }
        if(cache[msg]<=t)
        {
            cache[msg]=t+10;
            return true;
        }
        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */