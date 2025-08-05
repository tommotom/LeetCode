impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, mut baskets: Vec<i32>) -> i32 {
        let mut ans = fruits.len();
        for f in fruits {
            for i in 0..baskets.len() {
                if baskets[i] >= f {
                    baskets[i] = 0;
                    ans -= 1;
                    break;
                }
            }
        }
        ans as i32
    }
}
