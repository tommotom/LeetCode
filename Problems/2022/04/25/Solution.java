// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {

  private Iterator<Integer> iterator;
  private Integer stock;

  public PeekingIterator(Iterator<Integer> iterator) {
    this.iterator = iterator;
  }

  // Returns the next element in the iteration without advancing the iterator.
  public Integer peek() {
    if (stock == null) {
      stock = iterator.next();
    }
    return stock;
  }

  // hasNext() and next() should behave the same as in the Iterator interface.
  // Override them if needed.
  @Override
  public Integer next() {
    if (stock != null) {
      Integer tmp = stock;
      stock = null;
      return tmp;
    }
    return iterator.next();
  }

  @Override
  public boolean hasNext() {
    return stock != null || iterator.hasNext();
  }
}
