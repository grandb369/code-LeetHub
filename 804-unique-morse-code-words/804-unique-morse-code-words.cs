public class Solution {
    public int UniqueMorseRepresentations(string[] words) {
        HashSet<String>temp = new HashSet<String>();
        string [] k={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        foreach(string s in words)
        {
            string cur="";
            foreach(char c in s)
            {
                cur+=k[(int)c-97];
            }
            temp.Add(cur);
        }
        return temp.Count;
    }
}