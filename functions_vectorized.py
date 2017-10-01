def prod_non_zero_diag(X):
  x = np.array(np.diag(X))
  x[x==0] = 1
  return x.prod()


are_multisets_equal(x, y):
  return all(sort(x), sort(y))


max_after_zero(x):
  return x[np.arange(len(x)-1)[x[:-1]==0] + 1].max()


convert_image(z, coefs):
  return z[0] * coefs[0] + z[1] * coefs[1] + z[2] * coefs[2]


def run_length_encoding(x):
  z = np.append(np.array([1]),np.diff(x))
  a = np.where(z != 0, True, False)
  y1 = np.append(np.arange(len(y))[a], len(y))[1:]
  y2 = np.arange(len(y))[a]
  return x[a], y1 - y2


def pairwise_distance(x,y):
  xs, ys = np.meshgrid(x,y)
  return np.sqrt((xs - ys) ** 2)
  
