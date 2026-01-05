impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        fn is_magic_square(grid: &Vec<Vec<i32>>, r: usize, c: usize) -> bool {
            if r + 2 >= grid.len() {
                return false;
            }
            if c + 2 >= grid[0].len() {
                return false;
            }
            let mut counter = vec![0; 9];
            for i in r..(r+3) {
                for j in c..(c+3) {
                    if grid[i][j] > 9 || grid[i][j] == 0 {
                        return false;
                    }
                    counter[grid[i][j] as usize - 1] += 1;
                }
            }
            for i in 0..9 {
                if counter[i] != 1 {
                    return false;
                }
            }
            for i in 0..3 {
                let mut row = 0;
                let mut col = 0;
                for j in 0..3 {
                    row += grid[r+i][c+j];
                    col += grid[r+j][c+i];
                }
                if row != 15 || col != 15 {
                    return false;
                }
            }
            if 15 != grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] {
                return false;
            }
            if 15 != grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2] {
                return false;
            }
            true
        }

        let n = grid.len();
        let m = grid[0].len();
        let mut ans = 0;
        for r in 0..n {
            for c in 0..m {
                if is_magic_square(&grid, r, c) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
