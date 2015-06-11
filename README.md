# bankers
Bankers - This is an implementation of the banker's deadlock algorithm

http://en.wikipedia.org/wiki/Banker%27s_algorithm


# Usage

To find out, if a deadlock occurs you need to setup the following:

1. You need a resource_vector, which is a list with the total amount of the different resources:
    e.g. 3 times Resource 1, 4 times Resource 2, 2 times Resource 3 => resource_vector = [3, 4, 2]

2. You need a "need vector", which gets stored in the deadlock's requirements list.
    e.g. self.deadlock.requirements = [[0, 8, 3], [0, 2, 4]]. This would mean process 1 wants to have 0 instances of resource 1, 8 instances of resource 2 and 3 instances of resource 3, while process 2 wants 0 instances of resource 1, 2 instances of resource 2 and 4 instances of resource 4.

3. You also need an initial occupancy list, which represents which resources have been occupied by which process.
   e.g. occupancies = [[0, 1, 0, 1], [0, 1, 0, 0]]. This would mean process 1 holds 0 instances of resource 1, 1 instance of resource 2 and so on.

4. To calculate the resource_rest_vector (which represents the remaining resources available) you call set_resource_rest_vector with a resource_vector. The resource_rest_vector then gets calculated deending on the previously set occupancies and the given resource_vector.

The resource_vector is not stored in a class-field, since it is no longer needed after the calculation of the resource_rest_vector. The occupancies- and requirements-list however are needed in each step of the algorithm and this is why they get stored as fields.


# Example

TODO


