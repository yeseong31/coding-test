class Solution {
    public String solution(String new_id) {
        String answer = new_id.toLowerCase()
                .replaceAll("[^a-z0-9\\-_.]", "")
                .replaceAll("\\.+", ".")
                .replaceAll("^\\.+|\\.+$", "");
        
        if (answer.isEmpty()) {
            answer = "a";
        }
        if (answer.length() >= 16) {
            answer = answer.substring(0, 15)
                    .replaceAll("\\.+$", "");
        }
        while (answer.length() <= 2) {
            answer += answer.charAt(answer.length() - 1);
        }
        
        return answer;
    }
}