class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> map = new HashSet<>();
        for (int num : nums) {
            if (map.contains(num)) {
                return true;
            }
            map.add(num);
        }
        // if(nums.length != map.size()) {
        //     return true;
        // }
        return false;
    }
}