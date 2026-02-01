import java.util.*;

class Solution {
    
    public String[] solution(String[][] plans) {
        List<Plan> list = new ArrayList<>();
        
        for (String[] p : plans) {
            String name = p[0];
            int start = toMinutes(p[1]);
            int playing = Integer.parseInt(p[2]);
            list.add(new Plan(start, playing, name));
        }

        list.sort((a, b) -> Integer.compare(a.start, b.start));

        List<String> answer = new ArrayList<>();
        Deque<Paused> stack = new ArrayDeque<>();

        for (int i = 0; i < list.size(); i++) {
            Plan cur = list.get(i);

            if (i == list.size() - 1) {
                answer.add(cur.name);
                continue;
            }

            int nextStart = list.get(i + 1).start;
            int endTime = cur.start + cur.playing;

            if (nextStart < endTime) {
                stack.push(new Paused(endTime - nextStart, cur.name));
                continue;
            }

            answer.add(cur.name);
            int free = nextStart - endTime;

            while (!stack.isEmpty() && free != 0) {
                Paused paused = stack.pop();
                if (free < paused.remain) {
                    stack.push(new Paused(paused.remain - free, paused.name));
                    free = 0;
                } else {
                    free -= paused.remain;
                    answer.add(paused.name);
                }
            }
        }

        while (!stack.isEmpty()) {
            answer.add(stack.pop().name);
        }

        return answer.toArray(new String[0]);
    }

    private int toMinutes(String s) {
        int hh = Integer.parseInt(s.substring(0, 2));
        int mm = Integer.parseInt(s.substring(3, 5));
        return hh * 60 + mm;
    }

    private static class Plan {
        int start;
        int playing;
        String name;

        Plan(int start, int playing, String name) {
            this.start = start;
            this.playing = playing;
            this.name = name;
        }
    }

    private static class Paused {
        int remain;
        String name;

        Paused(int remain, String name) {
            this.remain = remain;
            this.name = name;
        }
    }
}