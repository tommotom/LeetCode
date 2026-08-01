impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        fn helper1(p1: i32, p2: i32, l: usize, r: usize, nums: &Vec<i32>) -> bool {
            if l > r  || r == usize::MAX {
                return p1 >= p2;
            }
            helper2(p1 + nums[l], p2, l + 1, r, nums) || helper2(p1 + nums[r], p2, l, r - 1, nums)
        }
        fn helper2(p1: i32, p2: i32, l: usize, r: usize, nums: &Vec<i32>) -> bool {
            if l > r  || r == usize::MAX {
                return p1 >= p2;
            }
            helper1(p1, p2 + nums[l], l + 1, r, nums) && helper1(p1, p2 + nums[r], l, r - 1, nums)
        }
        helper1(0, 0, 0, nums.len()-1, &nums)
    }
}
