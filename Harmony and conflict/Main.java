import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.Graph;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, HashSet<Integer>> currented = new HashMap<Integer, HashSet<Integer>>();
        int ve = StdIn.readInt();
        int ed = StdIn.readInt();

        Graph G = new Graph(ve);
        for (int i = 0; i < ed; i++) {
            int u = StdIn.readInt();
            int v = StdIn.readInt();
            int n = StdIn.readInt();

            if (n == 0) {
                HashSet<Integer> hashs = new HashSet<Integer>();
                hashs.add(u);
                hashs.add(v);

                if (currented.containsKey(u)) {
                    currented.get(u).add(v);
                } else {
                    currented.put(u, hashs);
                }

                if (currented.containsKey(v)) {
                    currented.get(v).add(u);
                } else {
                    currented.put(v, hashs);
                }
            }
            G.addEdge(u, v);
        }

        Undirected g = new Undirected(G, currented);

        if (g.isBipartite()) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
