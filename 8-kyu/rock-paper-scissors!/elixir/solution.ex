defmodule RockPaperScissors do
  @beats_table %{
    "scissors" => "paper",
    "paper" => "rock",
    "rock" => "scissors"
  }
  
  def rps(p1, p2) when p1 == p2, do: "Draw!"
  def rps(p1, p2), do: if @beats_table[p1] == p2, do: "Player 1 won!", else: "Player 2 won!"
end