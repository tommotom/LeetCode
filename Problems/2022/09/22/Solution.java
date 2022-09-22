class Solution {
    public String reverseWords(String s) {
        return String.join(" ", Arrays.stream(s.split(" ")).map(c->new StringBuilder(c).reverse().toString()).toArray(String[]::new));
    }
}
