impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, mut capacity: Vec<i32>) -> i32 {
        capacity.sort_by(|a, b| b.cmp(&a));
        let mut apples: i32 = apple.iter().sum();
        let mut ans = 0;
        for cap in capacity {
            apples -= cap;
            ans += 1;
            if apples <= 0 {
                break;
            }
        }
        ans
    }
}
