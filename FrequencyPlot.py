import vincent

def make_bar(x, y, out_filename):
    data = {'data': y, 'x': x}
    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json(out_filename)