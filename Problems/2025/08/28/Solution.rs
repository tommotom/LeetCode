impl Solution {
    pub fn sort_matrix(mut grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        for rr in 0..n {
            let (mut r, mut c) = (rr, 0);
            let mut arr = Vec::new();
            while r < n {
                arr.push(grid[r][c]);
                r += 1;
                c += 1;
            }
            arr.sort_by(|a, b| b.cmp(&a));
            let (mut r, mut c) = (rr, 0);
            while r < n {
                grid[r][c] = arr[c];
                r += 1;
                c += 1;
            }
        }
        for cc in 1..n {
            let (mut r, mut c) = (0, cc);
            let mut arr = Vec::new();
            while c < n {
                arr.push(grid[r][c]);
                r += 1;
                c += 1;
            }
            arr.sort();
            let (mut r, mut c) = (0, cc);
            while c < n {
                grid[r][c] = arr[r];
                r += 1;
                c += 1;
            }
        }
        grid
    }
}
