struct Spreadsheet {
    matrix: Vec<Vec<i32>>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Spreadsheet {

    fn new(rows: i32) -> Self {
        let mut matrix = vec![vec![0; 26]; rows as usize];
        Self {
            matrix
        }
    }

    fn cell_to_coordinate(&self, cell: String) -> (usize, usize) {
        let col = cell[..1].chars().next().unwrap() as u8 - 'A' as u8;
        let row = cell[1..].parse::<usize>().unwrap();
        (col as usize, row - 1)
    }

    fn set_cell(&mut self, cell: String, value: i32) {
        let (col, row) = self.cell_to_coordinate(cell);
        self.matrix[row][col] = value;
    }

    fn reset_cell(&mut self, cell: String) {
        self.set_cell(cell, 0);
    }

    fn is_numeric(&self, s: &str) -> bool {
        s.chars().all(|c| c.is_ascii_digit())
    }

    fn resolve_value(&self, s: &str) -> i32 {
        if self.is_numeric(s) {
            return s.parse::<i32>().unwrap();
        } else {
            let (col, row) = self.cell_to_coordinate(s.to_string());
            return self.matrix[row][col];
        }
    }

    fn get_value(&self, formula: String) -> i32 {
        formula[1..].split('+').map(|s| self.resolve_value(s)).sum()
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet::new(rows);
 * obj.set_cell(cell, value);
 * obj.reset_cell(cell);
 * let ret_3: i32 = obj.get_value(formula);
 */
