class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices; // Dictionary
        for(int i=0;i<nums.size();i++) {
            indices[nums[i]] = i;
        }
        for(int i=0;i<nums.size();i++){
            int diff=target-nums[i];
            if(indices.count(diff) && indices[diff]!=i){    // If the number is there & diff != num.
                return {i,indices[diff]};
            }    
        }
        return {};
    }
};
