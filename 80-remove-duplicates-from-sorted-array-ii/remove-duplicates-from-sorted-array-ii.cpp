class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 1;
        int prev = nums[0];
        int index = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == prev) {
                if (count < 2) {
                    nums[index] = prev;
                    index++;
                    count++;
                } else {
                    continue;
                }
            } else {
                nums[index] = nums[i];
                prev = nums[i];
                count = 1;
                index++;
            }
        }      
        return index;
    }
};