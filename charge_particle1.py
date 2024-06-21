import numpy as np
import matplotlib.pyplot as plt

def calculate_electric_field(q, xq, yq, x, y):
    """
    Calculates the electric field components due to point charges.
    
    Parameters:
    - q: Array of charges.
    - xq, yq: Arrays of x and y coordinates of charges.
    - x, y: 2D grids of x and y coordinates for field calculation.
    
    Returns:
    - EX, EY: Electric field components.
    - E: Magnitude of the electric field.
    """
    k = 8.9875e9  # Coulomb's constant
    eps = 1e-10  # Small epsilon value to prevent division by zero

    # Initialize electric field components
    EX = np.zeros_like(x)
    EY = np.zeros_like(y)

    # Calculate electric field due to point charges
    for i in range(len(q)):
        rx = x - xq[i]
        ry = y - yq[i]
        r = np.sqrt(rx**2 + ry**2)
        r3 = (r**3 + eps)  # add eps to prevent division by very small r
        EX += k * q[i] * rx / r3
        EY += k * q[i] * ry / r3

    E = np.sqrt(EX**2 + EY**2)  # Magnitude of electric field
    return EX, EY, E

def main():
    """
    Main function to study the behavior of particles in an electric field.
    """
    # Initial charges and positions for particles 1 and 2
    q = np.array([1, -1])  # Charges
    xq = np.array([1, -1])  # x-coordinates of charges
    yq = np.array([0, 0])  # y-coordinates of charges

    # Interactive input for the third particle
    xq_third = float(input("Enter x-coordinate of the third particle (0 to 2): "))
    yq_third = float(input("Enter y-coordinate of the third particle (0 to 2): "))
    q_third = float(input("Enter charge of the third particle (positive or negative): "))
    
    # Append the third particle to existing arrays
    q = np.append(q, q_third)
    xq = np.append(xq, xq_third)
    yq = np.append(yq, yq_third)

    # Create a grid for plotting
    h = 0.01  # Step size for grid
    x, y = np.meshgrid(np.arange(-4, 4+h, h), np.arange(-4, 4+h, h))

    # Calculate electric field including all particles
    EX, EY, E = calculate_electric_field(q, xq, yq, x, y)

    # Plotting
    plt.figure(figsize=(8, 6))

    # Plot electric field lines
    plt.streamplot(x, y, EX, EY, color='b', linewidth=1, arrowsize=1, arrowstyle='-')

    # Plot charges
    plt.scatter(xq, yq, c=q, s=200, cmap='bwr', edgecolors='k', linewidths=2, label='Charges')
    for i, txt in enumerate(q):
        plt.annotate(f'q{i+1} = {txt}', (xq[i], yq[i]), fontsize=12, ha='right' if xq[i] < 1.5 else 'left')

    # Plot specifications
    plt.title('Electric Field and Particle Positions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.colorbar(label='Charge (q)')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
