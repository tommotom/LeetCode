class MyCalendar {

    private TreeMap<Integer, Integer> calendar = new TreeMap<>();

    public MyCalendar() {
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);
        Integer next = calendar.ceilingKey(start);
        if (prev != null && start < calendar.get(prev)) {
            return false;
        }

        if (next != null && next < end) {
            return false;
        }
        calendar.put(start, end);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
