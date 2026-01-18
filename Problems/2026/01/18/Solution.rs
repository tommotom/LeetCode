impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        for r in 0..grid.len() {
            for c in 0..grid[0].len() {
                for s in 1..((grid.len() - r).min(grid[0].len() - c) + 1) {
                    let mut target = 0;
                    for d in 0..s {
                        target += grid[r+d][c+d];
                    }
                    let mut is_valid = true;
                    let mut sum = 0;
                    for d in 0..s {
                        sum += grid[r+d][c+s-1-d];
                    }
                    if target != sum {
                        is_valid = false;
                        continue;
                    }

                    for d in 0..s {
                        let mut row = 0;
                        for cc in c..(c+s) {
                            row += grid[r+d][cc];
                        }
                        if row != target {
                            is_valid = false;
                            break;
                        }

                        let mut col = 0;
                        for rr in r..(r+s) {
                            col += grid[rr][c+d];
                        }
                        if col != target {
                            is_valid = false;
                            break;
                        }
                    }
                    if is_valid {
                        ans = ans.max(s)
                    }
                }
            }
        }
        ans as i32
    }
}
