defmodule EmailObfuscator do

  def execute(email) do
    email
    |> String.replace(~r/\./, " [dot] ", global: true)
    |> String.replace(~r/@/, " [at] ", global: true)
  end

end