impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut buy = 0;
        let mut sell = 0;
        let mut profit = 0;
        let mut holding = false;
        let n = prices.len();
        if n == 0 {
            return 0;
        }
        for i in 0..n - 1 {
            if sell == i {
                profit += prices[sell] - prices[buy];
                holding = false;
            }
            if buy ==  i {
                holding = true;
            }
            if prices[i] <= prices[i + 1] {
                if !holding {
                    buy = i;
                    holding = true;
                }
                sell = i + 1
            } else {
                if holding {
                    sell = i;
                    holding = false;
                    profit += prices[sell] - prices[buy];
                }
                buy = i + 1;
            }
        }
        if holding {
            profit += prices[n-1] - prices[buy];
        }
        return profit;
    }
}

struct Solution {}

fn main() {}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn test_case_0() {
        let prices: Vec<i32> = vec![];
        assert_eq!(Solution::max_profit(prices), 0);
    }

    #[test]
    fn test_case_1() {
        let prices: Vec<i32> = vec![7, 1, 5, 3, 6, 4];
        assert_eq!(Solution::max_profit(prices), 7);
    }

    #[test]
    fn test_case_2() {
        let prices: Vec<i32> = vec![1, 2, 3, 4, 5];
        assert_eq!(Solution::max_profit(prices), 4);
    }

    #[test]
    fn test_case_3() {
        let prices: Vec<i32> = vec![7, 6, 4, 3, 1];
        assert_eq!(Solution::max_profit(prices), 0);
    }
}
