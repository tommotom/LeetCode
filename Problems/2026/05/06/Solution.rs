impl Solution {
    pub fn rotate_the_box(box_grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
        let (m, n) = (box_grid.len(), box_grid[0].len());
        let mut ans = vec![vec!['.'; m]; n];
        for r in 0..m {
            let mut count = 0;
            let mut i = n - 1;
            for c in (0..n).rev() {
                if box_grid[r][c] == '*' {
                    while count > 0 {
                        ans[i][m - r - 1] = '#';
                        count -= 1;
                        i -= 1;
                    }
                    i = c - 1;
                    ans[c][m - r - 1] = '*';
                } else if box_grid[r][c] == '#' {
                    count += 1;
                }
            }
            while count > 0 {
                ans[i][m - r - 1] = '#';
                count -= 1;
                i -= 1;
            }
        }
        ans
    }
}
