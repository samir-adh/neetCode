struct Item {
    height: i32,
    index: usize,
}

struct Stack<T> {
    items : Vec<T>
}

impl<T> Stack<T> {
    fn push(&mut self, item: T) {
        self.items.push(item);
    }

    fn peek(&self) -> &T {
        return self.items.last().expect("Called 'peek' on empty stack.");
    }

    fn pop(&mut self) -> T {
        return self.items.pop().expect("Called 'pop' on empty stack.");
    }

    fn new() -> Stack<T> {
        return Stack { items: vec![] };
    }

    fn is_empty(&self) -> bool {
        return self.items.is_empty();
    }
}

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut padded_heights = heights.clone();
        padded_heights.push(0);
        let n = padded_heights.len();
        let mut max_area = 0;
        let mut stack = Stack::new();
        stack.push(Item{
            height: padded_heights[0],
            index : 0
        });
        for i in 1..n {
            let mut item = Item {
                height: padded_heights[i],
                index : i,
            };
            while !stack.is_empty() && padded_heights[i] < stack.peek().height {
                let removed_item = stack.pop();
                let j = removed_item.index;
                let k = removed_item.height;
                let area = (i-j) as i32 * k;
                max_area = max_area.max(area);
                item.index = j;
            }
            stack.push(item);
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

    #[test]
    fn test_case_3() {
        let heights: Vec<i32> = vec![2,1,2];
        assert_eq!(Solution::largest_rectangle_area(heights), 3);
    }
}
