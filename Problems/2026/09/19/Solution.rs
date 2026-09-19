impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        if x_center < x1 {
            if y_center < y1 {
                return (x1 - x_center).pow(2) + (y1 - y_center).pow(2) <= radius.pow(2);
            } else if y_center <= y2 {
                return x1 <= x_center + radius;
            } else {
                return (x1 - x_center).pow(2) + (y_center - y2).pow(2) <= radius.pow(2);
            }
        } else if x_center <= x2 {
            if y_center < y1 {
                return y1 <= y_center + radius;
            } else if y_center <= y2 {
                return true;
            } else {
                return y_center - radius <= y2;
            }
        } else {
            if y_center < y1 {
                return (x_center - x2).pow(2) + (y1 - y_center).pow(2) <= radius.pow(2);
            } else if y_center <= y2 {
                return x_center - radius <= x2;
            } else {
                return (x_center - x2).pow(2) + (y_center - y2).pow(2) <= radius.pow(2);
            }
        }
    }
}
