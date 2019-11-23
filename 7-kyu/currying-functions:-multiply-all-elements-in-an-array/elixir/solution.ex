defmodule Multiply_all do
  def solution(lst), do: fn n -> Enum.map(lst, fn x -> x * n end) end
end