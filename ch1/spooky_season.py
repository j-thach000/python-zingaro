# TODO
# [x] input (integer)
# [] process input (an integer between [2,20])
# [x] output (string, the word spooky with S letter o's)

spook_level = int(input())
spook_o = 'o' * spook_level
spook_result = 'sp' + spook_o + 'ky'

print(spook_result)