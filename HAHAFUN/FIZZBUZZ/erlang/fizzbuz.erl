-module(fizzbuzz).
-export([fizzbuzz/1]).

-define(MOD_THREE, "fizz").
-define(MOD_FIVE, "buzz").

% Helper function to map fizzbuzz across a sequence of numbers
fizzbuzz(To) ->
    lists:map(fun nt/1, lists:seq(1, To)).

% initiate the number transform for a Number
nt(Number) ->
    number_transform(Number, []).

% transform the number to either nothing or 'fizz' or 'buzz' or 'fizzbuzz'
%% NOTE: This style of fizzbuzz allows arbitrary matching
%% e.g. add bazz for number where Number rem 7 == 0
number_transform(0, Words) ->
    lists:flatten(lists:reverse(Words));
number_transform(Number, Words) when Number rem 3 == 0 ->
    case lists:member(?MOD_THREE, Words) of
        true -> number_transform(round(Number / 3), Words);
        false -> number_transform(round(Number / 3), [?MOD_THREE|Words])
    end;
number_transform(Number, Words) when Number rem 5 == 0 ->
    case lists:member(?MOD_FIVE, Words) of
        true -> number_transform(round(Number / 5), Words);
        false -> number_transform(round(Number / 5), [?MOD_FIVE|Words])
    end;
number_transform(Number, []) ->
    Number;
number_transform(Number, Words) ->
    Number,
    lists:flatten(lists:reverse(Words)).
