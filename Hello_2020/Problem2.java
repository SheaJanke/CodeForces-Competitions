package Hello_2020;

import java.util.ArrayList;
import java.util.Scanner;
public class Problem2 {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int ascentCount  =  0;
    ArrayList<int[]> startEnd = new ArrayList<int[]>();
    int count = 0;
    for(int a = 0; a < n; a ++){
      int size = s.nextInt();
      boolean ascent = false;
      int[] values = new int[size];
      for(int b = 0; b < size; b++){
        values[b] = s.nextInt();
      }
      for(int b = 0; b < size-1; b++){
        if(values[b] < values[b+1]){
          ascent = true;
          ascentCount++;
          break;
        }
      }
      if(ascent == false){
        int[] vals = new int[2];
        vals[0] = values[0];
        vals[1] = values[values.length-1];
        startEnd.add(vals);
      }
    }
    count += ascentCount*n;
    count += (n-ascentCount) * ascentCount;
    for(int[] a:startEnd){
      for(int[] b: startEnd){
        if(a[1] < b[0]){
          count++;
        }
      }
    }
    System.out.println(count);
    s.close();
  }
}