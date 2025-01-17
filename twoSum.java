import java.util.ArrayList;
import java.util.Arrays;

public class twoSum {

    public static void sumTwo(int nums[], int target) {
        int res[] = new int[2];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                }
            }
        }
        System.out.println(Arrays.toString(res));
    }

    public static void sumV2(int nums[], int target) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            a.add(nums[i]);
        }
        int res = 0;
        int resArray[] = new int[2];
        for (int i = 0; i < a.size(); i++) {
            res = target - a.get(i);
            if (a.contains(res)) {
                resArray[0] = i;
                resArray[1] = a.indexOf(res);
            }

        }
        System.out.println(Arrays.toString(resArray));

    }

    public static void main(String args[]) {
        int nums[] = { 2, 7, 11, 15 };
        int target = 9;
        twoSum s = new twoSum();
        s.sumTwo(nums, target);
        s.sumV2(nums, target);
    }
}