class Node {
  public Node[] children = new Node[27];
  public int index;
}

class WordFilter {

  private Node trie;

  public WordFilter(String[] words) {
    trie = new Node();
    for (int i = 0; i < words.length; i++) {
      char[] chars = words[i].toCharArray();
      for (int j = chars.length; j >= 0; j--) {
        Node cur = trie;
        for (int k = j; k < chars.length; k++) {
          char c = chars[k];
          if (cur.children[c-'a'] == null) {
            cur.children[c-'a'] = new Node();
          }
          cur = cur.children[c-'a'];
          cur.index = i;
        }
        if (cur.children['{'-'a'] == null) {
          cur.children['{'-'a'] = new Node();
        }
        cur = cur.children['{'-'a'];
        cur.index = i;
        for (int k = 0; k < chars.length; k++) {
          char c = chars[k];
          if (cur.children[c-'a'] == null) {
            cur.children[c-'a'] = new Node();
          }
          cur = cur.children[c-'a'];
          cur.index = i;
        }
      }
    }
  }

  public int f(String prefix, String suffix) {
    Node cur = trie;
    for (char c : (suffix+"{"+prefix).toCharArray()) {
      if (cur.children[c-'a'] == null) {
        return -1;
      }
      cur = cur.children[c-'a'];
    }
    return cur.index;
  }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */
