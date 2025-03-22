s = gets.chomp

def palindrome?(word)
  word = word.to_s
  size = word.length / 2
  return word[0..size] == word.reverse[0..size]
end

if palindrome?(s)
  puts s
  exit
end

last = s[-1]
count = 0

r = s.reverse
s.size.downto(0) do |i|
  if palindrome?(s + r[i..])
    puts s + r[i..]
    exit
  end
end
