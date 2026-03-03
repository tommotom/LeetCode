impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut consecutive = Vec::new();
        for row in 0..n {
            let mut count = 0;
            for col in (0..n).rev() {
                if grid[row][col] == 1 {
                    break;
                }
                count += 1;
            }
            consecutive.push(count);
        }
        let mut ans = 0;
        for i in 0..n {
            if consecutive[i] >= n - i - 1 {
                continue;
            }
            let mut target = n;
            for j in (i+1)..n {
                if consecutive[j] >= n - i - 1 {
                    target = j;
                    break;
                }
            }
            if target == n {
                return -1;
            }
            let tmp = consecutive[target];
            for j in ((i+1)..=target).rev() {
                consecutive[j] = consecutive[j-1];
                ans += 1;
            }
            consecutive[i] = tmp;
        }
        ans
    }
}
