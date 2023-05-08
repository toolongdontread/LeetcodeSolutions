class Solution {
public:
    int passThePillow(int n, int time) {
        int p = 1;
        bool re = false;
        for(int i=0;i<time;i++){
            if(re==false){
                if(p<n){p++;}
            }
            else{
                if(p>1){p--;}
            }

            if(p==n){re=true;}
            else if(p==1){re=false;}
        }
        return p;
    }
};