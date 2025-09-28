use std::collections::HashMap;

impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        if numerator == 0 { return "0".to_string(); }
        let neg = (numerator < 0) ^ (denominator < 0);
        let numerator = (numerator as i64).abs();
        let denominator = (denominator as i64).abs();
        let mut outstring = "".to_string();
        if neg {
            outstring += &"-".to_string();
        }
        let mut cur_rem = numerator % denominator;
        outstring += &(numerator / denominator).to_string();
        if cur_rem == 0 {
            return outstring;
        }
        outstring+= &".".to_string();
        let mut decimalsvec: Vec<String> = Vec::new();
        let mut rem_map: HashMap<i64, usize> = HashMap::new();
        while cur_rem != 0 {
            if rem_map.contains_key(&cur_rem) {
                decimalsvec.insert(*rem_map.get(&cur_rem).unwrap(), "(".to_string());
                decimalsvec.push(")".to_string());
                break;
            }
            rem_map.insert(cur_rem, decimalsvec.len());
            cur_rem *= 10;
            let newval = cur_rem / denominator;
            cur_rem = cur_rem % denominator;
            decimalsvec.push(newval.to_string());
        }
        outstring += &decimalsvec.join("");
        outstring
    }
}
