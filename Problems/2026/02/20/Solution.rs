impl Solution {
    pub fn make_largest_special(s: String) -> String {
        let mut count = 0;
        let mut list = Vec::new();
        let s_chars: Vec<char> = s.chars().collect();
        let mut j = 0;

        for i in 0..s.len() {
            count += if s_chars[i] == '1' { 1 } else { -1 };

            if count == 0 {
                let temp_string: String = s_chars[(j+1)..i].iter().collect();
                let temp = Self::make_largest_special(temp_string);
                list.push(format!("1{}0", temp));
                j = i + 1;
            }
        }

        list.sort_by(|a, b| b.cmp(a));
        list.concat()
    }
}

