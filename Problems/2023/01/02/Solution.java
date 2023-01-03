class Solution {
    public boolean detectCapitalUse(String word) {
        return isAllCapitals(word) || isAllNotCapitals(word) || isOnlyFirstCapital(word);
    }

    private boolean isAllCapitals(String word) {
        for (char c : word.toCharArray()) {
            if (!('A' <= c && c <= 'Z')) {
                return false;
            }
        }
        return true;
    }

    private boolean isAllNotCapitals(String word) {
        for (char c : word.toCharArray()) {
            if (!('a' <= c && c <= 'z')) {
                return false;
            }
        }
        return true;
    }

    private boolean isOnlyFirstCapital(String word) {
        if (!('A' <= word.charAt(0) && word.charAt(0) <= 'Z')) {
            return false;
        }
        return isAllNotCapitals(word.substring(1));
    }
}
