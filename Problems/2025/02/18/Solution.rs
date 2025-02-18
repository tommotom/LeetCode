impl Solution {
    pub fn smallest_number(pattern: String) -> String {
        let mut nums = vec![0 as usize; pattern.len()+1];
        let mut used = vec![false; 10];
        Self::helper(0, &pattern.chars().collect(), &mut nums, &mut used);
        nums.into_iter().map(|u| char::from_digit(u as u32, 10).unwrap()).collect()
    }

    fn helper(i: usize, pattern: &Vec<char>, nums: &mut Vec<usize>, used: &mut Vec<bool>) -> bool {
        if (i == pattern.len()+1) {
            return true;
        }
        for num in 1..10 {
            if used[num] {
                continue;
            }
            if i > 0 && pattern[i-1] == 'I' && nums[i-1] >= num {
                continue;
            }
            if i > 0 && pattern[i-1] == 'D' && nums[i-1] <= num {
                continue;
            }
            used[num] = true;
            nums[i] = num;
            if Self::helper(i+1, pattern, nums, used) {
                return true;
            }
            used[num] = false;
        }
        false
    }
}
