A = -0.02
B = 0.25
C = 2.0
h = 0.01

def f1(y1, y2, y3):
    return y1 * (y1 - B) * (1 - y1) - y1 * y3 - A * (y1 - y2)


def f2(y1, y2, y3):
    return y2 * (y2 - B) * (1 - y2) - y2 * y3 - A * (y2 - y1)


def f3(y1, y2, y3):
    return y3 * (y1 + y2 - C)


def k1(func, x, y, z):
    return func(x, y, z)


def k2(func, x, y, z, k):
    return func(x + h / 2, y + k * h / 2, z + k * h / 2)


def k3(func, x, y, z, k2):
    return func(x + h / 2, y + k2 * h / 2, z + k2 * h / 2)


def k4(func, x, y, z, k3):
    return func(x + h, y + h * k3, z + h * k3)


def next_step_value(y_prev, k1, k2, k3, k4):
    return y_prev + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


y1 = C / 2
y2 = C / 2
y3 = (1 + B) * (y1 ** 2 + y2 ** 2) / C - B - (y1 ** 2 - y1 * y2 + y2 ** 2)
t = 0
with open('f1.csv', 'w') as p1:
    with open('f2.csv', 'w') as p2:
        with open('f3.csv', 'w') as p3:
            with open('f12.csv', 'w') as p12:
                with open('f13.csv', 'w') as p13:
                    with open('f23.csv', 'w') as p23:
                        while (t <= 100.0):
                            curr_k1 = k1(f1, y1, y2, y3)
                            curr_k2 = k2(f1, y1, y2, y3, curr_k1)
                            curr_k3 = k3(f1, y1, y2, y3, curr_k2)
                            curr_k4 = k4(f1, y1, y2, y3, curr_k3)

                            y1_coeffs = [curr_k1, curr_k2, curr_k3, curr_k4]

                            curr_k1 = k1(f2, y1, y2, y3)
                            curr_k2 = k2(f2, y1, y2, y3, curr_k1)
                            curr_k3 = k3(f2, y1, y2, y3, curr_k2)
                            curr_k4 = k4(f2, y1, y2, y3, curr_k3)

                            y2_coeffs = [curr_k1, curr_k2, curr_k3, curr_k4]

                            curr_k1 = k1(f3, y1, y2, y3)
                            curr_k2 = k2(f3, y1, y2, y3, curr_k1)
                            curr_k3 = k3(f3, y1, y2, y3, curr_k2)
                            curr_k4 = k4(f3, y1, y2, y3, curr_k3)

                            y3_coeffs = [curr_k1, curr_k2, curr_k3, curr_k4]

                            y1 = next_step_value(y1, y1_coeffs[0], y1_coeffs[1], y1_coeffs[2], y1_coeffs[3])

                            y2 = next_step_value(y2, y2_coeffs[0], y2_coeffs[1], y2_coeffs[2], y2_coeffs[3])

                            y3 = next_step_value(y3, y3_coeffs[0], y3_coeffs[1], y3_coeffs[2], y3_coeffs[3])

                            p1.write(f"{t},{y1} \n")
                            p2.write(f"{t},{y2} \n")
                            p3.write(f"{t},{y3} \n")

                            p12.write(f"{y1},{y2} \n")
                            p13.write(f"{y1},{y3} \n")
                            p23.write(f"{y2},{y3} \n")
                            t += h