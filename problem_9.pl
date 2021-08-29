triple(A, B, C) :-
  X is A^2 + B^2,
  C =:= sqrt(X).

problem9(X) :-
	between(1,1000,A),
	between(1,1000,B),
  C is 1000-A-B,
  triple(A, B, C),
  X is A * B * C, !.
