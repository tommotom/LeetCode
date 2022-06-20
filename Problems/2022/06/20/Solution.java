class Node {
  public char c;
  public Node[] children = new Node[26];

  public Node(char c) {
    this.c = c;
  }
}

class Solution {
  public int minimumLengthEncoding(String[] words) {
    Arrays.sort(words, (a, b) -> b.length() - a.length());

    Node root = new Node(' ');
    int ans = 0;
    for (String word : words) {
      Node node = root;
      boolean isSubstring = true;
      for (int i = word.length()-1; i >= 0; i--) {
        char c = word.charAt(i);
        int j = c - 'a';
        if (node.children[j] == null) {
          node.children[j] = new Node(c);
          isSubstring = false;
        }
        node = node.children[j];
      }
      if (!isSubstring) {
        ans += word.length() + 1;
      }
    }
    return ans;
  }
}
