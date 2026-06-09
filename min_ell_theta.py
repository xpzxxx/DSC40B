def learn_theta(data, colors):
    theta = None
    for x, c in zip(data, colors):
        if c == 'blue' and (theta is None or x > theta):
            theta = x
    return theta


def compute_ell(data, colors, theta):
    loss = 0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            loss += 1
        elif c == 'blue' and x > theta:
            loss += 1
    return float(loss)


def minimize_ell(data, colors):
    best_theta = None
    best_loss = None
    for theta in data:                          # O(n) candidates ...
        loss = compute_ell(data, colors, theta)  # ... each O(n) -> O(n^2)
        if best_loss is None or loss < best_loss:
            best_loss = loss
            best_theta = theta
    return float(best_theta)


def minimize_ell_sorted(data, colors):
    total_blue = colors.count('blue')

    red_leq_theta = 0          # # red points <= theta
    blue_gt_theta = total_blue  # # blue points > theta (theta below data[0])
    best_loss = None
    best_theta = None

    for alpha in range(1, len(data) + 1):
        x = data[alpha - 1]
        # Move data[alpha - 1] onto the "<= theta" side (theta = data[alpha-1]).
        if colors[alpha - 1] == 'red':
            red_leq_theta += 1
        else:                       # blue point now <= theta
            blue_gt_theta -= 1
        # Invariant restored: blue_gt_theta == # blue points > data[alpha-1].
        loss = red_leq_theta + blue_gt_theta
        if best_loss is None or loss < best_loss:
            best_loss = loss
            best_theta = x

    return float(best_theta)