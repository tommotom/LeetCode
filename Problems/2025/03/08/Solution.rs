impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let chars: Vec<char> = blocks.chars().collect();
        let mut whites = 0;
        for i in 0..k as usize {
            if chars[i] == 'W' {
                whites += 1;
            }
        }

        let mut ans = whites;
        for i in (k as usize)..chars.len() {
            if chars[i] == 'W' {
                whites += 1;
            }
            if chars[i - k as usize] == 'W' {
                whites -= 1;
            }
            ans = ans.min(whites);
        }

        ans
    }
}
