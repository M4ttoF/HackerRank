import java.util.*;
public class Solution {
    public int[] twoSum(int[] nums, int targ) {
    	for(int i=0;i<nums.length;i++){
    		for(int j=0;j<nums.length;j++){
    			int num=nums[i]+nums[j];
    			if(num==targ && i!=j){
    				int[]soln={i,j};
    				return soln;
    			}
    		}
    	}
    	return null;
    }
}