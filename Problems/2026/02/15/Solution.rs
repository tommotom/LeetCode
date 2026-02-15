impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a: Vec<char> = a.chars().collect();
        let b: Vec<char> = b.chars().collect();

        let mut ans = Vec::new();
        let mut i = a.len() - 1;
        let mut j = b.len() - 1;
        let mut k = 0;
        let mut carry = 0;
        loop {
            let mut d = carry;
            if a[i-k] == '1' {
                d += 1;
            }
            if b[j-k] == '1' {
                d += 1;
            }
            if d > 1 {
                carry = 1;
                d -= 2;
            } else {
                carry = 0;
            }
            ans.push(d.to_string());
            k += 1;
            if i < k || j < k {
                break;
            }
        }
        while i >= k {
            let mut d = carry;
            if a[i-k] == '1' {
                d += 1;
            }
            if d > 1 {
                carry = 1;
                d -= 2;
            } else {
                carry = 0;
            }
            ans.push(d.to_string());
            k += 1;
            if i < k {
                break;
            }
        }
        while j >= k {
            let mut d = carry;
            if b[j-k] == '1' {
                d += 1;
            }
            if d > 1 {
                carry = 1;
                d -= 2;
            } else {
                carry = 0;
            }
            ans.push(d.to_string());
            k += 1;
            if j < k {
                break;
            }
        }
        if carry > 0 {
            ans.push('1'.to_string());
        }
        ans = ans.into_iter().rev().collect();

        ans.concat()
    }
}
