import java.util.Arrays;

public class Solution {

    private boolean isValid(char[] tree, int start, int end, boolean parentIsDummy) {
        if (start > end) {
            return true;
        }

        int mid = (start + end) >>> 1;
        boolean currentIsOne = tree[mid] == '1';
        
        if (parentIsDummy && currentIsOne) {
            return false;
        }

        boolean currentIsDummy = !currentIsOne;

        return isValid(tree, start, mid - 1, currentIsDummy)
                && isValid(tree, mid + 1, end, currentIsDummy);
    }

    private char[] makeFullBinaryTree(long number) {
        String binary = Long.toBinaryString(number);

        int treeLength = 1;
        while (treeLength < binary.length()) {
            treeLength = treeLength * 2 + 1;
        }

        char[] tree = new char[treeLength];

        Arrays.fill(tree, '0');

        int padding = treeLength - binary.length();
        binary.getChars(0, binary.length(), tree, padding);

        return tree;
    }

    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            char[] tree = makeFullBinaryTree(numbers[i]);
            answer[i] = isValid(tree, 0, tree.length - 1, false) ? 1 : 0;
        }

        return answer;
    }
}