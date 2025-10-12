int hammingWeight(int n) {
    int ct =0;
    while(n!=0){
        if(n%2==1){
            ct++;
        }
        n = n/2;
    }
    return ct;
}