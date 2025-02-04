#! /usr/bin/env python3

import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('matrix_ops.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

class MatrixOps:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def matrix_add(self):
        logger.info(self.matrix_1 + self.matrix_2)
        return self.matrix_1 + self.matrix_2

    def matrix_sub(self):
        logger.info(self.matrix_1 - self.matrix_2)
        return self.matrix_1 - self.matrix_2
    
    def matrix_transpose(self):
        logger.info(self.matrix_1.T)
        return self.matrix_1.T

    def matrix_determinant(self):
        logger.info(np.linalg.det(self.matrix_1))
        return np.linalg.det(self.matrix_1)
    
    def matrix_inverse(self):
        logger.info(np.linalg.inv(self.matrix_1))
        return np.linalg.inv(self.matrix_1)
    
    def matrix_trace(self):
        logger.info(np.trace(self.matrix_1))
        return np.trace(self.matrix_1)
    
    def matrix_rank(self):
        logger.info(np.linalg.matrix_rank(self.matrix_1))
        return np.linalg.matrix_rank(self.matrix_1)
    
    def matrix_eigenvalues(self):
        logger.info(np.linalg.eigvals(self.matrix_1))
        return np.linalg.eigvals(self.matrix_1)

    def matrix_eigenvectors(self):
        logger.info(np.linalg.eig(self.matrix_1))
        return np.linalg.eig(self.matrix_1)
    
    def matrix_diagonalization(self):
        logger.info(np.linalg.eig(self.matrix_1))
        return np.linalg.eig(self.matrix_1)
    
    def matrix_singular_value_decomposition(self):
        logger.info(np.linalg.svd(self.matrix_1))
        return np.linalg.svd(self.matrix_1)

    def matrix_svd(self):
        logger.info(np.linalg.svd(self.matrix_1))
        return np.linalg.svd(self.matrix_1)

def main():
    matrix_ops = MatrixOps(matrix_1, matrix_2)
    matrix_ops.matrix_add()
    matrix_ops.matrix_sub()
    matrix_ops.matrix_transpose()
    matrix_ops.matrix_determinant()
    matrix_ops.matrix_inverse()
    matrix_ops.matrix_trace()
    matrix_ops.matrix_rank()
    matrix_ops.matrix_eigenvalues()
    matrix_ops.matrix_eigenvectors()
    matrix_ops.matrix_diagonalization()
    matrix_ops.matrix_singular_value_decomposition()
    matrix_ops.matrix_svd()

if __name__ == "__main__":
    main()