#!/usr/bin/env python
import hashlib

print("Enter input")
# inp = raw_input()
# m = hashlib.sha256()
ans = "jenkins"
print(hashlib.sha256(ans).hexdigest())


