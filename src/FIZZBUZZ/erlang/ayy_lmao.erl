fizzbuzz() ->
	F = fun(N) when N rem 15 == 0 -> "AyyLmaaoooo";
		(N) when N rem 3 == 0  -> "Ayy";
		(N) when N rem 5 == 0  -> "Lmao";
		(N) -> integer_to_list(N)
	end,
	[F(N)++"\n" || N <- lists:seq(1,100)]
