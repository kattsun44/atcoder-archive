N, Q = gets.chomp.split.map(&:to_i)
L = N.times.map { gets.chomp.split.map(&:to_i) }

Q.times do
  s, t = gets.chomp.split.map(&:to_i)
  puts L[s - 1][t]
end
