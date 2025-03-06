impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len();
        let mut counter = vec![0; n*n];
        for row in grid {
            for num in row {
                counter[num as usize - 1] += 1;
            }
        }
        let mut ans = vec![0, 0];
        for i in 0..n*n {
            if counter[i] == 0 {
                ans[1] = i as i32 + 1;
            } else if counter[i] == 2 {
                ans[0] = i as i32 + 1;
            }
        }
        ans
    }
}
