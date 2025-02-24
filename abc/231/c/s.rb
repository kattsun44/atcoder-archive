n, q = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i).sort
x = q.times.map { gets.chomp.to_i }

x.each do |xx|
  i = a.bsearch_index { _1 >= xx }
  puts i.nil? ? 0 : n - i
end
