import java.util.*;

class ExamRoom {
    private int n;
    private TreeSet<Integer> occupied;

    public ExamRoom(int n) {
        this.n = n;
        this.occupied = new TreeSet<>();
    }

    public int seat() {
        if (occupied.isEmpty()) {
            occupied.add(0);
            return 0;
        }

        int prev = -1;
        int maxDist = 0;
        int seat = 0;

        // Check seats between occupied seats
        for (int curr : occupied) {
            if (prev == -1) {
                // Check distance from 0 to the first occupied seat
                if (curr > maxDist) {
                    maxDist = curr;
                    seat = 0;
                }
            } else {
                // Check the middle of two occupied seats
                int dist = (curr - prev) / 2;
                if (dist > maxDist) {
                    maxDist = dist;
                    seat = prev + dist;
                }
            }
            prev = curr;
        }

        // Check the distance from the last occupied seat to the end
        if (n - 1 - occupied.last() > maxDist) {
            seat = n - 1;
        }

        occupied.add(seat);
        return seat;
    }

    public void leave(int p) {
        occupied.remove(p);
    }
}
/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */