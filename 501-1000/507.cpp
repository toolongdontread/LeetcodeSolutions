class Solution {
public:
    bool checkPerfectNumber(int num) {
        int r = 0;
        for(int i=1;i<num;i++){
            if(num%i==0){
                r+=i;
            }
        }
        if(r==num) return true;
        return false;
    }
};