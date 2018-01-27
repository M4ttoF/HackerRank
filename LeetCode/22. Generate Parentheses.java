public class Solution {
    public List<String> generateParenthesis(int n) {
        //int count = line.length() - line.replace(".", "").length();
        List<String>ans=new ArrayList<String>();
        if(n==1){
            ans.add("()");
            return ans;
        }
        else{
            int open,close;
            open=n-1;
            close=n;
            genPar("(",open,close,ans);
            return ans;
        }
        
    }
    public static void genPar(String s, int leftO, int leftC,List<String> answer){
        if(leftO==0 && leftC==0){
            answer.add(s);
        }
        if(leftO>0){
            genPar(s+"(",leftO-1,leftC,answer);
        }
        if(leftO<leftC){
            genPar(s+")",leftO,leftC-1,answer);
        }
        
    }
}