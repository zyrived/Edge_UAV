from Algorithm_2_COPY import generate_populations
from Algorithm_3_UCA import cluster_algorithm
from Algorithm_4_TSA import tabu_search_algorithm
from generate_random_population import generate_random_population
from Evaluate_Edge_UAV import calculate_fitness
from evolutionary_operators_DE import evoluationary_operators_DE
from Algorithm_2_Update_coordinate import Update_corrdinate

import random
import numpy as np


class UE:
    def __init__(self, num_UEs, seed=41):
        self.x_range = 1000  # 设置UE的随机范围
        self.y_range = 1000
        self.seed = seed  # 设置随机种子
        self.num_UEs = num_UEs

    def generate_random_UEs(self):

        if self.seed is not None:
            np.random.seed(self.seed)

        self.UEs = []

        for _ in range(self.num_UEs):
            x = round(np.random.uniform(0, self.x_range), 1)
            y = round(np.random.uniform(0, self.y_range), 1)
            self.UEs.append((x, y))
        return self.UEs


class Edge_Uav:
    def __init__(self, pop_size, UEs):
        self.Iteration = 1
        self.Iteration_max = 10000  # Set the maximum function evaluations
        self.width_max = 1000
        self.height_max = 1000
        self.Max_iteration_path = 20
        self.pop_size = pop_size
        self.UEs = UEs

        # self.pop = self.initialize_population()

    def initialize_population(self):
        # Implement the population initialization
        self.pop = generate_random_population(self.pop_size, self.width_max, self.height_max)
        pass

    def algorithm_3_UCA(self, pop):
        # TODO: 聚类算法
        cluster = cluster_algorithm(pop)
        # self.cluster_optimal =  [sub_list for sub_list in self.cluster if len(sub_list) > 2]
        return cluster

    def algorithm_4_TSA(self, cluster, pop):
        # Implement Algorithm 4 (TSA)
        UAv = tabu_search_algorithm(cluster, self.Max_iteration_path, pop)
        return UAv

    def evaluate(self, pop, UAv):
        # Implement the evaluation function (18a)
        fitness = calculate_fitness(self.UEs, pop, UAv)
        return fitness

    def reproduce(self):
        # Implement the reproduction function using DE operators
        pop_0 = evoluationary_operators_DE(self.pop)
        return pop_0
        pass

    def algorithm_2(self, offspring):
        # Implement Algorithm 2
        insert = random.choice(self.pop)
        pop_1, pop_2, pop_3 = generate_populations(offspring, insert)
        return pop_1, pop_2, pop_3

    def algorithm_2_Update_coordinate(self, offspring, iteration, best_pop):
        pop_list = Update_corrdinate(offspring, iteration, best_pop, self.Iteration_max)
        return pop_list

    def optimize(self):

        # 初始化阶段
        self.initialize_population()
        SPs_cluster = self.algorithm_3_UCA(self.pop)
        UAv = self.algorithm_4_TSA(SPs_cluster, self.pop)
        self.fitness = self.evaluate(self.pop, UAv)
        self.Iteration += 1
        variance_threshold = 0.0001  # 设置一个方差的阈值，根据需要调整
        recent_fitness = []  # 存储最近1000次的fitness值

        # 算法优化阶段
        while self.Iteration < self.Iteration_max:
            # 差分进化算法更新种群坐标
            offspring = self.reproduce()
            # 添加正则化规则
            # pop_1, pop_2, pop_3 = self.algorithm_2(offspring)
            pop_list = self.algorithm_2_Update_coordinate(offspring, self.Iteration, self.pop)

            for pop in pop_list:
                cluster = self.algorithm_3_UCA(pop)
                UAv = self.algorithm_4_TSA(cluster, pop)
                fitness = self.evaluate(pop, UAv)
                if len(fitness) == 1:
                    if fitness < self.fitness:
                        self.pop = pop
                        self.fitness = fitness
                    # 实时更新最佳种群和最佳适应度值
                else:
                    print("len fitness > 1")
            recent_fitness.append(self.fitness)
            self.Iteration += 2

            # 检查是否需要计算方差和提前结束循环
            if self.Iteration % 2000== 0:  # 每二十次循环
                if self.Iteration >= 500:  # 至少需要十次次循环才能计算方差
                    variance = np.var(recent_fitness)  # 计算方差
                    if variance < variance_threshold:  # 方差小于阈值
                        print("方差为{}，此时已达最佳适应度，适应度值为{}".format(variance, self.fitness))
                        # break  # 提前结束循环
                    else:
                        print("方差为 {}，继续循环...".format(variance))
                recent_fitness = []  # 置空

            print("第{}次循环此时最佳适应度为：{}".format(self.Iteration, self.fitness))

            # Select the best population among pop, pop_1, pop_2, and pop_3

        return self.pop, self.fitness  # Return the best solution


if __name__ == "__main__":
    # 假设，一个UE选择一个SPs进行传输，则初始化POP的数量，假设=UE的数量。
    # 随机设置UE的位置，生成一个UE的类。
    # 初始化UE
    num_UE = 100
    num_SPS = num_UE
    UEs = UE(num_UE).generate_random_UEs()

    # 开始优化
    Algorithm = Edge_Uav(num_SPS, UEs)
    Algorithm.optimize()
    print(Algorithm.fitness)