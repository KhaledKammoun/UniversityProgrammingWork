from mrjob.job import MRJob
from mrjob.step import MRStep

class SpendByCustomer(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words, reducer=self.reducer_sum_counts),
            MRStep(reducer=self.reducer_compute_mean)
        ]

    def mapper_get_words(self, _, line): 
        customerID, _, orderAmount = line.split(',')
        yield customerID, float(orderAmount)
    
    def reducer_sum_counts(self, customerID, orderAmounts):
        # Convert generator to a list to get its length
        orderAmounts_list = list(orderAmounts)
        # Calculate sum of order amounts and count of orders for each customer
        total_order_amount = sum(orderAmounts_list)
        count_orders = len(orderAmounts_list)
        yield customerID, (total_order_amount, count_orders)

    def reducer_compute_mean(self, customerID, order_stats):
        total_sum = 0
        total_count = 0
        for sum_value, count in order_stats:
            total_sum += sum_value
            total_count += count
        mean = total_sum / total_count
        yield customerID, round(mean, 2)

if __name__ == '__main__':
    SpendByCustomer.run()
