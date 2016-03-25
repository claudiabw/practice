void ReversePrint(Node head) {

    if (head == null) {
        return;
    } else {
        Node current = head;
        ArrayList<Node> nodes = new ArrayList<Node>();
        while (current != null) {
            nodes.add(current);
            // Node prev = current;
            current = current.next;
        }
        for (int i = nodes.size() - 1; i >= 0; i--) {
            Node result = nodes.get(i);
            System.out.println(result.data);
        }
    }

}