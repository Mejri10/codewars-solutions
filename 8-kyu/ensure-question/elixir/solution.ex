defmodule Parsers do
  def ensure_question(s) do
    cond do
      String.ends_with?(s, "?") -> s
      true -> s <> "?"
    end
  end
end