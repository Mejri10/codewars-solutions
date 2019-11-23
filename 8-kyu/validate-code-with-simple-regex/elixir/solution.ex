defmodule CodeValidator do
  def valid?(code) do
    code
    |> Integer.to_string
    |> String.starts_with?(~w(1 2 3))
  end
end