/******************************************************************************
 *  Compilation:      javac-algs4 RandomizedQueue.java
 *  Execution:        java-algs4 RandomizedQueue
 *  Author:           Haoyu Yun
 *  Date:             9/15/2017
 *
 *  Data type for Randomized Queue
 *
 ******************************************************************************/

import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] queue;
    private int size;
    private int cap;

    public RandomizedQueue()                 // construct an empty randomized queue
    {
    	cap = 2;
    	queue = (Item[]) new Object[cap];
    	size = 0;
    }

    public boolean isEmpty()                 // is the queue empty?
    {
    	return (size == 0);
    }

    public int size()                        // return the number of items on the queue
    {
   		return size;
    }

    public void enqueue(Item item)           // add the item
    {
    	if (item == null) throw new IllegalArgumentException("can't add null item");
    	if (size == cap) resize(cap*2);
    	queue[size] = item;
    	size++;
    }

    private void resize(int capacity)
    {
    	cap = capacity;
    	Item[] temp = (Item[]) new Object[capacity];
    	System.arraycopy(queue, 0, temp, 0, size);
    	queue = temp;
    }

    public Item dequeue()                    // remove and return a random item
    {
    	if (isEmpty()) throw new NoSuchElementException();
        int rand = StdRandom.uniform(size);
    	Item item = queue[rand];

        int toShift = size-rand-1;
        if (toShift > 0)
            System.arraycopy(queue, rand+1, queue, rand, toShift);

    	queue[size-1] = null;				// to GC
    	size--;

    	if (size > 0 && size == cap/4) resize(cap/2);

    	return item;
    }

    public Item sample()                     // return (but do not remove) a random item
    {
        if (isEmpty()) throw new NoSuchElementException();
    	int rand = StdRandom.uniform(size);
    	return queue[rand];
    }

    public Iterator<Item> iterator()         // return an independent iterator over items in random order
    {
    	return new RQIterator();
    }

    private class RQIterator implements Iterator<Item> {
    	private int i;
        private int[] inds = new int[size];

    	public RQIterator() {
            for (int j = 0; j < size; j++)
                inds[j] = j;
            StdRandom.shuffle(inds);
        }

    	public boolean hasNext() 	{ return i < size; }
    	public void remove()		{ throw new UnsupportedOperationException(); }
    
    	public Item next() {
    		if (!hasNext()) throw new NoSuchElementException();
    		return queue[inds[i++]];
    	}

    }

    // unit testing
    public static void main(String[] args)
    {
    	RandomizedQueue<Integer> q = new RandomizedQueue<Integer>();
    	StdOut.println("(Initial: " + q.size() + " left in queue)");
    	for (int i = 0; i < 20; i++) {
    		q.enqueue(i);
    		StdOut.println("Added " + i);
    		if (!q.isEmpty()) StdOut.println(q.sample());
    	}
    	StdOut.println("(Post-add1: " + q.size() + " left in queue)");
        for (Integer item : q) {				// tests Iterator
        	if (item == 10) {
	        	for (Integer item2: q)
	        		StdOut.println(item + " " + item2);
                for (Integer item2: q)
                    StdOut.println(item + " " + item2);
            }
	        else
	        	StdOut.println(item);
        }
        StdOut.println("(Post-iter1: " + q.size() + " left in queue)");
    	while (!q.isEmpty()) {
    		StdOut.println(q.dequeue());
    		if (!q.isEmpty()) StdOut.println(q.sample());
    	}
    	q.enqueue(88);
    	q.enqueue(-188);
    	StdOut.println(q.sample());
    	StdOut.println("(Post-rem1: " + q.size() + " left in queue)");
    }
}