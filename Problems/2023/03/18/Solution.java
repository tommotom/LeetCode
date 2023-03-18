class BrowserHistory {

    private Stack<String> back = new Stack<>();
    private Stack<String> forward = new Stack<>();
    private String cur;

    public BrowserHistory(String homepage) {
        this.cur = homepage;
    }

    public void visit(String url) {
        forward = new Stack<>();
        back.push(cur);
        cur = url;
    }

    public String back(int steps) {
        while (steps > 0 && back.size() > 0) {
            forward.push(cur);
            cur = back.pop();
            steps--;
        }
        return cur;
    }

    public String forward(int steps) {
        while (steps > 0 && forward.size() > 0) {
            back.push(cur);
            cur = forward.pop();
            steps--;
        }
        return cur;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
