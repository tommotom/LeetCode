use std::cmp::Ordering;

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let n = squares.len();
        let m = 2 * n; // Each square produces two events.
        let mut events = Vec::with_capacity(m);
        let mut xs_raw = Vec::with_capacity(m);

        // Step 1: Generate events and collect x-coordinates
        for sq in squares {
            let x = sq[0] as f64;
            let y = sq[1] as f64;
            let l = sq[2] as f64;
            let x2 = x + l;
            let y2 = y + l;

            events.push(Event { y, x1: x, x2, event_type: 1 }); // Start event
            events.push(Event { y: y2, x1: x, x2, event_type: -1 }); // End event
            xs_raw.push(x);
            xs_raw.push(x2);
        }

        // Step 2: Sort events by y-coordinate
        events.sort_by(|a, b| a.y.partial_cmp(&b.y).unwrap_or(Ordering::Equal));

        // Step 3: Compress x-coordinates
        let xs = Self::compress(xs_raw);

        // Step 4: Build Segment Tree over compressed x-coordinates
        let mut st = SegmentTree::new(xs.clone());

        let mut total_area = 0.0;
        let mut prev_y = events[0].y;
        let mut segments = Vec::new();
        let mut i = 0;

        // Step 5: Sweep through the events
        while i < m {
            let cur_y = events[i].y;
            if cur_y > prev_y {
                let union_x = st.query();
                let segment_area = union_x * (cur_y - prev_y);
                total_area += segment_area;
                segments.push(SweepSegment {
                    y_start: prev_y,
                    y_end: cur_y,
                    start_cum: total_area - segment_area,
                    union_x,
                });
                prev_y = cur_y;
            }

            // Process all events at cur_y
            while i < m && events[i].y == cur_y {
                let l_idx = xs.binary_search_by(|x| x.partial_cmp(&events[i].x1).unwrap()).unwrap();
                let r_idx = xs.binary_search_by(|x| x.partial_cmp(&events[i].x2).unwrap()).unwrap();
                st.update(1, 0, xs.len(), l_idx, r_idx, events[i].event_type);
                i += 1;
            }
        }

        let target_area = total_area / 2.0;

        // Step 6: Find the y-coordinate where the area is divided in half
        for seg in segments {
            let seg_area = seg.union_x * (seg.y_end - seg.y_start);
            if target_area <= seg.start_cum + seg_area {
                let needed_area = target_area - seg.start_cum;
                let dy = needed_area / seg.union_x;
                return seg.y_start + dy;
            }
        }

        prev_y // Fallback, should not happen if everything is correct
    }

    // Step 7: Compress an array of doubles to a sorted array of unique values
    fn compress(arr: Vec<f64>) -> Vec<f64> {
        let mut unique_vals = arr.clone();
        unique_vals.sort_by(|a, b| a.partial_cmp(b).unwrap());
        unique_vals.dedup();
        unique_vals
    }
}

// Event for sweep-line (vertical boundaries)
struct Event {
    y: f64,
    x1: f64,
    x2: f64,
    event_type: i32,
}

// Segment representing a portion of the union-area function
struct SweepSegment {
    y_start: f64,
    y_end: f64,
    start_cum: f64, // Cumulative area at y_start
    union_x: f64,   // Union length in x over this segment
}

// Segment Tree for union-length of x-intervals
struct SegmentTree {
    n: usize,
    tree: Vec<f64>, // Tree[idx]: Total length covered in the node's interval
    count: Vec<i32>, // Count[idx]: Coverage count
    xs: Vec<f64>,   // Compressed x-coordinates
}

impl SegmentTree {
    fn new(xs: Vec<f64>) -> Self {
        let n = xs.len();
        let tree = vec![0.0; 4 * n];
        let count = vec![0; 4 * n];
        SegmentTree { n, tree, count, xs }
    }

    // Update the range [ql, qr) with delta
    fn update(&mut self, idx: usize, l: usize, r: usize, ql: usize, qr: usize, delta: i32) {
        if qr <= l || ql >= r {
            return;
        }
        if ql <= l && r <= qr {
            self.count[idx] += delta;
        } else {
            let mid = (l + r) / 2;
            self.update(idx * 2, l, mid, ql, qr, delta);
            self.update(idx * 2 + 1, mid, r, ql, qr, delta);
        }

        if self.count[idx] > 0 {
            self.tree[idx] = self.xs[r] - self.xs[l];
        } else if r - l == 1 {
            self.tree[idx] = 0.0;
        } else {
            self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1];
        }
    }

    // Query the union of covered length in x
    fn query(&self) -> f64 {
        self.tree[1]
    }
}
