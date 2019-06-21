
import math

# def find_signal(period, sensitivity, signal, start, end):
#     pre_mean = 0.0
#     pre_stdev = 0.0
#     for i in range(period):
#         pre_mean += signal[i]
#     mean = pre_mean / len(signal)
#     for i in range(period):
#         pre_stdev += (signal[i] - mean) ** 2
#     stdev = math.sqrt(pre_stdev / len(signal))
#
#     for i in range(start, len(signal)):
#         r = abs(signal[i] - mean)/stdev
#         if r >= sensitivity:
#             return i



def trim(signal):
    period = 1000
    sensitivity_pre = 1000.0
    sensitivity_post = 40.0
    pre_mean = 0.0
    pre_stdev = 0.0
    for i in range(period):
        pre_mean += signal[i]
    mean = pre_mean / len(signal)
    for i in range(period):
        pre_stdev += (signal[i] - mean) ** 2
    stdev = math.sqrt(pre_stdev / len(signal))

    start_pos = 0
    for i in range(period, len(signal)):
        r = abs(signal[i] - mean)/stdev
        if r >= sensitivity_pre:
            start_pos = i
            break

    pre_mean = 0.0
    pre_stdev = 0.0
    for i in reversed(range(len(signal) - period, len(signal))):
        pre_mean += signal[i]
    mean = pre_mean / len(signal)
    for i in reversed(range(len(signal) - period, len(signal))):
        pre_stdev += (signal[i] - mean) ** 2
    stdev = math.sqrt(pre_stdev / len(signal))

    end_pos = len(signal) - 1
    for i in reversed(range(start_pos, len(signal) - period)):
        r = abs(signal[i] - mean) / stdev
        if r >= sensitivity_post:
            end_pos = i
            break







    # max = 0
    # for i in range(800):
    #     max = signal[i] if signal[i] > max else max
    #
    # # max += 10
    # max = 100
    # start_pos = 800
    # for i in range(800, len(signal)):
    #     fff = signal[i]
    #     if signal[i] > max:
    #         start_pos = i - 100
    #         break
    #     else:
    #         continue
    #
    # counter = 0
    # end_pos = start_pos + 25
    # for i in range(start_pos + 25, len(signal)):
    #     a = signal[i]
    #     if signal[i] < max:
    #         counter += 1
    #         if counter == 500:
    #             end_pos = i - 500
    #             break
    #     else:
    #         counter = 0
    return signal[start_pos:end_pos], start_pos, end_pos















