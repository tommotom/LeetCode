impl Solution {
    pub fn find_gcd(mut nums: Vec<i32>) -> i32 {
        fn gcd(a: i32, b: i32) -> i32 {
            if b == 0 {
                return a;
            }
            gcd(b, a % b)
        }
        nums.sort();
        gcd(nums[nums.len()-1], nums[0])
    }
}
