class Solution {
  public boolean isValid(String s) {
    Map<Character, Character> brackets = new HashMap<>();
    brackets.put('(', ')');
    brackets.put('[', ']');
    brackets.put('{', '}');

    if (s.length() % 2 == 1) {
      return false;
    }

    Stack<Character> st = new Stack<>();
    for (int i = 0; i < s.length(); i++) {
      if (brackets.containsKey(s.charAt(i))){
        st.push(s.charAt(i));
      } else if (st.size() == 0 || brackets.get(st.pop()) != s.charAt(i)) {
        return false;
      }
    }

    return st.size() == 0;
  }
}
