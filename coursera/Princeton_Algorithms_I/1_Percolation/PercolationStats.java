/******************************************************************************
 *  Compilation:      javac PercolationStats.java
 *  Execution:        java PercolationStats
 *  Author:            Haoyu Yun
 *    Date:            9/14/2017
 *
 *  Runs Monte Carlo simulation on Percolation
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
// import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
// import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {
    private int trials;
    private double mean;
    private double stddev;

    public PercolationStats(int n, int trials) {    // perform trials independent experiments on an n-by-n grid
        if (n <= 0 || trials <= 0)
            throw new java.lang.IllegalArgumentException();
        this.trials = trials;
        double[] filled = new double[trials];
        int r, c;
        for (int i = 0; i < trials; i++) {
            Percolation p = new Percolation(n);
            while (!p.percolates()) {
                r = StdRandom.uniform(1, n+1);
                c = StdRandom.uniform(1, n+1);
                p.open(r, c);
            }
            filled[i] = 1.0*p.numberOfOpenSites()/(n*n);
        }
        mean = StdStats.mean(filled);
        if (trials == 1)
            stddev = Double.NaN;
        else 
            stddev = StdStats.stddev(filled);
    }

    public double mean()  {                        // sample mean of percolation threshold
        return mean;
    }

    public double stddev() {                       // sample standard deviation of percolation threshold
        return stddev;
    }

    public double confidenceLo() {                  // low  endpoint of 95% confidence interval
        return mean - 1.96*stddev/Math.sqrt(this.trials);
    }

    public double confidenceHi()  {                // high endpoint of 95% confidence interval
        return mean + 1.96*stddev/Math.sqrt(this.trials);
    }

    public static void main(String[] args) {        // test client (described below)
      // Stopwatch s = new Stopwatch();

        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[1]);
        PercolationStats ps = new PercolationStats(n, t);
        StdOut.println("mean = " + ps.mean());
        StdOut.println("stddev = " + ps.stddev());
        StdOut.println("95% confidence interval = [" + ps.confidenceLo() + ", " + ps.confidenceHi() + "]");

      // StdOut.println("Time Elapsed: " + s.elapsedTime());
    }
}