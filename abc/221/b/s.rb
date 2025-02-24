s = gets.chomp
t = gets.chomp

if s == t
  puts "Yes"
  return
end

(s.length - 1).times do |i|
  if s[0...i] + s[i+1] + s[i] + s[i+2...s.length] == t
    puts "Yes"
    return
  end
end

puts "No"
