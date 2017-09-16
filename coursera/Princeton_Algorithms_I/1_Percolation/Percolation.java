/******************************************************************************
 *  Compilation:      javac PercolationStats.java
 *  Execution:        java PercolationStats
 *  Author:            Haoyu Yun
 *    Date:            9/12/2017
 *
 *  Data type to test Percolation
 *
 ******************************************************************************/

import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Percolation {

    private WeightedQuickUnionUF wQU;
    private byte[][] status;
    // 0 blocked, 1 open, 3(011) connect bottom
    private int sitesOpen;
    private int n;

    public Percolation(int n) {                // create n-by-n grid, with all sites blocked
        if (n < 1)  throw new java.lang.IllegalArgumentException("n must be >= 1");

        n++;
        this.n = n;
        wQU = new WeightedQuickUnionUF(n*n);
        status = new byte[n][n];
        sitesOpen = 0;
    }

    public void open(int row, int col) {    // open site (row, col) if it is not open already
        checkValidIndex(row, col);

        if (status[row][col] != 0)
            return;
        status[row][col] = 1;
        sitesOpen += 1;

        // special actions for cells in top and bottom row
        int mInd = xyTo1D(row, col);
        if (row == 1) wQU.union(0, mInd);         // union connects to top
        if (row == n-1) status[row][col] |= 2;    // status reflects connecting to bottom
        if (n == 2)  status[0][0] |= 2;           // edge case, 1x1 grid

        // connects roots of neighbors
        if (row > 1 && isOpen(row-1, col))
            connectRoots(row, col, row-1, col);
        if (row < n-1 && isOpen(row+1, col))
            connectRoots(row, col, row+1, col);
        if (col > 1 && isOpen(row, col-1))   
            connectRoots(row, col, row, col-1);
        if (col < n-1 && isOpen(row, col+1))    
            connectRoots(row, col, row, col+1);
    }

    private void connectRoots(int r1, int c1, int r2, int c2) {
        int rt_1 = wQU.find(xyTo1D(r1, c1));
        int rt_2 = wQU.find(xyTo1D(r2, c2));
        wQU.union(xyTo1D(r1, c1), xyTo1D(r2, c2));
        // updates whether mutual root is connected to bottom
        if (((status[rt_1 / n][rt_1 % n] & 2) | (status[rt_2 / n][rt_2 % n] & 2)) != 0) {
            int rt_new = wQU.find(xyTo1D(r1, c1));
            status[rt_new / n][rt_new % n] |= 2;
        }
    }

    public boolean isOpen(int row, int col) {  // is site (row, col) open?
        checkValidIndex(row, col);
        return (status[row][col] & 1) != 0;
    }

    public boolean isFull(int row, int col) {  // is site (row, col) full?
        checkValidIndex(row, col);
        // StdOut.println(row + " " + col);
        return (status[row][col] & 1) != 0 && (wQU.connected(xyTo1D(row, col), 0));
    }

    public int numberOfOpenSites() {          // number of open sites
        return sitesOpen;
    }

    public boolean percolates()   {           // does the system percolate?
        int top_ind = wQU.find(0);
        return (status[top_ind / n][top_ind % n] & 2) != 0;
    }

    private int xyTo1D(int row, int col) {
        return row*n + col;
    }

    private void checkValidIndex(int row, int col) {
        if (row <= 0 || row >= n || col <= 0 || col >= n)
            throw new java.lang.IllegalArgumentException("row " + row + " and col " + col + " are not within nxn");
    }

    public static void main(String[] args)  { // test client (optional)
        int n = StdIn.readInt();
        Percolation p = new Percolation(n);
        p.open(1, 1);
        p.open(1, 2);
        StdOut.println(p.numberOfOpenSites() == 2);
        // StdOut.println(wQU.connected(1, 2));
    }
}
