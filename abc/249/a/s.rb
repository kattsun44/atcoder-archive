A, B, C, D, E, F, X = gets.chomp.split.map(&:to_i)

t = 0
a = 0

X.times do |x|
  t += B if x % (A + C) < A
  a += E if x % (D + F) < D
end

if t > a
  puts "Takahashi"
elsif a > t
  puts "Aoki"
else
  puts "Draw"
end
