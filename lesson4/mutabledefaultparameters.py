
# def sum_series(nth=1, sequence=(0,1)):
#     """
#     Generate a list of sums given a seed and return the Nth number.
#     """
#     sequence = list(sequence)
#     for i in range(2, nth):
#         sequence.append(sequence[i-2] + sequence[i-1])
#     return sequence[nth-1]
#
# print(sum_series(5))

# names = {1: "fred", 2: "Sally", 3: "Bob"}
# print(names.items())
# for i, (key,value) in enumerate(names):
#     print(i, key, value)
# #
# #     last_name = "Barrie"

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
  # k is now the key
  # v is the value
  print(k, v)