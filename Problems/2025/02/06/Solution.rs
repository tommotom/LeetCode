use std::collections::HashMap;

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut product = HashMap::new();
        for i in 1..nums.len() {
            for j in 0..i {
                let p = nums[i] * nums[j];
                if !product.contains_key(&p) {
                    product.insert(p, Vec::new());
                }
                if let Some(arr) = product.get_mut(&p) {
                    arr.push((nums[i], nums[j]));
                }
            }
        }

        let mut ans = 0;
        for (k, v) in product.iter() {
            let n = v.len() as i32;
            ans += n * (n - 1) * 4
        }
        ans
    }
}
