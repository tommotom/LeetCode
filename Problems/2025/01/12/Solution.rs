impl Solution {
    fn helper(s: &Vec<char>, locked: &Vec<char>, rev: bool) -> bool {
        let begin = if rev {')'} else {'('};
        let mut level = 0;
        let mut change = 0;
        for i in 0..s.len() {
            if locked[i] == '0' {
                change += 1;
            } else if s[i] == begin {
                level += 1;
            } else {
                level -= 1;
            }
            if level + change < 0 {
                return false;
            }
        }
        return level + change >= 0 && level <= change;
    }

    pub fn can_be_valid(s: String, locked: String) -> bool {
        if s.len() % 2 == 1 {
            return false;
        }
        let s_chars: Vec<char> = s.chars().collect();
        let locked_chars: Vec<char> = locked.chars().collect();
        return Self::helper(&s_chars, &locked_chars, false) && Self::helper(&s_chars.iter().rev().copied().collect(), &locked_chars.iter().rev().copied().collect(), true);
    }
}
