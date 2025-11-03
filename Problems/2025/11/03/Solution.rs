impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let mut arr: Vec<char> = colors.chars().collect();
        let (mut j, mut ans) = (0, 0);
        for i in 1..arr.len() {
            if arr[i] == arr[j] {
                ans += needed_time[i].min(needed_time[j]);
            }
            if arr[i] != arr[j] || needed_time[i] > needed_time[j] {
                j = i;
            }
        }
        ans
    }
}
