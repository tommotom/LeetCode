impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        fn to_arr(mut num: i32) -> Vec<i32> {
            let mut arr = Vec::new();
            while num > 0 {
                arr.push(num % 10);
                num /= 10;
            }
            arr
        }
        let mut ans = Vec::new();
        for num in nums {
            for d in to_arr(num).iter().rev() {
                ans.push(*d);
            }
        }
        ans
    }
}
