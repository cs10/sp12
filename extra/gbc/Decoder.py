import time
###   Pure recursive solution.  I believe it works but its a memory hog for
###     larger trees.  Full alphabet isn't flying.
##  def find_combo(ordering, mapping, current_mapping):
##     if len(ordering) > 0:
##        character = ordering.pop(0)
##        results = []
##
##        for decoded in mapping[character]:
##           current_mapping[character] = decoded
##           results.extend(find_combo(list(ordering), mapping, current_mapping))
##
##        return results
##     else:
##        return [dict(current_mapping)]

## Generator
def find_combo2(ordering, mapping, current_mapping):
   if len(ordering) > 0:
      character = ordering.pop(0)
      results = []

      for decoded in mapping[character]:
         current_mapping[character] = decoded
         for combo in find_combo2(list(ordering), mapping, current_mapping):
            yield combo
   else:
      yield current_mapping

class Decoder(object):
   def __init__(self):
      print "Loading word list."
      wordfile = open('WORDS.TXT')
      raw_words = wordfile.readlines()
      wordfile.close()

      ## Build a dictionary that has words as keys (value is not important).
      self.word_dict = {}
      for word in raw_words:
         self.word_dict[word.strip()] = True
      print "Done."

   def generate_combos(self):
      bkwds_order = list(self.ordering)
      bkwds_order.reverse()
      return find_combo2(bkwds_order, self.mapping, {})

   def count_words_in(self, phrase):
      real_words = 0

      for word in phrase.split(' '):
         if self.word_dict.has_key(word):
            real_words += 1

      return real_words

   def apply_mapping(self, mapping, phrase):
      return ''.join([mapping[item] for item in phrase])

   def solve(self, phrase, strategy):
      solutions = []
      # Go ahead and build the strategy for the input phrase.
      strategy.reset()
      strategy.build_strategy_for(phrase)

      self.mapping = strategy.get_mapping()
      self.ordering = strategy.get_ordering()

      combo_generator = self.generate_combos()
      start_time = time.time()
      num_tried = 0
      for combo in combo_generator:
         decoded_phrase = self.apply_mapping(combo, phrase)
         num_words = self.count_words_in(decoded_phrase)
         ## Announce the phrase if it contains only real words and has not been announced yet.
         if len(decoded_phrase.split(' ')) is num_words and decoded_phrase not in [solution[0] in solutions]:
            print "100%% match for phrase '%s'" % decoded_phrase
            solutions.append( (decoded_phrase, combo) )

         num_tried += 1
         if num_tried % 100000 is 0:
            print 'Attempted %d different combinations [%.2f combinations per second]' % (num_tried, num_tried / (time.time() - start_time))

      return solutions
