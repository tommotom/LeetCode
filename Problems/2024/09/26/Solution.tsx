class MyCalendar {

    books: number[][];

    constructor() {
        this.books = [];
    }

    book(start: number, end: number): boolean {
        const i = this.search(start);
        if (i < this.books.length && this.hasIntersection(this.books[i], [start, end])) {
            return false;
        }
        this.books.splice(i, 0, [start, end]);
        return true;
    }

    hasIntersection(book1: number[], book2: number[]) {
        return !(book1[1] <= book2[0] || book2[1] <= book1[0]);
    }

    search(start: number): number {
        let l = 0, r = this.books.length;
        while (l < r) {
            const m = l + (Math.floor((r - l) / 2));
            if (this.books[m][1] <= start) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
