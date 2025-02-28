n, m = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
b = gets.chomp.split(" ").map(&:to_i)

success = true

b.each do |bb|
  if a.include?(bb)
    a.delete_at(a.index(bb))
  else
    success = false
  end
end

puts success ? "Yes" : "No"
