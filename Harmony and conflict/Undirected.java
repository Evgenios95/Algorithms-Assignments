import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.Graph;
import java.util.HashMap;
import java.util.HashSet;

public class Undirected {

    Queue<Integer> q = new Queue<Integer>();
    private int[] edgeTo; // need bfs

    private boolean isBipartite = true;
    HashMap<Integer, HashSet<Integer>> currented;

    private static boolean coloredV = true;
    private static boolean unColoredV = false;

    private boolean[] marked;
    private boolean[] color;

    public Undirected(Graph G, HashMap<Integer, HashSet<Integer>> currented) {
        isBipartite = true;
        color = new boolean[G.V()];
        marked = new boolean[G.V()];
        edgeTo = new int[G.V()];
        this.currented = currented;

        int v;
        for (v = 0; v < G.V() && isBipartite; v++) {
            if (!marked[v]) {
                bfs(G, v);
            }
        }
    }

    private Boolean isHarmonious(int v, int w) {

        if (this.currented.containsKey(v) && this.currented.get(v).contains(w)) {
            return (this.currented.containsKey(w) && this.currented.get(w).contains(v)) ? true : false;
        }
        return false;
    }

    // 540 + need to check if it's harmonious or not through the checker above.
    private void bfs(Graph G, int s) {
        color[s] = unColoredV;
        marked[s] = true;
        q.enqueue(s);

        while (!q.isEmpty()) {
            int v = q.dequeue();
            for (int w : G.adj(v)) {

                Boolean harmoniousG = isHarmonious(v, w);
                if (!marked[w]) {
                    marked[w] = true;
                    edgeTo[w] = v;

                    if (harmoniousG) {
                        color[w] = color[v];
                    } else {
                        color[w] = !color[v];
                    }

                    q.enqueue(w);
                } else if (harmoniousG == false && color[v] == color[w]) {
                    isBipartite = !isBipartite;
                    return;
                }
            }
        }
    }

    public boolean isBipartite() {
        return isBipartite;
    }
}