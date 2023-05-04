import numpy as np
def is_pareto_optimal(fitness):
    """
    Find the pareto-optimal points
    :param fitness: An (n_points, n_fitness) array (each data in a row)
    :return: A (n_points,) boolean array, indicating whether each point is Pareto optimal
    """
    is_efficient = np.ones(fitness.shape[0], dtype=bool)
    for i, c in enumerate(fitness):
        if is_efficient[i]:
            is_efficient[is_efficient] = np.any(fitness[is_efficient] > c, axis=1)
            is_efficient[i] = True  # And keep self
    return is_efficient
