class Solution {
  public String minRemoveToMakeValid(String s) {
    String[] arr = s.split("");
    int level = 0;
    for (int i = 0; i < arr.length; i++) {
      String character = arr[i];
      if (character.equals("(")) {
        level++;
      } else if (character.equals(")")) {
        if (level == 0) {
          arr[i] = "";
        } else {
          level--;
        }
      }
    }

    int i = arr.length-1;
    while (level > 0) {
      if (arr[i].equals("(")) {
        arr[i] = "";
        level--;
      }
      i--;
    }

    return String.join("", arr);
  }
}
