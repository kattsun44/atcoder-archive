s = gets.chomp

count = 0
ans = 0
s.split("").each do |c|
  if count % 2 == 1 && c == "i"
    ans += 1
    count += 1
  elsif count % 2 == 0 && c == "o"
    ans += 1
    count += 1
  end
  count += 1
end

ans += 1 if s[-1] == "i"

puts ans
