Code Assessment - MediaMath - Python

Challenge 1.
A “Straight Flush” is a poker hand containing five cards of sequential rank, all of the same suit, such as [Tile, 5, 4, 3, 2, 1[, or [Heart, A, K, Q, J, 10 (aka royal flush)].
Given a set of poker cards, 
	•	Write a small program to detect if a straight flush (include royal flush) exists in the set of cards given; 

#hands to be tested
straight_flush_hand = ["2H", "AH", "3H", "4H", "5H"]
straight_flush_hand2 = ["KH", "JH", "AH", "0H", "QH"]
one_pair_hand = ["AS", "AH", "KD", "JD", "7C"]

def check_for_straight_flush(hand):
  #list to check against for straight
  number = ['234567890JQKA'.index(num) for num, suit in hand]
  sorted_number = number.sort()
  
  #getting unique elements in list
  suits = [suit for num, suit in hand]
  
  straight = False
  flush = False 
  #straight condition
  if (max(number) - min(number) == 4 and len(number) == 5 or max(number) - min(number) == 12 and len(number) == 5):
    straight = True
  #flush condition
  if len(set(suits)) == 1:
    flush = True
  #checking for both straight and flush
  if straight and flush:
    return "You have a straight flush!"
  else:
    return "Sorry, no straight flush..."


	•	Write a unit test program to verify your implementation. 

def straight_flush_test():
	assert check_for_straight_flush(one_pair_hand) == "Sorry, no straight flush..."
	assert check_for_straight_flush(straight_flush_hand) == "You have a straight flush!"
	assert check_for_straight_flush(straight_flush_hand2) == "You have a straight flush!"
	return "works as intended"

print straight_flush_test()


Challenge 2.
Run-length encoding (RLE) is a very simple form of lossless data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. For example, string "abbccccddd" can be represented as "1a2b4c3d" in RLE. A Compact-Run-length-Encoding is a variation to the RLE that it encodes run lengths only for runs of two or more characters only. In the above example, "abbccccddd" is encoded as "a2b4c3d" in the compact form.

	•	Write a simple function to expand a Compact-RLE string;

def reverse_compact_rle(string):
  count = 0
  
  #list of letters to join at the end
  letters_only = []
  
  #loop to iterate through string
  while count != len(string):
    if string[count].isdigit():
    	
    	#if number, have function append letter "number" amount of times
      [letters_only.append(string[count + 1]) for _ in range(int(string[count]))]
    
    #if letter is not preceded by number, append letter
    elif string[count].isalpha() and not string[count-1].isdigit():
      letters_only.append(string[count])
    
    #increase count to prevent exceeding call stack
    count+= 1
  
  return "".join(letters_only)
  

	•	Write a unit test program to verify your implementation.

def reverse_compact_rle_test():
  assert reverse_compact_rle('1a2b3c4de') == "abbcccdddde"
  assert reverse_compact_rle('5eas2d') == "eeeeeasdd"
  assert reverse_compact_rle('e2adsf') == "eaadsf"
  return 'pass test'
  
print reverse_compact_rle('1a2b3c4de')
print reverse_compact_rle('5eas2d')
print reverse_compact_rle('e2adsf')

print reverse_compact_rle_test()