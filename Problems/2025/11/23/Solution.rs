impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        let mut zero = Vec::new();
        let mut one = Vec::new();
        let mut two = Vec::new();
        let mut sum = 0;
        for num in nums {
            if num % 3 == 0 {
                zero.push(num);
            } else if num % 3 == 1 {
                one.push(num);
            } else {
                two.push(num);
            }
            sum += num;
        }
        one.sort();
        two.sort();

        if sum % 3 == 1 {
            if one.len() > 0 && two.len() > 1 {
                return sum - one[0].min(two[0] + two[1]);
            } else if one.len() > 0 {
                return sum - one[0];
            } else {
                return sum - two[0] - two[1];
            }
        } else if sum % 3 == 2 {
            if one.len() > 1 && two.len() > 0 {
                return sum - two[0].min(one[0] + one[1]);
            } else if two.len() > 0 {
                return sum - two[0];
            } else {
                return sum - one[0] - one[1];
            }
        }
        sum
    }
}
