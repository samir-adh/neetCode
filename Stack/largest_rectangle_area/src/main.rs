struct Item {
    value: i32,
    left: i32,
    right: i32,
}

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let n = heights.len();
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return heights[0];
        }
        let mut areas: Vec<i32> = heights.iter().map(|_x| 0).collect();
        for i in 0..n {
            let i_val = heights[i];
            let mut left = -1;
            for j in 1..(i + 1) {
                let j_val = heights[i - j];
                if j_val < i_val {
                    left = (i - j) as i32;
                    break;
                }
            }
            let mut right = n as i32;
            for k in 1..(n - i) {
                let k_val = heights[i + k];
                if k_val < i_val {
                    right = (i + k) as i32;
                    break;
                }
            }
            areas[i] = (right - left - 1) * i_val
        }
        let mut max_area = areas[0];
        for i in 1..n {
            if max_area < areas[i] {
                max_area = areas[i];
            }
        }
        return max_area;
    }
}

struct Solution;

fn main() {}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_case_0() {
        let heights: Vec<i32> = vec![];
        assert_eq!(Solution::largest_rectangle_area(heights),0);
    }

    #[test]
    fn test_case_1() {
        let heights: Vec<i32> = vec![2,1,5,6,2,3];
        assert_eq!(Solution::largest_rectangle_area(heights), 10);
    }

    #[test]
    fn test_case_2() {
        let heights: Vec<i32> = vec![2,4];
        assert_eq!(Solution::largest_rectangle_area(heights), 4);
    }
}
