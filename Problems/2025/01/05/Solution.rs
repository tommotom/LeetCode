impl Solution {
    pub fn shifting_letters(s: String, mut shifts: Vec<Vec<i32>>) -> String {
        let n = shifts.len();
        let mut starts = Vec::new();
        let mut ends = Vec::new();
        for i in 0..n {
            starts.push([shifts[i][0], shifts[i][2]]);
            ends.push([shifts[i][1], shifts[i][2]]);
        }
        starts.sort_by(|a, b| a[0].cmp(&b[0]));
        ends.sort_by(|a, b| a[0].cmp(&b[0]));

        let mut d = 0;
        let mut s_i = 0;
        let mut e_i = 0;
        let mut ans = "".to_owned();
        for (i, c) in s.chars().enumerate() {
            while s_i < starts.len() && i >= starts[s_i][0] as usize {
                d += if starts[s_i][1] == 1 {1} else {25};
                d %= 26;
                s_i += 1;
            }
            while e_i < ends.len() && i > ends[e_i][0] as usize {
                d += if ends[e_i][1] == 1 {25} else {1};
                d %= 26;
                e_i += 1;
            }
            ans.push(((c.to_ascii_lowercase() as u8 - 97 + d) % 26 + 97) as char);
        }
        ans
    }
}
