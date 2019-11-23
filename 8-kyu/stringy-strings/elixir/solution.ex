defmodule OneZeroSequencer do
  def stringy(size) do
    [1, 0]
    |> Stream.cycle()
    |> Enum.take(size)
    |> Enum.join()
  end
end