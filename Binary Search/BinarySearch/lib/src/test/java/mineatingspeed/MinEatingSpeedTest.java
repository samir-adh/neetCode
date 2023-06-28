package mineatingspeed;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class MinEatingSpeedTest {
    @Test
    void minEatingSpeedTest1() {
        Solution solution = new Solution();
        int[] piles = new int[] { 3, 6, 7, 11 };
        int h = 8;
        int answer = 4;
        int output = solution.minEatingSpeed(piles, h);
        String message = String.format("search(%s,%d) should return '%d' but returned '%d'.", Arrays.toString(piles), h,
                answer, output);
        assertEquals(answer, output, message);
        return;
    }

    @Test
    void minEatingSpeedTest2() {
        Solution solution = new Solution();
        int[] piles = new int[] { 30, 11, 23, 4, 20 };
        int h = 5;
        int answer = 30;
        int output = solution.minEatingSpeed(piles, h);
        String message = String.format("search(%s,%d) should return '%d' but returned '%d'.", Arrays.toString(piles), h,
                answer, output);
        assertEquals(answer, output, message);
        return;
    }

    @Test
    void minEatingSpeedTest3() {
        Solution solution = new Solution();
        int[] piles = new int[] { 30, 11, 23, 4, 20 };
        int h = 6;
        int answer = 23;
        int output = solution.minEatingSpeed(piles, h);
        String message = String.format("search(%s,%d) should return '%d' but returned '%d'.", Arrays.toString(piles), h,
                answer, output);
        assertEquals(answer, output, message);
        return;
    }

    @Test
    void minEatingSpeedTest4() {
        Solution solution = new Solution();
        int[] piles = new int[] { 312884470 };
        int h = 968709470;
        int answer = 1;
        int output = solution.minEatingSpeed(piles, h);
        String message = String.format("search(%s,%d) should return '%d' but returned '%d'.", Arrays.toString(piles), h,
                answer, output);
        assertEquals(answer, output, message);
        return;
    }
    // [805306368,805306368,805306368]

    @Test
    void minEatingSpeedTest5() {
        Solution solution = new Solution();
        int[] piles = new int[] { 805306368,805306368,805306368 };
        int h = 1000000000;
        int answer = 3;
        int output = solution.minEatingSpeed(piles, h);
        String message = String.format("search(%s,%d) should return '%d' but returned '%d'.", Arrays.toString(piles), h,
                answer, output);
        assertEquals(answer, output, message);
        return;
    }
}