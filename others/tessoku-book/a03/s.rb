n, k = gets.chomp.split.map(&:to_i)
p = gets.chomp.split.map(&:to_i)
q = gets.chomp.split.map(&:to_i)

sum_is_k = false

p.each do |pp|
  q.each do |qq|
    sum_is_k = true if pp + qq == k
  end
end

puts sum_is_k ? "Yes" : "No"
