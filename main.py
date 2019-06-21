from dtw import *
from mfcc import *
import sounddevice as sd
from tqdm import tqdm
import time
import preprocessing

# test/test: 5,210,323
# one/one: 4,016,351
# one/seven: 3,923,839
# bolli/mamamam: 7,783,529
# red/red: 9,798,072
# red--/--red: 7,488,571


# ==============================================================
#       Sound Recorder/Sampler Initialization
# ==============================================================
bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt}'
sd.default.samplerate = 8000
sd.default.channels = 1
sd.default.dtype='int16'
duration = 2.0  # seconds

# ==============================================================
#       User Input (Speech)
# ==============================================================
input("First Sample:")
time.sleep(0.1)
print("recording...")
filename1 = sd.rec(int(duration * 8000))
sd.wait()
print("Done\n")

input("Second Sample:")
time.sleep(0.1)
print("recording...")
filename2 = sd.rec(int(duration * 8000))
sd.wait()
print("Done\n")

input("Third Sample:")
time.sleep(0.1)
print("recording...")
filename3 = sd.rec(int(duration * 8000))
sd.wait()
print("Done\n")

# ==============================================================
#       Preprocessing Input Signals
# ==============================================================
first, start1, end1 = preprocessing.trim(filename1)
second, start2, end2 = preprocessing.trim(filename2)
third, start3, end3 = preprocessing.trim(filename3)

# plt.figure()
# plt.subplot(2, 2, 1)
# plt.plot(filename1, 'b')
# plt.axvline(start1, color='r')
# plt.axvline(end1, color='r')
# plt.axvline(15000, color='g')
# plt.axvline(1000, color='g')
#
#
# plt.subplot(2, 2, 2)
# plt.plot(filename2, 'b')
# plt.axvline(start2, color='r')
# plt.axvline(end2, color='r')
# plt.axvline(15000, color='g')
# plt.axvline(1000, color='g')
#
#
# plt.subplot(2, 2, 3)
# plt.plot(first, 'b')
# plt.subplot(2, 2, 4)
# plt.plot(second, 'b')


# filename1 = 'test.wav'
# filename2 = 'test2.wav'
# filename3 = 'test3.wav'

# ==============================================================
#       Mel Coefficients Extraction
# ==============================================================
mfcc1 = MFCC(first)
mfcc2 = MFCC(second)
# mfcc3 = MFCC(filename3)
mfcc3 = MFCC(third)

    # -----
    # plt.figure()
    # plt.subplot(312)
    # plt.imshow(mfcc1, cmap=plt.cm.jet, aspect='auto') # .T transposes the output of the tile function to fit the desired shape.
    # plt.xticks(numpy.arange(0, (mfcc1).shape[1],
    # int((mfcc1).shape[1] / 4)),
    # ['0s', '0.5s', '1s', '1.5s','2.5s','3s','3.5'])
    # ax = plt.gca()
    # ax.invert_yaxis()
    # plt.title('MFCC of ' + filename1)
    # plt.subplot(313)
    # plt.imshow(mfcc2, cmap=plt.cm.jet, aspect='auto') # .T transposes the output of the tile function to fit the desired shape.
    # plt.xticks(numpy.arange(0, (mfcc2).shape[1],
    # int((mfcc2).shape[1] / 4)),
    # ['0s', '0.5s', '1s', '1.5s','2.5s','3s','3.5'])
    # ax = plt.gca()
    # ax.invert_yaxis()
    # plt.title('MFCC of ' + filename2)
    # plt.subplots_adjust(top = 1.2, hspace = 1)
    # -----
    # plt.show()
# dtw(mfcc1[0], mfcc2[0])

# ==============================================================
#       Visualisation Results
# ==============================================================
plt.figure()
total_cost = 0.0
cost = 0.0
cnt = 0
for i in range(16):
    if i < 10 or i == 12 or i == 13:
        plt.subplot(4, 4, i + 1)
        plt.plot(mfcc1[cnt], 'b-')
        plt.plot(mfcc2[cnt], 'g-')
        cost = dtw(mfcc1[cnt], mfcc2[cnt])
        plt.title('cost: ' + ("%.1f" % cost))
        total_cost += cost
        plt.legend().remove()
        cnt += 1

plt.subplot(4, 4, 11)
plt.plot(filename1, 'b')
plt.axvline(start1, color='r')
plt.axvline(end1, color='r')
plt.axvline(15000, color='g')
plt.axvline(1000, color='g')
plt.subplot(4, 4, 12)
plt.plot(filename2, 'b')
plt.axvline(start2, color='r')
plt.axvline(end2, color='r')
plt.axvline(15000, color='g')
plt.axvline(1000, color='g')
plt.subplot(4, 4, 15)
fff = numpy.concatenate([first, second])
plt.plot(first, 'b')
plt.subplot(4, 4, 16)
plt.plot(second, 'b')
plt.show()


plt.figure()
plt.subplot(2, 4, 1)
plt.plot(filename1, 'b')
plt.axvline(start1, color='r')
plt.axvline(end1, color='r')
plt.axvline(15000, color='g')
plt.axvline(1000, color='g')
plt.title("A")
plt.subplot(2, 4, 2)
plt.plot(filename2, 'b')
plt.axvline(start2, color='r')
plt.axvline(end2, color='r')
plt.axvline(15000, color='g')
plt.axvline(1000, color='g')
plt.title("B")
plt.subplot(2, 4, 4)
plt.plot(filename3, 'b')
plt.axvline(start3, color='r')
plt.axvline(end3, color='r')
plt.axvline(15000, color='g')
plt.axvline(1000, color='g')
plt.title("C")
plt.subplot(2, 4, 5)
plt.plot(first, 'b')
plt.subplot(2, 4, 6)
plt.plot(second, 'b')
plt.subplot(2, 4, 7)
plt.title("A + B")
plt.plot(numpy.concatenate([first, second]), 'b')
plt.subplot(2, 4, 8)
plt.plot(third, 'b')

# plt.subplots_adjust(left = None, right = None, top = None, wspace = 0.2, hspace = 0.9)
# plt.suptitle("Cost Measure: {:,}".format(int(total_cost)))
# # plt.tight_layout(h_pad=0.1, w_pad=0.1, pad=0.4)
#
# _green_bold = "\033[92m\033[1m"
# _red_bold = "\033[91m\033[1m"
# _end = "\033[0m"
# if total_cost <= 2500000.0:
#     print(_green_bold + "MATCH FOUND" + _end)
# else:
#     print(_red_bold + "MATCH NOT FOUND" + _end)
# print(total_cost)
plt.show()


