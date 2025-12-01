import colorgram

rgb_colors = []
colors = colorgram.extract('python2025\python\day18\image.jpg', 50)
for color in colors:
    rgb_colors.append(color.rgb)
for i in range(len(rgb_colors)):
    rgb_colors[i] = (rgb_colors[i].r, rgb_colors[i].g, rgb_colors[i].b)
print(rgb_colors)