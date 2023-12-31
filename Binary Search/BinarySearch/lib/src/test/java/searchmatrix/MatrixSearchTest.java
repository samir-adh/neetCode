/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package searchmatrix;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class MatrixSearchTest {
    @Test
    void searchTest1() {
        Solution solution = new Solution();
        int[][] nums = new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } };
        int target = 3;
        boolean answer = true;
        boolean output = solution.searchMatrix(nums, target);
        String message = String.format("search(%s,%d) should return '%s'", Arrays.toString(nums), target,
                Boolean.toString(answer));
        assertEquals(answer, output, message);
    }
    @Test
    void searchTest2() {
        Solution solution = new Solution();
        int[][] nums = new int[][] { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } };
        int target = 13;
        boolean answer = false;
        boolean output = solution.searchMatrix(nums, target);
        String message = String.format("search(%s,%d) should return '%s'", Arrays.toString(nums), target,
                Boolean.toString(answer));
        assertEquals(answer, output, message);
    }
    @Test
    void searchTest3() {
        Solution solution = new Solution();
        int[][] nums = new int[][] { { 1, 1 } };
        int target = 0;
        boolean answer = false;
        boolean output = solution.searchMatrix(nums, target);
        String message = String.format("search(%s,%d) should return '%s'", Arrays.toString(nums), target,
                Boolean.toString(answer));
        assertEquals(answer, output, message);
    }
    @Test
    void searchTest4() {
        Solution solution = new Solution();
        int[][] nums = new int[][] { { 1 },{ 3 } };
        int target = 3;
        boolean answer = true;
        boolean output = solution.searchMatrix(nums, target);
        String message = String.format("search(%s,%d) should return '%s'", Arrays.toString(nums), target,
                Boolean.toString(answer));
        assertEquals(answer, output, message);
    }
}
