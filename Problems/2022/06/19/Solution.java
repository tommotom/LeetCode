class Node {
  private List<String> words = new ArrayList<>();
  private Node[] children = new Node[26];
  public char c;

  public Node(char c) {
    this.c = c;
  }

  public Node getChild(char c) {
    return children[c-'a'];
  }

  public void putChild(char c, Node node) {
    children[c-'a'] = node;
  }

  public List<String> getSuggestion() {
    List<String> ret = new ArrayList<>();
    int limit = Math.min(3, words.size());
    for (int i = 0; i < limit; i++) {
      ret.add(words.get(i));
    }
    return ret;
  }

  public void addWord(String word) {
    words.add(word);
  }
}

class Solution {
  public List<List<String>> suggestedProducts(String[] products, String searchWord) {
    Arrays.sort(products);

    Node root = new Node(' ');
    for (String product : products) {
      Node cur = root;
      for (char c : product.toCharArray()) {
        if (cur.getChild(c) == null) {
          cur.putChild(c, new Node(c));
        }
        cur = cur.getChild(c);
        cur.addWord(product);
      }
    }

    List<List<String>> ans = new ArrayList<>();
    Node cur = root;
    for (char c : searchWord.toCharArray()) {
      if (cur != null) {
        cur = cur.getChild(c);
      }
      if (cur == null) {
        ans.add(new ArrayList());
        continue;
      }
      ans.add(cur.getSuggestion());
    }
    return ans;
  }
}
