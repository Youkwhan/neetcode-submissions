class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        // array
        int[] buckets = new int[26];
        for (int i =0; i < s.length(); i++) {
            // lower case only; a=97 -> 0
            buckets[s.charAt(i) - 'a'] += 1;
            buckets[t.charAt(i) - 'a'] -= 1;
        }

        for(int bucket:buckets) {
            if (bucket != 0){
                return false;
            }
        }
        return true;
    }
}
