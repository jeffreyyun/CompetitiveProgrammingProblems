/******************************************************************************
 *  Compilation:      javac-algs4 Permutation.java
 *  Execution:        java-algs4 Permutation
 *  Author:           Haoyu Yun
 *  Date:             9/15/2017
 *
 *  Client program to test Randomized Queue
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class Permutation {
    public static void main(String[] args)
    {
    	int k = Integer.parseInt(args[0]);
    	RandomizedQueue<String> rq = new RandomizedQueue<String>();
    	while (!StdIn.isEmpty()) {
    		rq.enqueue(StdIn.readString());
    	}
    	while (k > 0) {	
    		StdOut.println(rq.dequeue());
    		k--;
    	}
    }
}