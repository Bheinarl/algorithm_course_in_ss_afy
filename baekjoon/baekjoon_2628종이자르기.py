width, height = map(int, input().split())
cut_time = int(input())
hei_arr = [0]
hei_arr += [height]
wid_arr = [0]
wid_arr += [width]
for _ in range(cut_time):
    w_h, num = map(int, input().split())

    if w_h == 1:
        wid_arr += [num]
    else:
        hei_arr += [num]

wid_arr.sort()
hei_arr.sort()

max_area = 0
for i in range(len(wid_arr)-1):
    for j in range(len(hei_arr)-1):
        area = (wid_arr[i+1] - wid_arr[i]) * (hei_arr[j+1] - hei_arr[j])

        if max_area < area:
            max_area = area

print(max_area)
