class Node {
  public final int wordI;
  public int i;

  public Node(int wordI) {
    this.wordI = wordI;
    this.i = 0;
  }
}

class Solution {
  public int numMatchingSubseq(String s, String[] words) {
    LinkedList[] state = new LinkedList[26];
    for (int i = 0; i < 26; i++) {
      state[i] = new LinkedList<Node>();
    }
    for (int i = 0; i < words.length; i++) {
      int j = words[i].charAt(0) - 'a';
      state[j].add(new Node(i));
    }
    int ans = 0;
    for (char c : s.toCharArray()) {
      int i = c - 'a';
      int size = state[i].size();
      for (int j = 0; j < size; j++) {
        Node node = (Node) state[i].poll();
        String word = words[node.wordI];
        if (node.i == word.length()-1) {
          ans++;
        } else {
          node.i++;
          int k = word.charAt(node.i) - 'a';
          state[k].add(node);
        }
      }
    }
    return ans;
  }
}
