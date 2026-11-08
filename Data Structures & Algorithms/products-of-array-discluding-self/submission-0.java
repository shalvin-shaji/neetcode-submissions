class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int product_rev = 1;
        int a[] = new int[nums.length];
        int b[] = new int[nums.length];
        int result[] = new int[nums.length];
        for(int i=0; i<nums.length; i++) {
            a[i] = product;
            b[i] = product_rev;
            product *= nums[i];
            product_rev *= nums[nums.length-i-1];
        }
        for(int i=0; i<nums.length; i++){
            result[i] = a[i] * b[nums.length-i-1];
            System.out.println(a[i] + " " + b[i]);
        }
        return result;
    }
}  
