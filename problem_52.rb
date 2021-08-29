# PROBLEM 52 (runs in about 9s)

def problem52
  x = 1
  while true
    multiples = Array.new(6) {|i| (x*(i+1)).to_s.split('').sort!}
    return x if multiples.uniq.size == 1
    x = x+1
  end
end

puts "Solution to Problem 52: #{problem52}"
