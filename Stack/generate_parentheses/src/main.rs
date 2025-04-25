use std::i32;

struct Solution;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut out = vec![];
        let mut stack = vec![State {
            text: String::from(""),
            open: 0,
            close: 0,
        }];
        while stack.len() > 0 {
            let current = stack
                .pop()
                .expect("'pop' was called on the stack although it was empty.");
            if current.open > 0 {
                // Case where we can close a parentheses
                let new = State {
                    text: current.text.clone() + ")",
                    open: current.open - 1,
                    close: current.close + 1,
                };
                if new.close == n {
                    // If we have close n parentheses then we made a complete combination
                    out.push(new.text);
                } else {
                    // Else we add the new state to the stack
                    stack.push(new);
                }
            }
            if current.open + current.close < n {
                // Case where we open a parentheses
                let new = State {
                    text: current.text.clone() + "(",
                    open: current.open + 1,
                    close: current.close,
                };
                stack.push(new) // Since we just opened a parentheses we still have to close it so we add the new state to the stack
            }
        }
        return out;
    }
}

struct State {
    text: String,
    open: i32,
    close: i32,
}

fn main() {
    return;
}

#[cfg(test)]
mod tests {
    use super::*;

    fn sorted(mut v: Vec<String>) -> Vec<String> {
        v.sort();
        v
    }

    #[test]
    fn test_n_0() {
        let result = Solution::generate_parenthesis(0);
        assert_eq!(result, Vec::<String>::new());
    }

    #[test]
    fn test_n_1() {
        let result = Solution::generate_parenthesis(1);
        assert_eq!(sorted(result), vec!["()"]);
    }

    #[test]
    fn test_n_2() {
        let result = Solution::generate_parenthesis(2);
        assert_eq!(sorted(result), sorted(vec!["(())".to_string(), "()()".to_string()]));
    }

    #[test]
    fn test_n_3() {
        let result = Solution::generate_parenthesis(3);
        assert_eq!(
            sorted(result),
            sorted(vec![
                "((()))".to_string(),
                "(()())".to_string(),
                "(())()".to_string(),
                "()(())".to_string(),
                "()()()".to_string()
            ])
        );
    }

    #[test]
    fn test_n_4_len() {
        let result = Solution::generate_parenthesis(4);
        // Catalan number C4 = 14
        assert_eq!(result.len(), 14);
    }
}
