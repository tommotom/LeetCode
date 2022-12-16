class MyQueue {

    Stack<Integer> a = new Stack<>();
    Stack<Integer> b = new Stack<>();

    public MyQueue() {
    }

    public void push(int x) {
        a.push(x);
    }

    public int pop() {
        while (!a.isEmpty()) {
            b.push(a.pop());
        }
        int ret = b.pop();
        while (!b.isEmpty()) {
            a.push(b.pop());
        }
        return ret;
    }

    public int peek() {
        while (!a.isEmpty()) {
            b.push(a.pop());
        }
        int ret = b.peek();
        while (!b.isEmpty()) {
            a.push(b.pop());
        }
        return ret;
    }

    public boolean empty() {
        return a.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
