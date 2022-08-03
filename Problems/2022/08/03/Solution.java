class Reservation implements Comparable<Reservation> {

    public int start;
    public int end;

    public Reservation(int start, int end) {
        this.start = start;
        this.end =end;
    }

    @Override
    public int compareTo(Reservation another) {
        if (this.start == another.start) {
            return Integer.compare(another.end, this.end);
        }
        return Integer.compare(another.start, this.start);
    }

    public boolean isOverlapped(Reservation another) {
        if (this.end <= another.start) {
            return false;
        }
        if (another.end <= this.start) {
            return false;
        }
        return true;
    }
}

class MyCalendar {

    private LinkedList<Reservation> reservations;

    public MyCalendar() {
        reservations = new LinkedList<>();
    }

    public boolean book(int start, int end) {
        Reservation newReservation = new Reservation(start, end);
        int i = Collections.binarySearch(reservations, newReservation);
        if (i < 0) {
            i = -i - 1;
        }
        if (0 <= i && i < reservations.size() && newReservation.isOverlapped(reservations.get(i))) {
            return false;
        }
        if (0 < i && newReservation.isOverlapped(reservations.get(i-1))) {
            return false;
        }
        if (i < 0 || i == reservations.size()){
            reservations.addLast(newReservation);
        } else {
            reservations.add(i, newReservation);
        }
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
