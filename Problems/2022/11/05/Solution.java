class Node {
    char c;
    Map<Character, Node> children = new HashMap<>();
    boolean isWord;

    public Node(char c) {
        this.c = c;
    }
}


class Solution {

    Set<String> ans = new HashSet<>();
    char[][] board;
    int[][] dirs = new int[][] {{1,0},{-1,0},{0,1},{0,-1}};

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;

        Node root = new Node(' ');
        for (String word : words) {
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (!node.children.containsKey(c)) {
                    node.children.put(c, new Node(c));
                }
                node = node.children.get(c);
            }
            node.isWord = true;
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(i, j, new HashSet<>(), new StringBuilder(), root);
            }
        }

        return new ArrayList<>(ans);
    }

    private void dfs(int i, int j, Set<Integer> visited, StringBuilder sb, Node node) {
        if (i < 0 || i == board.length || j < 0 || j == board[0].length) {
            return;
        }
        int key = i * 100 + j;
        if (visited.contains(key)) {
            return;
        }
        char c = board[i][j];
        if (!node.children.containsKey(c)) {
            return;
        }
        visited.add(key);
        node = node.children.get(c);
        sb.append(c);
        if (node.isWord) {
            ans.add(sb.toString());
        }

        for (int[] dir : dirs) {
            dfs(i+dir[0], j+dir[1], visited, sb, node);
        }

        sb.deleteCharAt(sb.length()-1);
        visited.remove(key);
    }
}
