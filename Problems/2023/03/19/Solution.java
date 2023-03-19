class Node {

    char c;
    Map<Character, Node> children = new HashMap<>();
    boolean isWord;

    Node(char c) {
        this.c = c;
    }
}

class WordDictionary {

    Node root;

    public WordDictionary() {
        root = new Node(' ');
    }

    public void addWord(String word) {
        Node node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new Node(c));
            node = node.children.get(c);
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        List<Node> q = new ArrayList<>();
        q.add(root);
        for (char c : word.toCharArray()) {
            if (q.size() == 0) {
                return false;
            }
            List<Node> next = new ArrayList<>();

            if (c == '.') {
                for (Node node : q) {
                    for (Node child : node.children.values()) {
                        next.add(child);
                    }
                }
            } else {
                for (Node node : q) {
                    if (!node.children.containsKey(c)) {
                        continue;
                    }
                    next.add(node.children.get(c));
                }
            }

            q = next;
        }

        return q.stream().anyMatch(a -> a.isWord);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
