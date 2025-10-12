class Solution {
public:
    int reverse(int x) {
        long rev = 0;
        while(x!=0){
            int rem = x%10;
            x = x/10;
            rev = rev*10 + rem;
        }
        if(rev<INT_MIN || rev>INT_MAX){
            return 0;
        }
        return rev;
    }
};