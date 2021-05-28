/*
Date:19-05-2021

quicksort_java

*/
public class quickSort{

    public static void main(String[] args){
        double[] seqnum = {4,8,2,7,5,6,9,3,1,1.5,-30,100};
        double[] sorted;
        int n = seqnum.length;
   
        sorted = quickSort(seqnum,0,n-1);
        for(int i = 0;i < sorted.length;i++){
            System.out.println("Java:" + sorted[i]);
        }
    }

    static double[] quickSort(double[] a,int p,int r){
        if(p >=r){
            return a;
        }
        else{
            int q = partition(a,p,r);
            quickSort(a, p, q - 1);
            quickSort(a, q + 1, r);
            return a;
        }
        
    }

    static int partition(double[] a,int p,int r){
        double x = (a[r]);
        int i = p - 1;
        int j;
        for (j = p ;j<=r - 1 ;j++){
            if(a[j]<=x){
                i = i +1;
                double temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        double temp = a[i+1];
        a[i+1] = a[r];
        a[r] = temp;
        return i + 1;
    }
    
}