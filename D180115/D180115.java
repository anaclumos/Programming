/*
Developed by Sunghyun Cho on January 15th, 2018.

Challenge:
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
*/

class FindMedianSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] all = new int[nums1.length+nums2.length];
        for(int x = 0; x < nums1.length; x++)
            all[x] = nums1[x];
        for(int x = 0; x < nums2.length; x++)
            all[nums1.length+x] = nums2[x];
        Arrays.sort(all);
        if(all.length%2==0) return (all[all.length/2-1]+all[all.length/2])/2.0;
            else return all[all.length/2];
    }
}