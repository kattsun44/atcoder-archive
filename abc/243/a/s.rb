A = gets.chomp.split.map(&:to_i)

v = A[0]
abc = A[1..]
i = 0

while v >= 0
  v -= abc[i % 3]
  i += 1
end

if i % 3 == 0
  puts "T"
elsif i % 3 == 1
  puts "F"
else
  puts "M"
end
