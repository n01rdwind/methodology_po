import numpy as np
import matplotlib.pyplot as plt

def objective(x):
    return x[0]**2 + x[1]**2 + 4*x[1] - 1

def gradient_objective(x):
    return np.array([2*x[0], 2*x[1] + 4])

def constraint1(x):
    return x[0]**2 + x[1]

def gradient_constraint1(x):
    return np.array([2*x[0], 1])

def constraint2(x):
    return x[0] - 2*x[1] - 8

def gradient_constraint2(x):
    return np.array([1, -2])

def barrier_function(x, r):
    c1 = constraint1(x)
    c2 = constraint2(x)
    if c1 > 0 or c2 > 0:  # Убеждаемся, что все ограничения строго соблюдаются
        return np.inf  # Возвращаем "бесконечный" штраф, если условие нарушено
    return objective(x) - r * (np.log(-c1) + np.log(-c2))

def gradient_barrier_function(x, r):
    c1 = constraint1(x)
    c2 = constraint2(x)
    if c1 > 0 or c2 > 0:
        return np.array([np.inf, np.inf])
    
    grad_f = gradient_objective(x)
    grad_c1 = gradient_constraint1(x)
    grad_c2 = gradient_constraint2(x)
    
    grad_barrier = grad_f - r * (grad_c1 / c1 + grad_c2 / c2)
    return grad_barrier

def penalty_function(x, r):
    c1 = constraint1(x)
    c2 = constraint2(x)
    if c1 > 0 or c2 > 0:
        return np.inf
    return -r * (np.log(-c1) + np.log(-c2))

def gradient_descent(x_k, r_k, alpha=0.01, max_iter=1000, tol=1e-6):
    for i in range(max_iter):
        grad = gradient_barrier_function(x_k, r_k)
        if np.any(np.isinf(grad)):
            break
        x_k1 = x_k - alpha * grad
        if np.linalg.norm(x_k1 - x_k) < tol:
            break
        x_k = x_k1
    return x_k

def barrier_method(initial_guess, r0=1.0, C=10, epsilon=0.01, alpha=0.01):
    x_k = initial_guess
    r_k = r0
    k = 0
    history = [x_k.copy()]

    while True:
        x_k1 = gradient_descent(x_k, r_k, alpha=alpha)

        p_k = penalty_function(x_k1, r_k)
        if np.abs(p_k) <= epsilon or np.isnan(p_k):
            break

        r_k /= C  # Уменьшение параметра штрафа
        x_k = x_k1
        history.append(x_k.copy())
        k += 1

    return x_k1, history, k

# Начальное приближение, которое должно строго удовлетворять ограничениям
initial_guess = np.array([0.5, -0.5])  # Эта точка должна удовлетворять g1(x) < 0 и g2(x) < 0

result, history, iterations = barrier_method(initial_guess)
print("Результат минимизации:", result)
print("Значение функции в минимуме:", objective(result))
print("Количество итераций:", iterations)

# Построение траектории оптимизации
history = np.array(history)
plt.plot(history[:, 0], history[:, 1], 'ro-')
plt.title("Trajectory of the optimization process")
plt.xlabel("x[0]")
plt.ylabel("x[1]")
plt.grid(True)
plt.show()
