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
                    break;
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
                break;
            }

        }
        System.out.println(Arrays.toString(resArray));

    }

    public static void main(String args[]) {
        int nums[] = new int[10000];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = i + 1; // Fill the array with numbers 1 to 10000
        }
        int target = 15000;
        twoSum s = new twoSum();

        // Measure time for sumTwo
        long start1 = System.nanoTime();
        s.sumTwo(nums, target);
        long end1 = System.nanoTime();
        long duration1 = end1 - start1;
        System.out.println("Execution time (sumTwo): " + duration1 + " nanoseconds");

        // Measure time for sumV2
        long start2 = System.nanoTime();
        s.sumV2(nums, target);
        long end2 = System.nanoTime();
        long duration2 = end2 - start2;
        System.out.println("Execution time (sumV2): " + duration2 + " nanoseconds");
    }
}