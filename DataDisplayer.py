import matplotlib.pyplot as plt

class DataDisplayer:
    def __init__(self):
        self.list_chosen_data_managers = []
        self.chosen_stock_temp_container = []

    def testCase(self):
        x = [10.20, 10.30, 10.40]
        y = [[2.3, 2.4, 2.5], [4.2, 4.3, 4.1], [20.1, 20.4, 19]]

        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title("Stock Prices vs Time")
        for i in range(len(y)):
            plt.plot(x, [pt[i] for pt in y], label='id %s' % i)
        plt.legend()
        plt.show()


    def testCase2(self):
        # line 1 points
        x1 = [1, 2, 3]
        y1 = [2, 4, 1]
        # plotting the line 1 points
        plt.plot(x1, y1, label="line 1")

        # line 2 points
        x2 = [1, 2, 3]
        y2 = [4, 1, 3]
        # plotting the line 2 points
        plt.plot(x2, y2, label="line 2")

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')
        # giving a title to my graph
        plt.title('Two lines on same graph!')

        # show a legend on the plot
        plt.legend()

        # function to show the plot
        plt.show()


    def testCase3(self, dataList):
        # x axis values


        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # corresponding y axis values
        # y = dataList#[39.27, 39.30, 39.38, 39.35, 39.30, 39.26, 39.35, 39.40, 39.37, 39.29 ]


        x = []
        y = []
        stockCount = 0
        for stock in dataList:
            stockCount += 1
            x.append(stockCount)
            y.append(float(stock["last"]))

        print(x[0:50])
        print(y[0:50])
        # plotting the points
        plt.plot(x, y, color='blue', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='black', markersize=6)

        # setting x and y axis range
        plt.xlim(1, 51)
        plt.ylim(39.10, 39.40)

        # naming the x axis
        plt.xlabel('Time - axis')
        # naming the y axis
        plt.ylabel('Price - axis')

        # giving a title to my graph
        plt.title('Magic graph of '+ dataList[0]["symbol"])

        # function to show the plot
        plt.show()