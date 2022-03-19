class Element implements Comparable<Element>{

  int freq;
  int insertedAt;
  int val;

  public Element(int freq, int insertedAt, int val) {
    this.freq = freq;
    this.insertedAt = insertedAt;
    this.val = val;
  }

  @Override
  public int compareTo(Element e) {
    if (this.freq != e.freq) {
      return e.freq - this.freq;
    }
    return e.insertedAt - this.insertedAt;
  }
}

class FreqStack {

  int time = 0;
  Map<Integer, Integer> freq = new HashMap<>();
  PriorityQueue<Element> q = new PriorityQueue<>();

  public FreqStack() {

  }

  public void push(int val) {
    if (!freq.containsKey(val)) {
      freq.put(val, 0);
    }
    freq.put(val, freq.get(val)+1);
    q.add(new Element(freq.get(val), time, val));
    time++;
  }

  public int pop() {
    Element ele = q.poll();
    freq.put(ele.val, freq.get(ele.val)-1);
    return ele.val;
  }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */
