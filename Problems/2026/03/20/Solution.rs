impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        fn helper(grid: &Vec<Vec<i32>>, i: usize, j: usize, k: usize) -> i32 {
            let mut vals = Vec::new();
            for r in i..(i+k) {
                for c in j..(j+k) {
                    vals.push(grid[r][c]);
                }
            }
            vals.sort();
            let mut ans = i32::MAX;
            for l in 1..vals.len() {
                if vals[l] == vals[l-1] {
                    continue;
                }
                ans = ans.min(vals[l] - vals[l-1]);
            }
            if ans == i32::MAX {0} else {ans}
        }

        let k = k as usize;
        let m = grid.len();
        let n = grid[0].len();

        let mut ans: Vec<Vec<i32>> = Vec::new();
        for i in 0..(m-k+1) {
            let mut row = Vec::new();
            for j in 0..(n-k+1) {
                row.push(helper(&grid, i, j, k));
            }
            ans.push(row);
        }
        ans
    }
}
