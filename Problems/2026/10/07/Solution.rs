impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        fn remove(
            text: String,
            scan_start: usize,
            delete_start: usize,
            open: u8,
            close: u8,
            answers: &mut Vec<String>,
        ) {
            let bytes = text.as_bytes();
            let mut balance = 0i32;

            for i in scan_start..bytes.len() {
                if bytes[i] == open {
                    balance += 1;
                } else if bytes[i] == close {
                    balance -= 1;
                }

                if balance >= 0 {
                    continue;
                }

                for j in delete_start..=i {
                    if bytes[j] == close
                        && (
                            j == delete_start
                            || bytes[j - 1] != close
                        )
                    {
                        let mut child =
                            String::with_capacity(text.len() - 1);

                        child.push_str(&text[..j]);
                        child.push_str(&text[j + 1..]);

                        remove(
                            child, i, j, open, close, answers
                        );
                    }
                }

                return;
            }

            let reversed: String = text.chars().rev().collect();

            if open == b'(' {
                remove(reversed, 0, 0, b')', b'(', answers);
            } else {
                answers.push(reversed);
            }
        }

        let mut answers = Vec::new();
        remove(s, 0, 0, b'(', b')', &mut answers);
        answers
    }
}
