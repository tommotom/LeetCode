impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let num = num.chars().collect::<Vec<char>>();
        let mut max = std::string::String::from("");
        for i in 2..num.len() {
            if num[i-2] == num[i-1] && num[i-1] == num[i] {
                max = max.max([num[i-2], num[i-1], num[i]].iter().collect::<String>());
            }
        }
        max
    }
}
