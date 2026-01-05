impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        grid.iter().map(|row| row.iter().filter(|&num| *num < 0).count() as i32).sum()
    }
}
