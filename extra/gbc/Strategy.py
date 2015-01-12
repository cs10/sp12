
class Strategy(object):
   def __init__(self):
      self.reset()

   def reset(self):
      self.ordering = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
      self.mapping = {
         'a' : [chr(i) for i in xrange(97, 123)],
         'b' : [chr(i) for i in xrange(97, 123)],
         'c' : [chr(i) for i in xrange(97, 123)],
         'd' : [chr(i) for i in xrange(97, 123)],
         'e' : [chr(i) for i in xrange(97, 123)],
         'f' : [chr(i) for i in xrange(97, 123)],
         'g' : [chr(i) for i in xrange(97, 123)],
         'h' : [chr(i) for i in xrange(97, 123)],
         'i' : [chr(i) for i in xrange(97, 123)],
         'j' : [chr(i) for i in xrange(97, 123)],
         'k' : [chr(i) for i in xrange(97, 123)],
         'l' : [chr(i) for i in xrange(97, 123)],
         'm' : [chr(i) for i in xrange(97, 123)],
         'n' : [chr(i) for i in xrange(97, 123)],
         'o' : [chr(i) for i in xrange(97, 123)],
         'p' : [chr(i) for i in xrange(97, 123)],
         'q' : [chr(i) for i in xrange(97, 123)],
         'r' : [chr(i) for i in xrange(97, 123)],
         's' : [chr(i) for i in xrange(97, 123)],
         't' : [chr(i) for i in xrange(97, 123)],
         'u' : [chr(i) for i in xrange(97, 123)],
         'v' : [chr(i) for i in xrange(97, 123)],
         'w' : [chr(i) for i in xrange(97, 123)],
         'x' : [chr(i) for i in xrange(97, 123)],
         'y' : [chr(i) for i in xrange(97, 123)],
         'z' : [chr(i) for i in xrange(97, 123)],
         ' ' : [' '],
      }

   ## You don't need to use this.  It's for the internal machinery.
   def get_mapping(self):
      return self.mapping

   ## You don't need to use this.  It's for the internal machinery.
   def get_ordering(self):
      return self.ordering

   ###
   ## Use this to say "the letter ENCODED must be the letter DECODED."
   ###
   def pair(self, encoded, decoded):
      self.mapping[encoded] = [decoded]

   ###
   ## Use this to say "the letter ENCODED cannot be the letter DECODED."
   ###
   def eliminate(self, encoded, decoded):
      self.mapping[encoded].remove(decoded)

   ###
   ## Use this to say "don't even try to decode the letter ENCODED."
   ###
   def dont_decode(self, encoded):
      self.ordering.remove(encoded)
      del self.mapping[encoded]

   def decoding(self, encoded):
      return encoded in self.ordering

   ###
   ## Use this to say "check out the letter ENCODED." 
   ###
   def reorder(self, encoded, position):
      self.ordering.remove(encoded)
      self.ordering.insert(position, encoded)

   ###
   ##  This is where you make your mark!  Build a strategy using the functions above,
   ##     or edit the self.ordering and self.mapping structures yourself.
   ###
   def build_strategy_for(self, phrase):
      pass
