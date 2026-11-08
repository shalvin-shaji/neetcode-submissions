class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();

        for(String s: strs) {
            char[] keyArray = new char[26];
            for(char c: s.toCharArray()) {
                keyArray[c - 'a'] += 1;
            }
            String key = new String(keyArray);
            group.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(group.values());
    }
    
}
