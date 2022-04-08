import java.lang.annotation.Target;

import javax.sound.sampled.ReverbType;

class Test {
    public static void main(String[] args){
        int[] arr = {1, 2, 3, 5, 6, 99, 120, 899, 2555, 500000};
        
        System.out.println(binarySearch(arr, 899));
        System.out.println(binarySearch(arr, 8909));
    }

    public static boolean binarySearch(int[] arr, int value){
        int first = 0;
        int last = arr.length - 1;
        while (first < last) {
            int midpoint = (int) (last + first) / 2;

            if (arr[midpoint] == value){
                return true;
            }

            else if (value < arr[midpoint]){
                last = midpoint - 1;
            }

            else if (value > arr[midpoint]){
                first = midpoint + 1;
            }
        }

        return false;
    }
}