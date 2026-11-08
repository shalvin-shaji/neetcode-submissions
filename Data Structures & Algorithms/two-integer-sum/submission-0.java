class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dict = new HashMap<>();
        for(int i=0; i < nums.length; i++) {
            if(!dict.containsKey(nums[i])) {
                dict.put(target-nums[i], i);
            }
            else {
                return new int[]{dict.get(nums[i]), i};
            }
        }
        return new int[]{};
    }
}
