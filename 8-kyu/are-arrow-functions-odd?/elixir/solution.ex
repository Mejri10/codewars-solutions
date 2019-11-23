defmodule OnlyOdd do
  def odds(nums) do
    Enum.filter(nums, fn x -> Integer.mod(x, 2) == 1 end)
  end
end