impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut less = Vec::new();
        let mut equal = Vec::new();
        let mut greater = Vec::new();
        for num in nums {
            if num < pivot {
                less.push(num);
            } else if num > pivot {
                greater.push(num);
            } else {
                equal.push(num);
            }
        }
        less.extend(equal.iter().cloned());
        less.extend(greater.iter().cloned());
        less
    }
}
