class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();

        for(String s: strs) {
            int[] keyArray = new int[26];
            for(int i=0; i<s.length(); i++) {
                char c = s.charAt(i);
                int index = (int) c - (int) 'a';
                keyArray[index] += 1;
            }
            String key = build(keyArray);
            group.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(group.values());
    }
    private String build(int[] keyArray) {
        StringBuilder builder = new StringBuilder();
        for(int i: keyArray) {
            builder.append(i);
            builder.append(",");
        }
        return builder.toString();
    }
}
