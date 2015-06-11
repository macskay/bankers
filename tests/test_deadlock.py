# -*- encoding: utf-8 -*-

from unittest import TestCase
from bankers.deadlock import Deadlock


class DeadlockTestCase(TestCase):
    def setUp(self):
        self.deadlock = Deadlock()
        self.deadlock.resource_rest_vector = [0, 7, 5, 6]

    def test_when_all_processes_have_terminated_return_minus_one(self):
        self.deadlock.requirements = [[-1, -1, -1, -1], [-1, -1, -1, -1]]
        found_process = self.deadlock.find_process_that_meets_requirements()
        self.assertEqual(found_process, -1)

    def test_when_given_a_process_that_is_less_than_or_equal_to_requirements_return_index(self):
        self.deadlock.requirements = [[0, 8, 3, 5], [0, 2, 4, 6]]
        found_process = self.deadlock.find_process_that_meets_requirements()
        self.assertEqual(found_process, 1)

    def test_when_a_process_was_found_everything_needs_to_be_updated(self):
        self.deadlock.requirements = [[0, 8, 3, 5], [0, 2, 4, 6]]
        self.deadlock.occupancies = [[0, 0, 0, 0], [0, 0, 0, 0]]
        found_process = 1
        self.deadlock.update_matrices(found_process)
        expected_result_requirements = [[0, 8, 3, 5], [-1, -1, -1, -1]]
        self.assertEquals(expected_result_requirements[1], self.deadlock.requirements[1])

    def test_when_given_a_resource_vector_set_resource_rest_vector(self):
        resource_vector = [1, 2, 1, 3]
        self.deadlock.occupancies = [[0, 1, 0, 1], [0, 1, 0, 0]]
        self.deadlock.resource_rest_vector = list()
        self.deadlock.set_resource_rest_vector(resource_vector)
        result = [1, 0, 1, 2]
        self.assertEquals(result, self.deadlock.resource_rest_vector)

    def test_when_given_a_no_deadlock_dataset_return_false(self):
        resource_vector = [2, 2]
        self.deadlock.occupancies = [[0, 1], [1, 0], [1, 0], [0, 1]]
        self.deadlock.requirements = [[1, 0], [0, 0], [0, 1], [0, 0]]
        self.deadlock.resource_rest_vector = list()
        self.deadlock.set_resource_rest_vector(resource_vector)
        self.assertFalse(self.deadlock.find_deadlock())

    def test_when_given_a_deadlock_dataset_return_true(self):
        resource_vector = [1, 2, 1, 3]
        self.deadlock.occupancies = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0]]
        self.deadlock.requirements = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
        self.deadlock.resource_rest_vector = list()
        self.deadlock.set_resource_rest_vector(resource_vector)
        self.assertTrue(self.deadlock.find_deadlock())