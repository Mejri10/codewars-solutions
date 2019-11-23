defmodule Count do
  def count_by(x, n) do
    Enum.take_every((x..x*n), x)
  end
end