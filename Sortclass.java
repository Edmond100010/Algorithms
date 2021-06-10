import java.util.Arrays;


/*
Reference:
https://www.educative.io/edpresso/how-to-implement-a-merge-sort-in-java (mergesort)



*/


public class Sortclass {
    private String str;
    private char[] chararray;
    private int[] intarrray;
    private double[] doublearrray;
    private double[] doublearrraysort;

    private int i = 0;


    public Sortclass(String a){
        str = a;
        doublearrraysort = new double[(a.length())];
        while( i < a.length()){
            doublearrraysort[i] = Double.valueOf(a.charAt(i));
            i++;
        }
    }
    public Sortclass(char[] a){
        chararray = a;
        doublearrraysort = new double[a.length];
        while( i < a.length){
            doublearrraysort[i] = Double.valueOf(a[i]);
            i++;
        }

    }
  
    public Sortclass(int[] a){
        doublearrraysort = new double[(a.length)];
        while( i < a.length){
            doublearrraysort[i] = Double.valueOf(a[i]);
            i++;
        }
        intarrray = a;
    }    


    public Sortclass(double[] a){
        doublearrray = a;
        doublearrraysort = a;
    }

    public String getsort(){
        if(str != null){
            return str;
        }else if(intarrray != null){
            return Arrays.toString(intarrray);
        }else if(doublearrray != null){
            return Arrays.toString(doublearrray);
        }else if(chararray != null){
            return Arrays.toString(chararray);
        }else
            return null;
    }

    public void insertionsort(){
        System.out.println("Insertion sort:");
        int j;
        double temp;
        for (int i =0;i<doublearrraysort.length;i++){
            j = i - 1;
            while( j >= 0 && doublearrraysort[j] > doublearrraysort[j+1]){
                temp = doublearrraysort[j];
                doublearrraysort[j] = doublearrraysort[j+1];
                doublearrraysort[j+1] = temp;
                j=j-1;
            }
        }
        converttype();
    }

    public void selectionsort(){
        System.out.println("Selection sort:");
        double temp;
        for ( i = 0;i < doublearrraysort.length;i++){
            for(int j = i + 1;j < doublearrraysort.length;j++){
                if(doublearrraysort[i]>doublearrraysort[j]){
                    temp = doublearrraysort[i];
                    doublearrraysort[i] = doublearrraysort[j];
                    doublearrraysort[j] = temp;
                }
            }
        }
        converttype();
    }

    public void mergesort(){
        doublearrraysort = mergesortrun(doublearrraysort);
        converttype();
    }




    /*private double[] mergesortrun(double[] a){        old version
        if(a.length<2){
            return a;
        }
        int len = a.length;
        int mid = len/2;
        double [] l = new double[mid];
        double [] r = new double[len-mid];
        int k = 0;
        
        l = Arrays.copyOf(a, mid);
        for(int i = 0;i<mid;i++){                         old version
            l[i] = a[i];
        }
        for(int i = mid;i<a.length;i++){
            r[r.length-(a.length-i)] = a[i];
        }

        mergesortrun(l);
        mergesortrun(r);
        int i = 0;
        int j = 0;
        k = 0;
        while(i<l.length && j<r.length){
            if(l[i] < r[j]){
                a[k++] = l[i++];
            }else{
                a[k++] = r[j++];
            }
        }
        while(i<l.length){
            a[k++] = l[i++];
        }
        while(j<r.length){
            a[k++] = r[j++];
        }
        return a;
    }*/

    private double[] mergesortrun(double[] a){            
        if(a.length<2){
            return a;
        }
        int len = a.length;
        int mid = len/2;
        double [] l = new double[mid];
        double [] r = new double[len-mid];
        int k = 0;
        for(int i = 0;i<len;i++){                            //Reference
            if(i<mid){
                l[i] = a[i];
            }
            else{
                r[k] = a[i];
                k = k+1;
            }
        }
        
        mergesortrun(l);
        mergesortrun(r);
        int i = 0;
        int j = 0;
        k = 0;
        while(i<l.length && j<r.length){
            if(l[i] < r[j]){
                a[k++] = l[i++];
            }else{
                a[k++] = r[j++];
            }
        }
        while(i<l.length){
            a[k++] = l[i++];
        }
        while(j<r.length){
            a[k++] = r[j++];
        }
        return a;
    }

    private void converttype(){
        if(intarrray != null){
            i = 0;
            while( i < doublearrraysort.length){
                intarrray[i] = (int)(doublearrraysort[i]);
                i++;
            }
            System.out.println(Arrays.toString(intarrray));
        }else if(doublearrray != null){
            doublearrray = doublearrraysort;
            System.out.println(Arrays.toString(doublearrray));
        }
        else if(str != null){
            i = 0;
            StringBuilder sb = new StringBuilder(doublearrraysort.length);
            while(i < doublearrraysort.length){
                sb.append((char)(int)doublearrraysort[i]);
                i++;
            }
            str = sb.toString();
            System.out.println(str);
        }else if(chararray!=null){
            i = 0;
            while(i < doublearrraysort.length){
                chararray[i] = (char)(int)doublearrraysort[i];
                i++;
            }
            System.out.println(Arrays.toString(chararray));
        }else System.out.println("null");
    }
}
