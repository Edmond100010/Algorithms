import java.util.Random;

public class main {
    public static void main(String[] args){
        int i =0;
        double[] seqnum = {4,8,2,7,5,6,9,3,1,-30,1.5,100};
        int[] seqnumguess = {5,4,3,2,1}; //19
        char[] chararray = {'a','a','h','v','b'};
        Sortclass S1 = new Sortclass("hell");
        Sortclass S2 = new Sortclass(seqnum);
        Sortclass S3 = new Sortclass(seqnumguess);
        Sortclass S4 = new Sortclass(chararray);
        S1.mergesort();
        S2.mergesort();
        S3.mergesort();
        S4.mergesort();


        /*
        double[] gen = new double[10000000];
        Random rand = new Random();
        while(i<gen.length){
            int rand1 = rand.nextInt(100000000);
            gen[i] = rand1;
            i++;
        }




        */



    }
}
