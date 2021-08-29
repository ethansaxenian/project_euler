divisor_sum(N, R) :-
  divisor_sum(N, 1, 0, R).

divisor_sum(N, N, R, R).
divisor_sum(N, X, R, T) :-
  X < N,
  0 is N mod X,
  X1 is X+1,
  R1 is R+X,
  divisor_sum(N, X1, R1, T).
divisor_sum(N, X, R, T) :-
  X < N,
  0 =\= N mod X,
  X1 is X+1,
  divisor_sum(N, X1, R, T).

amicable(A, B) :-
  A =\= B,
  divisor_sum(A, SA),
  divisor_sum(B, SB),
  SA =:= B,
  SB =:= A.

problem21(A,B) :-
  between(1, 10000, A),
  between(1, 10000, B),
  amicable(A,B).
