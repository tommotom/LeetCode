impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let (mut l, mut r, mut ans) = (0, height.len()-1, 0);
        while l < r {
            ans = ans.max((r - l) as i32 * height[l].min(height[r]));
            if height[l] < height[r] {
                l += 1;
            } else {
                r -= 1;
            }
        }
        ans
    }
}
