impl Solution {
    pub fn maximum_gain(mut s: String, x: i32, y: i32) -> i32 {
        if s.len() < 2 { return 0 }
        let (mut pats, mut points) = (vec![('a','b'),('b','a')],vec![x,y]);
        if y > x { pats = vec![('b','a'),('a','b')]; points = vec![y,x];}
        let mut s = s.chars().collect::<Vec<char>>();
        let mut result = 0;
        for pat_idx in 0..pats.len() {
            let (ch1,ch2) = pats[pat_idx];
            let mut stack = vec![s[0]];
            for idx in 1..s.len() {
                if stack.len() >0 && stack[stack.len()-1] == ch1 && s[idx] == ch2 {
                    stack.pop();
                    result += points[pat_idx];
                } else {
                    stack.push(s[idx]);
                }
            }
            if stack.len() == 0 { break };
            s = stack;
        }
        result
    }
}
