class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character,Integer> sat = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(sat.containsKey(s.charAt(i))){
                sat.put(s.charAt(i),sat.get(s.charAt(i))+1);
            } else {
                sat.put(s.charAt(i),1);
            }
        }
        for(int j = 0; j < t.length(); j++){
            if(sat.containsKey(t.charAt(j))){
                if(sat.get(t.charAt(j)) == 0){
                    return false;
                }
                sat.put(t.charAt(j),sat.get(t.charAt(j))-1);
            } else {
                return false;
            }
        }
    return true;
    }
}
