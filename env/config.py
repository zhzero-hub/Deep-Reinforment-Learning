# Simulation parameters
Thermal_noise_spectrum_density = 3.9810717055349565e-21  # -174dBm/Hz -> 3.9810717055349565e-21W/Hz
Communication_bandwidth = 5 * 1000000  # MHz->Hz
Communication_bandwidth_range = (5, 25)
Transmit_power = 0.1  # dBm->W 0.09999999999999998W->0.1W
Average_task_arrival_rate = 0.6  # request/sec
Average_task_arrival_rate_range = (0.6, 1.0)
Noise_figure = 5  # dB
Intensity_of_compressed_DNN_for_serviceI = 80  # cycles/bit
Intensity_of_compressed_DNN_for_serviceII = 160  # cycles/bit
Intensity_of_uncompressed_DNN_for_service = (200, 400)  # cycles/bit
Device_server_CPU_frequency = 0.1 * 1000000000  # GHz->Hz
Edge_server_CPU_frequency = 2.0 * 1000000000  # GHz->Hz
Number_of_devices = (5, 5)
Number_of_Type_I_devices = Number_of_devices[0]
Number_of_Type_II_devices = Number_of_devices[1]
Number_of_total_devices = Number_of_Type_I_devices + Number_of_Type_II_devices
Time_slot_duration = 1  # second
Balance_parameter = 0.05
Unit_penalty_for_queue_overflow = 1
Accuracy_of_compressed_DNN = (0.8, 0.8)
Accuracy_of_uncompressed_DNN = (1, 1)
Local_queue_capacity = 3.84 * 1024 * 1024  # MB->B
Edge_queue_capacity = 19.2 * 1024 * 1024  # MB->B

# Parameters of the proposed RL-based algorithm
Time_slots_per_episode = 200

Number_of_services = 2
Channel_condition_transition_matrix = ((0.3, 0.7, 0.0), (0.25, 0.5, 0.25), (0.0, 0.7, 0.3))
Sample_rate_base = 48000  # Hz
Sample_rate_types = (0.25, 0.5, 0.75, 1.0)  # 1/4, 2/4, 3/4, 4/4
Accuracy_to_sample_rate = (0.59, 0.884, 0.950, 0.987)
Raw_data_size = 768000  # bit
Channel_gain_good = 6 * 10e-13
Channel_gain_normal = 4 * 10e-13
Channel_gain_bad = 2 * 10e-13
Long_term_accuracy = (0.8, 0.9)
Long_term_accuracy_to_service_I = Long_term_accuracy[0]
Long_term_accuracy_to_service_II = Long_term_accuracy[1]
Initial_sample_rate = [0, 0, 0, 1]
