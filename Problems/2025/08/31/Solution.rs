impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        fn helper(r: usize, c: usize, board: &mut Vec<Vec<char>>) -> bool {
            if r == 9 {
                return true;
            }
            if board[r][c] != '.' {
                return helper(r + (c + 1) / 9, (c + 1) % 9, board);
            }
            for num in 1..10 {
                let mut isValid = true;
                let (rr, cc) = (r / 3 * 3, c / 3 * 3);
                let cha = char::from_digit(num, 10).unwrap();

                for i in 0..9 {
                    if board[i][c] == cha || board[r][i] == cha || board[rr+(i/3)][cc+i%3] == cha {
                        isValid = false;
                        break;
                    }
                }
                if !isValid {
                    continue;
                }
                board[r][c] = cha;
                if helper(r + (c + 1) / 9, (c + 1) % 9, board) {
                    return true;
                }
                board[r][c] = '.';
            }
            false
        }
        helper(0, 0, board);
    }
}
