#
# AyyLmao
# @theDevilsVoice
#
defmodule Ayy do
  @moduledoc """
  Ayylmao and what not.
  """

  if File.exists?("Elixir.Ayy.beam") do
    IO.puts("Wipe the old beam")
    File.rm! "Elixir.Ayy.beam"
  end

  IO.puts("Ayyyyy.")

  whichayy = fn
    (0, 0, _) -> "AyyLmao"
    (0, _, _) -> "Ayy"
    (_, 0, _) -> "Lmao"
    (_, _, n) -> n
  end

  ayylmao = fn (n) ->
    whichayy.(rem(n, 3), rem(n, 5), n)
  end

  IO.inspect Enum.map(1..100, ayylmao)

end
