class MyCalendarTwo {

    cal1: number[][];
    cal2: number[][]

    constructor() {
        this.cal1 = [];
        this.cal2 = [];
    }

    book(start: number, end: number): boolean {
        for (const booking of this.cal2) {
            if (this.hasIntersection(booking, [start, end])) {
                return false;
            }
        }

        for (const booking of this.cal1) {
            if (this.hasIntersection(booking, [start ,end])) {
                this.cal2.push(this.getRange(booking, [start, end]));
            }
        }

        this.cal1.push([start, end]);
        return true;
    }

    getRange(a: number[], b: number[]) {
        return [Math.max(a[0], b[0]), Math.min(a[1], b[1])];
    }

    hasIntersection(a: number[], b: number[]): boolean {
        return !(a[1] <= b[0] || b[1] <= a[0]);
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(start,end)
 */
