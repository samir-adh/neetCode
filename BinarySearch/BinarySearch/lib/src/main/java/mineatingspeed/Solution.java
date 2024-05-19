package mineatingspeed;

public class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int a = 0;
        int b = max(piles);
        while (b-a > 1) {
            int s = (b-a)/2;
            if (eatingTime(piles, a + s) > h){
                a += s;
            }
            else {
                b -= s;
            }
        }
        return b;
    }

    private long eatingTime(int[] piles, int speed) {
        long time = 0;
        for (int i : piles) {
            if (i/speed > 0){
                time += i / speed;
            }
            if (i % speed > 0) {
                time += 1;
            }
        }
        return time;
    }

    private int max(int[] piles){
        int maxValue = 0;
        for (int i : piles) {
            if (i > maxValue) {
                maxValue = i;
            }
        }
        return maxValue;
    }
}