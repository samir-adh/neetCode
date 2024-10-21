struct Solution;

impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 {
            return nums[0];
        }
        let mut nums_copy = nums.clone();
        while nums_copy.len() > 2 {
            let last = nums_copy.len() -1;
            let mid = nums_copy.len() / 2;
            let mid_value = nums_copy[mid];
            let last_value = nums_copy[last];
            if mid_value > last_value {
                nums_copy = nums_copy.split_at(mid).1.to_vec();
            } else if mid_value == last_value {
                return mid_value;
            } else {
                nums_copy = nums_copy.split_at(mid + 1).0.to_vec();
            }
        }
        let (v0, v1) = (nums_copy[0], nums_copy[1]);
        if v0 < v1 {
            return v0;
        } else {
            return v1;
        }
    }
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let nums = vec![3, 4, 5, 1, 2];
        let expected_answer = 1;
        assert_eq!(Solution::find_min(nums), expected_answer);
    }

    #[test]
    fn example2() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let expected_answer = 0;
        assert_eq!(Solution::find_min(nums), expected_answer);
    }

    #[test]
    fn example3() {
        let nums = vec![11, 13, 15, 17];
        let expected_answer = 11;
        assert_eq!(Solution::find_min(nums), expected_answer);
    }

    #[test]
    fn example4() {
        let nums = vec![1];
        let expected_answer = 1;
        assert_eq!(Solution::find_min(nums), expected_answer);
    }
}
