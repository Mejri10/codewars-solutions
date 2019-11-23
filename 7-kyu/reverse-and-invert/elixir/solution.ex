defmodule ReverseInverter do
  def reverse_invert(lst) do
    lst
    |> Enum.filter(&is_integer/1)
    |> Enum.map(&reverse_inverse_integer/1)
  end
  
  def reverse_inverse_integer(x) do
    x
    |> abs
    |> Integer.digits()
    |> Enum.reverse()
    |> Integer.undigits()
    |> (fn n -> if x > 0, do: -n, else: n end).()
  end
end