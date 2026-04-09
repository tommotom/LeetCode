use std::collections::HashMap;

impl Solution {
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        let n = grid.len();
        let m = grid[0].len();

        let mut pref_row = vec![0i64; n];
        let mut pref_col = vec![0i64; m];
        let mut mp: HashMap<i32, Vec<(usize, usize)>> = HashMap::new();


        for i in 0..n {
            let mut row_sum = 0i64;
            for j in 0..m {
                let val = grid[i][j];
                row_sum += val as i64;
                mp.entry(val).or_insert(Vec::new()).push((i, j));
            }
            pref_row[i] = row_sum + if i > 0 { pref_row[i - 1] } else { 0 };
        }

        for j in 0..m {
            let mut col_sum = 0i64;
            for i in 0..n {
                col_sum += grid[i][j] as i64;
            }
            pref_col[j] = col_sum + if j > 0 { pref_col[j - 1] } else { 0 };
        }

        let total = pref_row[n - 1];

        fn can_remove(r1: usize, c1: usize, r2: usize, c2: usize, i: usize, j: usize) -> bool {
            let rows = r2 - r1 + 1;
            let cols = c2 - c1 + 1;

            if rows * cols <= 1 { return false; }
            if rows == 1 { return j == c1 || j == c2; }
            if cols == 1 { return i == r1 || i == r2; }
            true
        }

        for i in 0..n - 1 {
            let top = pref_row[i];
            let bottom = total - top;
            if top == bottom { return true; }

            let diff = (top - bottom).abs();
            if diff <= i32::MAX as i64 {
                if let Some(coords) = mp.get(&(diff as i32)) {
                    for &(x, y) in coords {
                        if top > bottom {
                            if x <= i && can_remove(0, 0, i, m - 1, x, y) { return true; }
                        } else {
                            if x > i && can_remove(i + 1, 0, n - 1, m - 1, x, y) { return true; }
                        }
                    }
                }
            }
        }

        for j in 0..m - 1 {
            let left = pref_col[j];
            let right = total - left;
            if left == right { return true; }

            let diff = (left - right).abs();
            if diff <= i32::MAX as i64 {
                if let Some(coords) = mp.get(&(diff as i32)) {
                    for &(x, y) in coords {
                        if left > right {
                            if y <= j && can_remove(0, 0, n - 1, j, x, y) { return true; }
                        } else {
                            if y > j && can_remove(0, j + 1, n - 1, m - 1, x, y) { return true; }
                        }
                    }
                }
            }
        }

        false
    }
}
