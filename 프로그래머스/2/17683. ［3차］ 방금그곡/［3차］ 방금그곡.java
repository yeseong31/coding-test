import java.util.HashMap;
import java.util.Map;

class Solution {
    
    public String solution(String m, String[] musicinfos) {
        String answerTitle = "(None)";
        int maxPlayTime = -1;
        int minStartTime = Integer.MAX_VALUE;

        Map<String, String> sharp = new HashMap<>();
        sharp.put("C#", "c");
        sharp.put("D#", "d");
        sharp.put("F#", "f");
        sharp.put("G#", "g");
        sharp.put("A#", "a");

        for (String key : sharp.keySet()) {
            m = m.replace(key, sharp.get(key));
        }

        for (String info : musicinfos) {
            String[] parts = info.split(",");
            String startStr = parts[0];
            String endStr = parts[1];
            String title = parts[2];
            String melody = parts[3];

            for (String key : sharp.keySet()) {
                melody = melody.replace(key, sharp.get(key));
            }

            int start = Integer.parseInt(startStr.substring(0, 2)) * 60 + Integer.parseInt(startStr.substring(3));
            int end = Integer.parseInt(endStr.substring(0, 2)) * 60 + Integer.parseInt(endStr.substring(3));
            int playTime = end - start;

            StringBuilder playedMelody = new StringBuilder();
            int melodyLength = melody.length();
            for (int i = 0; i < playTime; i++) {
                playedMelody.append(melody.charAt(i % melodyLength));
            }

            if (playedMelody.toString().contains(m)) {
                if (playTime > maxPlayTime) {
                    maxPlayTime = playTime;
                    minStartTime = start;
                    answerTitle = title;
                } else if (playTime == maxPlayTime) {
                    if (start < minStartTime) {
                        minStartTime = start;
                        answerTitle = title;
                    }
                }
            }
        }

        return answerTitle;
    }
}