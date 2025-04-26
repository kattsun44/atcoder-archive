n, x = gets.chomp.split.map(&:to_i)

a = []

("A".."Z").each do |c|
  a << c * n
end

puts a.join[x - 1]
