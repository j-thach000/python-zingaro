# TODO
# [x] handle input (single integer N)
# [x] process input
# [x] return output (string, "A long time ago in a galaxy far away..." with far up to N times)

n_far = int(input())
far = 'far, ' * (n_far - 1)
credit_crawl = 'A long time ago in a galaxy ' + far + 'far away...'
print(credit_crawl)