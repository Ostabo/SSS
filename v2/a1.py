import cv2
import numpy as np

img_arr = []

for i in range(10):
    img_read = cv2.imread("./data/default" + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
    img_arr.append(img_read)

img = np.mean(img_arr, axis=0, dtype=float)
print(img)
sub_arrays = []
slicing_index = []

step = 20
threshold = 20
for i in range(0, len(img[0]) - step, step):
    if abs(int(img[0, i + step]) - int(img[0, i])) > threshold:
        # print("Slicing at index: " + str(i) + " with value: "
        #       + str(img[0][i]) + " and next value: " + str(img[0][i + 1]))
        slicing_index.append(i)
        sub_arrays.append(img[:, i-99:i])

slicing_index.append(len(img[0]))  # add last index
sub_arrays.append(img[:, len(img[0]) - 98:len(img[0]) - 1])

print(slicing_index)
print(sub_arrays)

res_mean = []
res_std = []
i = 0
for x in sub_arrays:
    mean = np.round(np.mean(x), 2)
    res_mean.append(mean)
    std = np.round(np.std(x), 2)
    res_std.append(std)

    print(f"Index: {i} , Mean: {mean}, Std: {std}")
    i += 1

# visualize sub arrays
for i in range(len(sub_arrays)):
    cv2.imshow("sub_array" + str(i), sub_arrays[i].astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
