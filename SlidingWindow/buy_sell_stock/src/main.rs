impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut buy = 0;
        let mut sell = 0;
        let mut profit = 0;
        let n = prices.len();
        for i in 0..n {
            if prices[i] > prices[sell] {
                sell = i;
            }
            if prices[i] < prices[buy] {
                buy = i;
                sell = i;
            }
            profit = profit.max(prices[sell] - prices[buy]);
        }
        return profit;
    }
}

struct Solution;

fn main() {}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn test_case_1() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        assert_eq!(Solution::max_profit(prices), 5)
    }

    #[test]
    fn test_case_2() {
        let prices = vec![7, 6, 4, 3, 1];
        assert_eq!(Solution::max_profit(prices), 0)
    }
}
