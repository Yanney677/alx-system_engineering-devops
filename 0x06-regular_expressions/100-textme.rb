#!/usr/bin/env ruby
# A script that output the following: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used in a textme message.
ARGF.read.scan(/Message from ([^,]+), to ([^,]+), Flags: ([^\n]+)/) { |m| puts "#{m[0]},#{m[1]},#{m[2]}" }
