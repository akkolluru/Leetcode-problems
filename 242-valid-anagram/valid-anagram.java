class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map_s = new HashMap<>();
        HashMap<Character, Integer> map_t = new HashMap<>();
        if (s.length() != t.length()) {
            return false;
        }

        for (int i=0; i < s.length(); i++){
            map_s.put(s.charAt(i), map_s.getOrDefault(s.charAt(i), 0) + 1);
            map_t.put(t.charAt(i), map_t.getOrDefault(t.charAt(i), 0) + 1);
        }

        if (map_s.size() != map_t.size()){
            return false;
        }

        for (Character ch : map_s.keySet()){
            if (!map_t.containsKey(ch) || !map_t.get(ch).equals(map_s.get(ch))){
                return false;
            }
        }
        return true;
    }
}