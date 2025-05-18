impl Solution {
    fn sort_colors(nums: &mut Vec<i32>) {
        let (mut zero, mut one, mut two) = (0, 0, 0);

        for &n in nums.iter() {
            match n {
                0 => zero += 1,
                1 => one += 1,
                2 => two += 1,
                _ => {}
            }
        }

        for i in 0..nums.len() {
            if zero > 0 {
                nums[i] = 0;
                zero -= 1;
            } else if one > 0 {
                nums[i] = 1;
                one -= 1;
            } else {
                nums[i] = 2;
                two -= 1;
            }
        }
    }
}
