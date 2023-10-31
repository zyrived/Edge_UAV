import random
import math


def Update_corrdinate(pop, iteration, best_pop, max_iterations):
    def temperature_function(iteration, max_iterations):
        # 使用指数函数来调整温度，可以根据需要调整参数

        return alpha * iteration / max_iterations
        # return math.exp( -alpha * iteration / max_iterations)



    # max_iterations = 1000  # 根据需要调整最大迭代次数
    pop_list = []
    beta = 0.1
    theta = 0.5
    alpha = 1

    pop_0 = pop.copy()
    pop_list.append(pop_0)
    for i in range(3):  # 生成三个扰动后的坐标矩阵
        temperature = temperature_function(iteration, max_iterations)

        if i == 0:
            # 第一个扰动：交换若干节点
            num_swaps = int(temperature * len(pop))
            print("iteration:{},num_swaps:{},temperature{}".format(iteration, num_swaps, temperature))
            pop_1 = pop.copy()
            for _ in range(num_swaps):
                # 随机选择一个节点从 best_pop 中替换到 pop_1 中
                idx1 = random.randint(0, len(pop_1) - 1)
                idx2 = random.randint(0, len(best_pop) - 1)
                pop_1[idx1] = best_pop[idx2]
            pop_list.append(pop_1)
        elif i == 1:
            # 第二个扰动：插入若干节点
            num_insertions = int(theta * temperature * len(pop))
            pop_2 = pop.copy()
            for _ in range(num_insertions):
                # 随机选择一个节点从 best_pop 中插入到 pop_2 中
                node_to_insert = random.choice(best_pop)
                insert_idx = random.randint(0, len(pop_2))
                pop_2.insert(insert_idx, node_to_insert)
            pop_list.append(pop_2)
        else:
            # 第三个扰动：随机删除若干节点
            num_deletions = int(beta * math.exp(-temperature) * len(pop))
            pop_3 = pop.copy()
            for _ in range(num_deletions):
                # 随机选择一个节点并从列表中删除
                if len(pop_3) > 1:
                    del_idx = random.randint(0, len(pop_3) - 1)
                    pop_3.pop(del_idx)
            pop_list.append(pop_3)

    return pop_list


# 示例用法
if __name__ == "__main__":

    pop = [(374.5, 950.7, 100), (732.0, 598.7, 100), (156.0, 156.0, 100), (58.1, 866.2, 100),
            (601.1, 708.1, 100), (20.6, 969.9, 100), (832.4, 212.3, 100), (181.8, 183.4, 100),
            (304.2, 524.8, 100), (431.9, 291.2, 100), (611.9, 139.5, 100), (292.1, 366.4, 100),
            (456.1, 785.2, 100), (199.7, 514.2, 100), (592.4, 46.5, 100), (607.5, 170.5, 100),
            (65.1, 948.9, 100), (965.6, 808.4, 100), (304.6, 97.7, 100), (684.2, 440.2, 100),
            (122.0, 495.2, 100), (34.4, 909.3, 100), (258.8, 662.5, 100), (311.7, 520.1, 100),
            (546.7, 184.9, 100), (969.6, 775.1, 100), (939.5, 894.8, 100), (597.9, 921.9, 100),
            (88.5, 196.0, 100), (45.2, 325.3, 100), (388.7, 271.3, 100), (828.7, 356.8, 100),
            (280.9, 542.7, 100), (140.9, 802.2, 100), (74.6, 986.9, 100), (772.2, 198.7, 100),
            (5.5, 815.5, 100), (706.9, 729.0, 100), (771.3, 74.0, 100), (358.5, 115.9, 100),
            (863.1, 623.3, 100), (330.9, 63.6, 100), (311.0, 325.2, 100), (729.6, 637.6, 100),
            (887.2, 472.2, 100), (119.6, 713.2, 100), (760.8, 561.3, 100), (771.0, 493.8, 100),
            (522.7, 427.5, 100), (25.4, 107.9, 100), (31.4, 636.4, 100), (314.4, 508.6, 100),
            (907.6, 249.3, 100), (410.4, 755.6, 100), (228.8, 77.0, 100), (289.8, 161.2, 100),
            (929.7, 808.1, 100), (633.4, 871.5, 100), (803.7, 186.6, 100), (892.6, 539.3, 100),
            (807.4, 896.1, 100), (318.0, 110.1, 100), (227.9, 427.1, 100), (818.0, 860.7, 100),
            (7.0, 510.7, 100), (417.4, 222.1, 100), (119.9, 337.6, 100), (942.9, 323.2, 100),
            (518.8, 703.0, 100), (363.6, 971.8, 100), (962.4, 251.8, 100), (497.2, 300.9, 100),
            (284.8, 36.9, 100), (609.6, 502.7, 100), (51.5, 278.6, 100), (908.3, 239.6, 100),
            (144.9, 489.5, 100), (985.7, 242.1, 100), (672.1, 761.6, 100), (237.6, 728.2, 100),
            (367.8, 632.3, 100), (633.5, 535.8, 100), (90.3, 835.3, 100), (320.8, 186.5, 100),
            (40.8, 590.9, 100), (677.6, 16.6, 100), (512.1, 226.5, 100), (645.2, 174.4, 100),
            (690.9, 386.7, 100), (936.7, 137.5, 100), (341.1, 113.5, 100), (924.7, 877.3, 100),
            (257.9, 660.0, 100), (817.2, 555.2, 100), (529.7, 241.9, 100), (93.1, 897.2, 100),
            (900.4, 633.1, 100), (339.0, 349.2, 100), (726.0, 897.1, 100), (887.1, 779.9, 100)]
    iteration = 3000 # 迭代次数（根据需要自行设置）
    best_pop = [(200.0, 200.0, 100), (500.0, 500.0, 100), (800.0, 800.0, 100)]
    max_iteration = 10000
    result = Update_corrdinate(pop, iteration, best_pop, max_iteration)
    for i, p in enumerate(result):
        print(f"pop_{i + 1}: {p}")



