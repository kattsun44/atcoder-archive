n = gets.to_i
a = gets.chomp.split.map(&:to_i)

success = false

(n-2).times do |i|
  success = true if a[i...i+3].uniq.size == 1
end

puts success ? "Yes" : "No"
