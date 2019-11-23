defmodule Evenator do
  def even?(n) when is_integer(n), do: Integer.mod(n, 2) == 0
  def even?(n) when is_float(n), do: false
end