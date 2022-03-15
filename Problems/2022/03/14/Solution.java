class Solution {
  public String simplifyPath(String path) {
    Deque<String> deque = new ArrayDeque<>();

    for (String p: path.split("/")) {
      if (p.isEmpty() || p.equals(".")) {
        continue;
      }
      if (p.equals("..")) {
        deque.poll();
      } else {
        deque.push(p);
      }
    }

    if (deque.isEmpty()) {
      return "/";
    }

    StringBuilder sb = new StringBuilder();
    int size = deque.size();
    for (int i = 0; i < size; i++) {
      sb.append("/").append(deque.removeLast());
    }

    return sb.toString();
  }
}
