package searchmatrix;

public class Solution {
    private int get(int[][] matrix, int index){
        return matrix[index/(matrix[0].length)][index%matrix[0].length];
    }
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length * matrix[0].length;
        int a = 0;
        int b = n-1;
        while (b-a > 1){
            if (get(matrix,a + (b-a)/2) < target){
                a += (b-a)/2;
            }
            else {
                b -= (b-a)/2;
            }
        }
        return (get(matrix,a)==target)||(get(matrix,b)==target);
    }
}
