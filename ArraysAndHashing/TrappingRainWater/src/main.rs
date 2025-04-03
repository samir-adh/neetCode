struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut total = 0;
        let n = height.len();
        let mut max_l = vec![0; n];
        let mut max_r = vec![0; n];
        let mut max_l_tmp = 0;
        let mut max_r_tmp = 0;
        for k in 0..n {
            // Left side
            max_l[k] = max_l_tmp;
            max_l_tmp = i32::max(height[k], max_l_tmp);
            // Right side
            max_r[n-k-1] = max_r_tmp;
            max_r_tmp = i32::max(height[n-k-1], max_r_tmp);
        }
        for k in 0..n {
            total += i32::max(0, i32::min(max_l[k], max_r[k]) - height[k]);
        }
        return total;
    }
}

fn main() {
    println!("Hello world");
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_case_1() {
        let heights = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        assert!(Solution::trap(heights) == 6);
    }
}
