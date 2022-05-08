/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {

  private List<NestedInteger> nestedList;
  private Stack<Integer> indices = new Stack<>();
  private Stack<List> lists = new Stack<>();
  private int i = 0;
  private Integer next;

  public NestedIterator(List<NestedInteger> nestedList) {
    this.nestedList = nestedList;
    this.next = fetchNext();
  }

  @Override
  public Integer next() {
    int tmp = next;
    next = fetchNext();
    return tmp;
  }

  @Override
  public boolean hasNext() {
    return next != null;
  }

  private Integer fetchNext() {
    if (i == nestedList.size()) {
      if (indices.empty()) {
        return null;
      }
      nestedList = lists.pop();
      i = indices.pop();
      return fetchNext();
    }

    NestedInteger cur = nestedList.get(i);
    i++;
    if (cur.isInteger()) {
      return cur.getInteger();
    }
    lists.push(nestedList);
    indices.push(i);
    nestedList = cur.getList();
    i = 0;
    return fetchNext();
  }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
