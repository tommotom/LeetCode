class Solution {
    public String breakPalindrome(String palindrome) {
        if (palindrome.length() == 1) {
            return "";
        }
        if (palindrome.substring(0, palindrome.length()/2).matches(".*[b-z].*")) {
            return palindrome.replaceFirst("[b-z]", "a");
        }
        return palindrome.substring(0, palindrome.length()-1) + "b";
    }
}
