impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let n = boxes.len();
        let boxes: Vec<i32> = boxes.chars().map(|c| c as i32 - '0' as i32).collect();

        let mut l_to_r = vec![0; n];
        let mut r_to_l = vec![0; n];

        let mut ones_l = 0;
        let mut ones_r = 0;

        for i in 0..n {
            l_to_r[i] = if i > 0 { l_to_r[i - 1] } else { 0 } + ones_l;
            ones_l += boxes[i];

            r_to_l[n-i-1] = if i > 0 { r_to_l[n-i] } else { 0 } + ones_r;
            ones_r += boxes[n-i-1];
        }

        (0..n).map(|i| l_to_r[i] + r_to_l[i]).collect()
    }
}
