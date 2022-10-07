class ByEnd implements Comparator<Booking> {
    @Override
    public int compare(Booking a, Booking b) {
        if (a.end == b.end) {
            return Integer.compare(a.start, b.start);
        }
        return Integer.compare(a.end, b.end);
    }
}

class ByStart implements Comparator<Booking> {
    @Override
    public int compare(Booking a, Booking b) {
        if (a.start == b.start) {
            return Integer.compare(a.end, b.end);
        }
        return Integer.compare(a.start, b.start);
    }
}

class Booking {

    int start;
    int end;

    public Booking(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class MyCalendarThree {

    PriorityQueue<Booking> books = new PriorityQueue<>(new ByStart());

    public MyCalendarThree() {
    }

    public int book(int start, int end) {
        books.add(new Booking(start, end));
        int ans = 0;
        PriorityQueue<Booking> recover = new PriorityQueue<>(new ByStart());
        PriorityQueue<Booking> in = new PriorityQueue<>(new ByEnd());
        while (!books.isEmpty()) {
            Booking book = books.poll();
            recover.add(book);
            while (in.size() > 0 && in.peek().end <= book.start) {
                in.poll();
            }
            in.add(book);
            ans = Math.max(ans, in.size());
        }
        books = recover;
        return ans;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */
