n, m = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
b = gets.chomp.split(" ").map(&:to_i)

success = true

b.each do |bb|
  if !a.include?(bb)
    success = false
  else
    a.delete(bb)
  end
end

puts success ? "Yes" : "No"
