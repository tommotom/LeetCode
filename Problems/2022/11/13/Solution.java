class Solution {
    public String reverseWords(String s) {
        String[] arr =  Arrays.stream(s.split(" ")).filter(c -> c != "").toArray(String[]::new);
        Collections.reverse(Arrays.asList(arr));
        return String.join(" ", arr);
    }
}
