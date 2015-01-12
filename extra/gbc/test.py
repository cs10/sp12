import time
import Decoder
import Strategy

d = Decoder.Decoder()
s = Strategy.Strategy()

secret = 'a lhiwqgqw lmz kmq xutqxunn lut pqkkaip xappqg kmqi ak mak jq'
answers = d.solve(secret, s)

start_time = time.time()
print "%d different solutions found in %.f seconds." % (len(answers), time.time() - start_time)
