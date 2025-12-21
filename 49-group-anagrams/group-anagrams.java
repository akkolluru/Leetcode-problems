class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
     for (String st : strs){
        char[] chrs = st.toCharArray();
        Arrays.sort(chrs);
        String str_sorted = new String(chrs);
        if (!map.containsKey(str_sorted)){
            map.put(str_sorted, new ArrayList<>());
            
        }
        map.get(str_sorted).add(st);
        

     }  
    return new ArrayList<>(map.values()); 
    }
}