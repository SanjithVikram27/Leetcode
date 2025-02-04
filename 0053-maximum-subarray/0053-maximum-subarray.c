int maxSubArray(int* nums, int numsSize) {
    int maxsum = nums[0];
    int sum=0;
    int i;

    for(i=0;i<numsSize;i++) {
        sum = sum + nums[i];
        if(sum>maxsum) {
            maxsum = sum;
        }
        if(sum<0) {
            sum=0;
        }
    }
    return maxsum;
}