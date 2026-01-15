impl Solution {
    pub fn maximize_square_hole_area(n: i32, m: i32, mut h_bars: Vec<i32>, mut v_bars: Vec<i32>) -> i32 {
        h_bars.sort();
        v_bars.sort();

        let mut count = 1;
        let mut h_max = 1;
        for i in 1..h_bars.len() {
            if h_bars[i-1] + 1 == h_bars[i] {
                count += 1;
            } else {
                count = 1;
            }
            h_max = h_max.max(count);
        }

        count = 1;
        let mut v_max = 1;
        for i in 1..v_bars.len() {
            if v_bars[i-1] + 1 == v_bars[i] {
                count += 1;
            } else {
                count = 1;
            }
            v_max = v_max.max(count);
        }


        let s = h_max.min(v_max) + 1;

        s * s
    }
}
