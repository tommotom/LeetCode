impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut smaller = Vec::new();
        let mut larger = Vec::new();
        let mut pivots = Vec::new();
        for num in nums {
            if num < pivot {
                smaller.push(num);
            } else if num > pivot {
                larger.push(num);
            } else {
                pivots.push(num);
            }
        }
        [smaller, pivots, larger].concat()
    }
}
