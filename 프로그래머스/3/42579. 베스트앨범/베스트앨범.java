import java.util.*;
import java.util.stream.*;

class Solution {

    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> totalPlay = new HashMap<>();
        Map<String, List<int[]>> genreList = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            totalPlay.merge(genres[i], plays[i], Integer::sum);
            genreList.computeIfAbsent(genres[i], k -> new ArrayList<>())
                     .add(new int[]{plays[i], i});
        }

        return totalPlay.entrySet().stream()
                .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                .flatMap(e -> genreList.get(e.getKey()).stream()
                        .sorted(Comparator.comparingInt((int[] a) -> -a[0])
                                         .thenComparingInt(a -> a[1]))
                        .limit(2)
                        .map(a -> a[1]))
                .mapToInt(Integer::intValue)
                .toArray();
    }
}