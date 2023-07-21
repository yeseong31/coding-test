class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0;
        
        for (int idx = 0; idx < code.length(); idx++) {
            if (code.charAt(idx) == '1') {
                mode = (mode == 0) ? 1: 0;
                continue;
            }
            if (mode == 0 && (idx % 2 == 0)) {
                ret.append(code.charAt(idx));
            } else if (mode == 1 && (idx % 2 == 1)) {
                ret.append(code.charAt(idx));
            }
        }
        
        return (ret.length() == 0) ? "EMPTY" : ret.toString();
    }
}