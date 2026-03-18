import java.util.*;

class Solution {
    
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> totalPlay = new HashMap<>();
        Map<String, List<int[]>> genreList = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            totalPlay.put(genres[i], totalPlay.getOrDefault(genres[i], 0) + plays[i]);
            
            genreList.putIfAbsent(genres[i], new ArrayList<>());
            genreList.get(genres[i]).add(new int[]{plays[i], i});
        }
        
        List<String> sortedGenres = new ArrayList<>(totalPlay.keySet());
        sortedGenres.sort((a, b) -> totalPlay.get(b) - totalPlay.get(a));
        
        List<Integer> result = new ArrayList<>();
        
        for (String genre : sortedGenres) {
            List<int[]> list = genreList.get(genre);
            list.sort((a, b) -> {
                if (b[0] == a[0]) return a[1] - b[1];
                return b[0] - a[0];
            });
            
            for (int i = 0; i < Math.min(2, list.size()); i++) {
                result.add(list.get(i)[1]);
            }
        }
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}