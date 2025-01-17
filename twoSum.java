import java.util.Arrays;

public class twoSum {
    public static void main(String args[]) {
        int nums[] = { 2, 7, 11, 15 };
        int res[] = new int[2];
        int target = 9;
        for (int i = 0; i <= nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                }
            }
        }
        System.out.println(Arrays.toString(res));
    }
}