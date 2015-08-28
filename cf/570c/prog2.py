def run():
    n, m = map(lambda x: int(x), raw_input().split(' '))
    data = map(lambda x: 1 if x == '.' else 0, raw_input())

    current_result = sum([
                            1 if data[idx] == 1 and data[idx + 1] == 1 else 0
                            for idx in range(0, n - 1)
                        ])

    for _ in xrange(m):
        idx, new_data_item = raw_input().split(' ')
        idx = int(idx) - 1
        new_data_item = 1 if new_data_item == '.' else 0
        if new_data_item == data[idx]:
            print current_result
            continue

        if new_data_item == 0:
            # 1 to 0
            if idx > 0 and data[idx - 1] == 1:
                current_result -= 1
            if idx < n - 1 and data[idx + 1] == 1:
                current_result -= 1
        elif new_data_item == 1:
            # 0 to 1
            if idx > 0 and data[idx - 1] == 1:
                current_result += 1
            if idx < n - 1 and data[idx + 1] == 1:
                current_result += 1

        data[idx] = new_data_item
        print current_result


if __name__ == '__main__':
    run()
