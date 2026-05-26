import java.util.*;

class Solution {

    public String[] solution(String[][] plans) {
        List<Task> tasks = new ArrayList<>();
        for (String[] plan : plans) {
            tasks.add(new Task(plan[0], toMinutes(plan[1]), Integer.parseInt(plan[2])));
        }
        Collections.sort(tasks, Comparator.comparingInt(t -> t.start));

        List<String> result = new ArrayList<>();
        Deque<Task> pausedStack = new ArrayDeque<>();

        for (int i = 0; i < tasks.size(); i++) {
            Task current = tasks.get(i);
            int nextStartTime = (i < tasks.size() - 1) ? tasks.get(i + 1).start : Integer.MAX_VALUE;

            if (nextStartTime < current.start + current.playTime) {
                current.playTime -= (nextStartTime - current.start);
                pausedStack.push(current);
            } else {
                result.add(current.name);
                processPausedTasks(result, pausedStack, nextStartTime - (current.start + current.playTime));
            }
        }

        while (!pausedStack.isEmpty()) {
            result.add(pausedStack.pop().name);
        }

        return result.toArray(new String[0]);
    }

    private void processPausedTasks(List<String> result, Deque<Task> stack, int availableTime) {
        while (!stack.isEmpty() && availableTime > 0) {
            Task top = stack.peek();
            if (top.playTime <= availableTime) {
                availableTime -= top.playTime;
                result.add(stack.pop().name);
            } else {
                top.playTime -= availableTime;
                availableTime = 0;
            }
        }
    }

    private int toMinutes(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
    }

    private static class Task {
        String name;
        int start;
        int playTime;

        Task(String name, int start, int playTime) {
            this.name = name;
            this.start = start;
            this.playTime = playTime;
        }
    }
}