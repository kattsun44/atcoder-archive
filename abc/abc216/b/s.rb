n = gets.chomp.to_i
h = {}

n.times do
  s = gets.chomp
  if h[s]
    puts "Yes"
    return
  end
  h[s] = true
end

puts "No"
