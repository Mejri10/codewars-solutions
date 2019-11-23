(ns rock-paper-scissors)

(defn rps [p1 p2]
  (def beats-table {"paper" "rock" "rock" "scissors" "scissors" "paper"})
  (if (= (get beats-table p1) p2)
      "Player 1 won!"
      (if (= (get beats-table p2) p1)
          "Player 2 won!"
          "Draw!"))
)