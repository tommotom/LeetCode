class Solution {
  public int minPartitions(String n) {
    return n.chars().mapToObj(i -> Character.getNumericValue((char) i)).max((a, b) -> a - b).get();
  }
}