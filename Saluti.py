class Saluti:

   
    def get_movimento(self):
        return self.movimento



    def __init__(self):
        self.movimento={}

        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.145772, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.145772, [3, -0.173333, 0], [3, 0.16, 0]], [-0.145772, [3, -0.16, 0], [3, 0.146667, 0]], [-0.145772, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.145772, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.145772, [3, -0.146667, 0], [3, 0.16, 0]], [-0.145772, [3, -0.16, 0], [3, 0.933333, 0]], [-0.145772, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["HeadPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.0138481, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.0138481, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0138481, [3, -0.16, 0], [3, 0.146667, 0]], [-0.0138481, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0138481, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.0138481, [3, -0.146667, 0], [3, 0.16, 0]], [-0.0138481, [3, -0.16, 0], [3, 0.933333, 0]], [-0.0138481, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["HeadYaw"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.0950661, [3, -0.506667, 0], [3, 0.173333, 0]], [0.095066, [3, -0.173333, 0], [3, 0.16, 0]], [0.095066, [3, -0.16, 0], [3, 0.146667, 0]], [0.095066, [3, -0.146667, 0], [3, 0.133333, 0]], [0.095066, [3, -0.133333, 0], [3, 0.146667, 0]], [0.095066, [3, -0.146667, 0], [3, 0.16, 0]], [0.095066, [3, -0.16, 0], [3, 0.933333, 0]], [0.093532, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LAnklePitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.115008, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.10427, [3, -0.173333, 0], [3, 0.16, 0]], [-0.10427, [3, -0.16, 0], [3, 0.146667, 0]], [-0.10427, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.10427, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.10427, [3, -0.146667, 0], [3, 0.16, 0]], [-0.10427, [3, -0.16, 0], [3, 0.933333, 0]], [-0.108872, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LAnkleRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.41874, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.418739, [3, -0.173333, 0], [3, 0.16, 0]], [-0.418739, [3, -0.16, 0], [3, 0.146667, 0]], [-0.418739, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.418739, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.418739, [3, -0.146667, 0], [3, 0.16, 0]], [-0.418739, [3, -0.16, 0], [3, 0.933333, 0]], [-0.417205, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LElbowRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-1.17815, [3, -0.506667, 0], [3, 0.173333, 0]], [-1.17815, [3, -0.173333, 0], [3, 0.16, 0]], [-1.17815, [3, -0.16, 0], [3, 0.146667, 0]], [-1.17815, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.17815, [3, -0.133333, 0], [3, 0.146667, 0]], [-1.17815, [3, -0.146667, 0], [3, 0.16, 0]], [-1.17815, [3, -0.16, 0], [3, 0.933333, 0]], [-1.18736, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LElbowYaw"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.2892, [3, -0.506667, 0], [3, 0.173333, 0]], [0.2892, [3, -0.173333, 0], [3, 0.16, 0]], [0.2892, [3, -0.16, 0], [3, 0.146667, 0]], [0.2892, [3, -0.146667, 0], [3, 0.133333, 0]], [0.2892, [3, -0.133333, 0], [3, 0.146667, 0]], [0.2892, [3, -0.146667, 0], [3, 0.16, 0]], [0.2892, [3, -0.16, 0], [3, 0.933333, 0]], [0.2868, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LHand"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.124296, [3, -0.506667, 0], [3, 0.173333, 0]], [0.124296, [3, -0.173333, 0], [3, 0.16, 0]], [0.124296, [3, -0.16, 0], [3, 0.146667, 0]], [0.124296, [3, -0.146667, 0], [3, 0.133333, 0]], [0.124296, [3, -0.133333, 0], [3, 0.146667, 0]], [0.124296, [3, -0.146667, 0], [3, 0.16, 0]], [0.124296, [3, -0.16, 0], [3, 0.933333, 0]], [0.119694, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LHipPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.122762, [3, -0.506667, 0], [3, 0.173333, 0]], [0.122762, [3, -0.173333, 0], [3, 0.16, 0]], [0.122762, [3, -0.16, 0], [3, 0.146667, 0]], [0.122762, [3, -0.146667, 0], [3, 0.133333, 0]], [0.122762, [3, -0.133333, 0], [3, 0.146667, 0]], [0.122762, [3, -0.146667, 0], [3, 0.16, 0]], [0.122762, [3, -0.16, 0], [3, 0.933333, 0]], [0.11816, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LHipRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.177902, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.177901, [3, -0.173333, 0], [3, 0.16, 0]], [-0.177901, [3, -0.16, 0], [3, 0.146667, 0]], [-0.177901, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.177901, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.177901, [3, -0.146667, 0], [3, 0.16, 0]], [-0.177901, [3, -0.16, 0], [3, 0.933333, 0]], [-0.174835, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LHipYawPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.092082, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.092082, [3, -0.173333, 0], [3, 0.16, 0]], [-0.092082, [3, -0.16, 0], [3, 0.146667, 0]], [-0.092082, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.092082, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.092082, [3, -0.146667, 0], [3, 0.16, 0]], [-0.092082, [3, -0.16, 0], [3, 0.933333, 0]], [-0.093616, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LKneePitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[1.43885, [3, -0.506667, 0], [3, 0.173333, 0]], [1.43885, [3, -0.173333, 0], [3, 0.16, 0]], [1.43885, [3, -0.16, 0], [3, 0.146667, 0]], [1.43885, [3, -0.146667, 0], [3, 0.133333, 0]], [1.43885, [3, -0.133333, 0], [3, 0.146667, 0]], [1.43885, [3, -0.146667, 0], [3, 0.16, 0]], [1.43885, [3, -0.16, 0], [3, 0.933333, 0]], [1.43271, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LShoulderPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.197844, [3, -0.506667, 0], [3, 0.173333, 0]], [0.197844, [3, -0.173333, 0], [3, 0.16, 0]], [0.197844, [3, -0.16, 0], [3, 0.146667, 0]], [0.197844, [3, -0.146667, 0], [3, 0.133333, 0]], [0.197844, [3, -0.133333, 0], [3, 0.146667, 0]], [0.197844, [3, -0.146667, 0], [3, 0.16, 0]], [0.197844, [3, -0.16, 0], [3, 0.933333, 0]], [0.196309, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LShoulderRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.125746, [3, -0.506667, 0], [3, 0.173333, 0]], [0.125746, [3, -0.173333, 0], [3, 0.16, 0]], [0.125746, [3, -0.16, 0], [3, 0.146667, 0]], [0.125746, [3, -0.146667, 0], [3, 0.133333, 0]], [0.125746, [3, -0.133333, 0], [3, 0.146667, 0]], [0.125746, [3, -0.146667, 0], [3, 0.16, 0]], [0.125746, [3, -0.16, 0], [3, 0.933333, 0]], [0.136484, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["LWristYaw"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.0828779, [3, -0.506667, 0], [3, 0.173333, 0]], [0.0828778, [3, -0.173333, 0], [3, 0.16, 0]], [0.0828778, [3, -0.16, 0], [3, 0.146667, 0]], [0.0828778, [3, -0.146667, 0], [3, 0.133333, 0]], [0.0828778, [3, -0.133333, 0], [3, 0.146667, 0]], [0.0828778, [3, -0.146667, 0], [3, 0.16, 0]], [0.0828778, [3, -0.16, 0], [3, 0.933333, 0]], [0.0874801, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RAnklePitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.116626, [3, -0.506667, 0], [3, 0.173333, 0]], [0.116626, [3, -0.173333, 0], [3, 0.16, 0]], [0.105888, [3, -0.16, 0], [3, 0.146667, 0]], [0.116626, [3, -0.146667, 0], [3, 0.133333, 0]], [0.105888, [3, -0.133333, 0], [3, 0.146667, 0]], [0.116626, [3, -0.146667, 0], [3, 0.16, 0]], [0.105888, [3, -0.16, 0], [3, 0.933333, 0]], [0.115092, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RAnkleRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.751702, [3, -0.506667, 0], [3, 0.173333, 0]], [0.707216, [3, -0.173333, 0], [3, 0.16, 0]], [0.849878, [3, -0.16, 0], [3, 0.146667, 0]], [0.707216, [3, -0.146667, 0], [3, 0.133333, 0]], [0.849878, [3, -0.133333, 0], [3, 0.146667, 0]], [0.707216, [3, -0.146667, 0], [3, 0.16, 0]], [0.849878, [3, -0.16, 0], [3, 0.933333, 0]], [0.405018, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RElbowRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.665714, [3, -0.506667, 0], [3, 0.173333, 0]], [0.759288, [3, -0.173333, 0], [3, 0.16, 0]], [0.716335, [3, -0.16, 0], [3, 0.146667, 0]], [0.759288, [3, -0.146667, 0], [3, 0.133333, 0]], [0.716335, [3, -0.133333, 0], [3, 0.146667, 0]], [0.759288, [3, -0.146667, 0], [3, 0.16, 0]], [0.716335, [3, -0.16, 0], [3, 0.933333, 0]], [1.18574, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RElbowYaw"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.8244, [3, -0.506667, 0], [3, 0.173333, 0]], [0.8244, [3, -0.173333, 0], [3, 0.16, 0]], [0.8244, [3, -0.16, 0], [3, 0.146667, 0]], [0.8244, [3, -0.146667, 0], [3, 0.133333, 0]], [0.8244, [3, -0.133333, 0], [3, 0.146667, 0]], [0.8244, [3, -0.146667, 0], [3, 0.16, 0]], [0.8244, [3, -0.16, 0], [3, 0.933333, 0]], [0.2852, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RHand"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[0.122678, [3, -0.506667, 0], [3, 0.173333, 0]], [0.122678, [3, -0.173333, 0], [3, 0.16, 0]], [0.122678, [3, -0.16, 0], [3, 0.146667, 0]], [0.122678, [3, -0.146667, 0], [3, 0.133333, 0]], [0.122678, [3, -0.133333, 0], [3, 0.146667, 0]], [0.122678, [3, -0.146667, 0], [3, 0.16, 0]], [0.122678, [3, -0.16, 0], [3, 0.933333, 0]], [0.122678, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RHipPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.113474, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.113474, [3, -0.173333, 0], [3, 0.16, 0]], [-0.113474, [3, -0.16, 0], [3, 0.146667, 0]], [-0.113474, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.113474, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.113474, [3, -0.146667, 0], [3, 0.16, 0]], [-0.113474, [3, -0.16, 0], [3, 0.933333, 0]], [-0.108872, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RHipRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.177902, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.177901, [3, -0.173333, 0], [3, 0.16, 0]], [-0.177901, [3, -0.16, 0], [3, 0.146667, 0]], [-0.177901, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.177901, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.177901, [3, -0.146667, 0], [3, 0.16, 0]], [-0.177901, [3, -0.16, 0], [3, 0.933333, 0]], [-0.174835, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RHipYawPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.101202, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.101202, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0904641, [3, -0.16, 0], [3, 0.146667, 0]], [-0.101202, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0904641, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.101202, [3, -0.146667, 0], [3, 0.16, 0]], [-0.0904641, [3, -0.16, 0], [3, 0.933333, 0]], [-0.091998, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RKneePitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.812978, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.812978, [3, -0.173333, 0], [3, 0.16, 0]], [-0.812978, [3, -0.16, 0], [3, 0.146667, 0]], [-0.812978, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.812978, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.812978, [3, -0.146667, 0], [3, 0.16, 0]], [-0.812978, [3, -0.16, 0], [3, 0.933333, 0]], [1.44354, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RShoulderPitch"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.312978, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.541544, [3, -0.173333, 0], [3, 0.16, 0]], [-0.190258, [3, -0.16, 0], [3, 0.146667, 0]], [-0.541544, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.190258, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.541544, [3, -0.146667, 0], [3, 0.16, 0]], [-0.190258, [3, -0.16, 0], [3, 0.933333, 0]], [-0.191792, [3, -0.933333, 0], [3, 0, 0]]]

        self.movimento["RShoulderRoll"] = [times,keys]
        times = [1.48, 2, 2.48, 2.92, 3.32, 3.76, 4.24, 7.04]
        keys = [[-0.334454, [3, -0.506667, 0], [3, 0.173333, 0]], [-0.214803, [3, -0.173333, 0], [3, 0.16, 0]], [-0.512397, [3, -0.16, 0], [3, 0.146667, 0]], [-0.214803, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.512397, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.214803, [3, -0.146667, 0], [3, 0.16, 0]], [-0.512397, [3, -0.16, 0], [3, 0.933333, 0]], [0.0827939, [3, -0.933333, 0], [3, 0, 0]]]
        self.movimento["RWristYaw"] = [times,keys]