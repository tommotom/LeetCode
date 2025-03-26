impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut vals = Vec::new();
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                vals.push(grid[i][j]);
            }
        }
        vals.sort();

        let mut r = 0;
        for i in (0..(vals.len()-1)).rev() {
            if (vals[i+1] - vals[i]) % x != 0 {
                return -1;
            }
            r += ((vals.len() - i - 1) as i32) * (vals[i+1] - vals[i]) / x;
        }

        let mut ans = r;
        let mut l = 0;
        for i in 1..vals.len() {
            r -= ((vals.len() - i) as i32) * (vals[i] - vals[i-1]) / x;
            l += (i as i32) * (vals[i] - vals[i-1]) / x;
            ans = ans.min(l + r);
        }

        ans
    }
}
