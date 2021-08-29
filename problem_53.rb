RANGE = 101
COMPARISON = 1000000

# PROBLEM 53

def fact(n)
  return 1 if n == 0
  n * fact(n-1)
end


def choose(n,k)
  fact(n) / (fact(k)*fact(n-k))
end


def problem53
  x = 0
  RANGE.times {|n|
    (n+1).times {|k|
      x = x+1 if choose(n,k) > COMPARISON
    }
  }
  x
end

puts "Solution to Problem 53: #{problem53}"
