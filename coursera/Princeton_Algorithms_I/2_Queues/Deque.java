/******************************************************************************
 *  Compilation:      javac-algs4 Deque.java
 *  Execution:        java-algs4 Deque
 *  Author:           Haoyu Yun
 *  Date:             9/15/2017
 *
 *  Data type for Deque
 *
 ******************************************************************************/

import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Deque<Item> implements Iterable<Item> {
  
    private Node first;
    private Node last;
    private int size;

    private class Node {
       private Item item;
       private Node prev;
       private Node next;

       public Node(Item item) {
           item = item;
           prev = null;
           next = null;
       }
    }

    public Deque() {
    //	  Node sentinel = new Node(null);		// only node with null item
    //    first = sentinel;
    //    last = sentinel;
    	first = null;
    	last = null;
        size = 0;
    } 
   
    public boolean isEmpty() {
    	return (size == 0);
    }
   
    // return the number of items on the deque
    public int size() {
        return size;
    }

    // add the item to the front
    public void addFirst(Item item) {
   		if (item == null) throw new IllegalArgumentException("can't add null item");
   		Node oldFirst = first;
   		first = new Node(item);
   		first.item = item;
   		first.next = oldFirst;
   		if (oldFirst != null) oldFirst.prev = first;
   		else last = first;		// size = 0
   		size++;
    } 
  
    // add the item to the end
    public void addLast(Item item) {
   	    if (item == null) throw new IllegalArgumentException("can't add null item");
   		Node oldLast = last;
   		last = new Node(item);
   		last.item = item;
   		last.prev = oldLast;
   		if (oldLast != null) oldLast.next = last;
   		else first = last;		// size = 0
   		size++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
    	if (isEmpty()) throw new NoSuchElementException("empty deque");
   		Node next = first.next;
      Item item = first.item;
      first = null;

      // case where all elements removed
      if (next == null) last = null;
      else next.prev = null;

      first = next;
   		size--;
   		return item;
    }

    // remove and return the item from the end
    public Item removeLast() {
    	if (isEmpty()) throw new NoSuchElementException("empty deque");
      Node prev = last.prev;
   		Item item = last.item;
      last = null;

      // case where all elements removed
      if (prev == null) first = null;
      else prev.next = null;

   		last = prev;
   		size--;
   		return item;
    }

    // return an iterator over items in order from front to end
    public Iterator<Item> iterator() {
    	return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
    	private Node curr = first;
    	public boolean hasNext()  	{ return curr != null; }
    	public void remove() 		{ throw new UnsupportedOperationException(); }
    
    	public Item next() {
    		if (!hasNext()) throw new NoSuchElementException();
    		Item item = curr.item;
    		curr = curr.next;
    		return item;
    	}
    }

    /* Unit testing */
    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<Integer>();
        StdOut.println("(Initial: " + deque.size() + " left in deque)");
        for (int i = 0; i < 10; i++) {
        	deque.addFirst(i);
        	deque.addLast(i+21);
        }
        StdOut.println("(Post-add1: " + deque.size() + " left in deque)");
        for (Integer item : deque)				// tests Iterator
        {
        	if (item == 5)
	        	for (Integer item2: deque)
	        		StdOut.println(item + " " + item2);
	        else
	        	StdOut.println(item);
        }
        StdOut.println("(Post-iter1: " + deque.size() + " left in deque)");
        while (!deque.isEmpty()) {
        	int first = deque.removeFirst();	// tests removeFirst
        	int last;
        	StdOut.println(first);
        	if (first % 5 == 0)
        	{
        		last = deque.removeLast();		// tests removeLast
        		StdOut.println(last);
        	}
        }
        deque.addFirst(88);
        deque.removeLast();
    	  deque.addFirst(-188);
        deque.removeLast();
        StdOut.println("(Post-rem1: " + deque.size() + " left in deque)");
    }
}