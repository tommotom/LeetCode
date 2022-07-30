class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] combine = new int[26];
        for (String word : words2) {
            int[] count = count(word);
            combine = merge(combine, count);
        }

        ArrayList<String> ans = new ArrayList<>();
        for (String word : words1) {
            int[] count = count(word);
            if (isValid(count, combine)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean isValid(int[] count, int[] combine) {
        for (int i = 0; i < 26; i++) {
            if (count[i] < combine[i]) {
                return false;
            }
        }
        return true;
    }

    private int[] count(String word) {
        int[] ret = new int[26];
        for (char c : word.toCharArray()) {
            ret[c-'a']++;
        }
        return ret;
    }

    private int[] merge(int[] count1, int[] count2) {
        int[] ret = new int[26];
        for (int i = 0; i < 26; i++) {
            ret[i] = Math.max(count1[i], count2[i]);
        }
        return ret;
    }
}
